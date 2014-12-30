from __future__ import with_statement
from functools import partial
from itertools import chain
import Live
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.Layer import Layer
from _Framework.ModesComponent import ModeButtonBehaviour, ModesComponent, AddLayerMode
from _Framework.SessionComponent import SessionComponent
from _Framework.SliderElement import SliderElement
from _Framework.SubjectSlot import subject_slot
from _Framework.Util import nop
from _Framework import Task

from .ButtonElement import ButtonElement
from .DeviceComponent import DeviceComponent, DeviceModeComponent
from .MixerComponent import MixerComponent
from .SkinDefault import make_default_skin
from consts import *
from logmessage import *

# NUM_TRACKS = 8
# LIVE_CHANNEL = 8


# CONSIDER: using OptimizedControlSurface
class VCM600_XL(ControlSurface):

    def __init__(self, c_instance, *a, **k):
        super(VCM600_XL, self).__init__(c_instance=c_instance, *a, **k)
        self._device_selection_follows_track_selection = True
        self._default_skin = make_default_skin()
        with self.component_guard():
            self._create_controls()
        self._initialize_task = self._tasks.add(Task.sequence(Task.wait(1), Task.run(self._create_components)))
        self._initialize_task.kill()
        log_set_logger(self)
        log_message("VCM600 XL has landed.")

    def _create_components(self):
        self._initialize_task.kill()
        self._disconnect_and_unregister_all_components()
        with self.component_guard():
            mixer = self._create_mixer()
            session = self._create_session()
            transport_control = self._create_transport_control()
            view_control = self._create_view_control()
            device = self._create_device()
            session.set_mixer(mixer)
            self.set_device_component(device)

    def _create_controls(self):

        def make_button(identifier, name, ch=VCM_CHANNEL, midi_type = MIDI_CC_TYPE, skin = self._default_skin):
            return ButtonElement(True, midi_type, ch, identifier, name=name, skin=skin)

        def make_button_list(identifiers, name, ch=VCM_CHANNEL):
            return [ make_button(identifier, name % (i + 1), ch, MIDI_NOTE_TYPE, self._default_skin) for i, identifier in enumerate(identifiers) ]

        def make_encoder(identifier, name, ch=VCM_CHANNEL):
            return EncoderElement(MIDI_CC_TYPE, ch, identifier, Live.MidiMap.MapMode.absolute, name=name)

        def make_slider(identifier, name, ch=VCM_CHANNEL):
            return SliderElement(MIDI_CC_TYPE, ch, identifier, name=name)

        # Track Controls:
        self._send_encoders = ButtonMatrixElement(rows=[[ make_encoder(TRACK_SEND_A, '%d_Send_A' % (i + 1), i) for i in xrange(NUM_TRACKS) ], [ make_encoder(TRACK_SEND_B, '%d_Send_B' % (i + 1), i) for i in xrange(NUM_TRACKS) ]])
        self._pan_device_encoders = ButtonMatrixElement(rows=[[ make_encoder(TRACK_PAN, '%d_Pan_Device' % (i + 1), i) for i in xrange(NUM_TRACKS) ]])
        self._resonance_encoders = ButtonMatrixElement(rows=[[ make_encoder(TRACK_RESONANCE, '%d_Filter_Resonance' % (i + 1), i) for i in xrange(NUM_TRACKS) ]])
        self._frequency_encoders = ButtonMatrixElement(rows=[[ make_encoder(TRACK_FREQUENCY, '%d_Filter_Frequency' % (i + 1), i) for i in xrange(NUM_TRACKS) ]])
        self._volume_faders = ButtonMatrixElement(rows=[[ make_slider(TRACK_VOLUME, '%d_Volume' % (i + 1), i) for i in xrange(NUM_TRACKS) ]])
        self._track_gain_encoders = ButtonMatrixElement(rows=[[make_encoder(TRACK_GAIN_HIGH, '%d_Track_Gain_H', i) for i in xrange(NUM_TRACKS)],
                                                              [make_encoder(TRACK_GAIN_MED, '%d_Track_Gain_M', i) for i in xrange(NUM_TRACKS)],
                                                              [make_encoder(TRACK_GAIN_LOW, '%d_Track_Gain_L', i) for i in xrange(NUM_TRACKS)]])
        self._track_select_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_SELECT, '%d_Track_Select', i) for i in xrange(NUM_TRACKS)]])  # this should be a toggle (through the view modes)
        self._clip_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_VIEW_CLIP, '%d_Track_Clip', i) for i in xrange(NUM_TRACKS)]])
        self._cf_assign_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_CF_ASSIGN, '%d_Track_CF_Assign', i) for i in xrange(NUM_TRACKS)]])
        self._track_play_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_PLAY, '%d_Track_Play', i) for i in xrange(NUM_TRACKS)]])
        self._track_stop_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_STOP, '%d_Track_Stop', i) for i in xrange(NUM_TRACKS)]])
        self._track_mute_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_MUTE, '%d_Track_Play', i) for i in xrange(NUM_TRACKS)]])
        self._track_solo_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_SOLO, '%d_Track_Play', i) for i in xrange(NUM_TRACKS)]])
        self._track_gain_buttons = ButtonMatrixElement(rows=[[make_button(TRACK_HIGH_CUT, '%d_Track_Gain_H', i) for i in xrange(NUM_TRACKS)],
                                                             [make_button(TRACK_MED_CUT, '%d_Track_Gain_M', i) for i in xrange(NUM_TRACKS)],
                                                             [make_button(TRACK_LOW_CUT, '%d_Track_Gain_L', i) for i in xrange(NUM_TRACKS)]])

        # don't forget led row by play buttons (vol, clipping?)

        # Device Control:
        self._device_parameter_encoders = ButtonMatrixElement(rows=[chain([ make_encoder(DEVICE_PARAM_ROW_1 + i, 'Device_Parameter_%d' % (i + 1)) for i in xrange(NUM_TRACKS)], [ make_encoder(DEVICE_PARAM_ROW_2 + i, 'Device_Parameter_%d' % (i + 1)) for i in xrange(NUM_TRACKS) ])])
        self._device_parameter_buttons = ButtonMatrixElement(rows=[chain([ make_button(DEVICE_BUTTON_ROW_1 + i, 'Device_Button_%d' % (i + 1)) for i in xrange(NUM_TRACKS)], [ make_encoder(DEVICE_BUTTON_ROW_2 + i, 'Device_Button_%d' % (i + 1)) for i in xrange(NUM_TRACKS) ])])

        # lower row of device parameter encoders & buttons (not sure how to do these)

        # Master/Return Control:

        # Transport Control:

        # Mode buttons:



#       self._pan_device_mode_button = make_button(105, 'Pan_Device_Mode', MIDI_NOTE_TYPE)

        self._mute_mode_button = make_button(106, 'Mute_Mode', MIDI_NOTE_TYPE)
        self._solo_mode_button = make_button(107, 'Solo_Mode', MIDI_NOTE_TYPE)
        self._arm_mode_button = make_button(108, 'Arm_Mode', MIDI_NOTE_TYPE)
        self._up_button = make_button(104, 'Up')
        self._down_button = make_button(105, 'Down')
        self._left_button = make_button(106, 'Track_Left')
        self._right_button = make_button(107, 'Track_Right')
        self._state_buttons = ButtonMatrixElement(rows=[make_button_list(chain(xrange(73, 77), xrange(89, 93)), 'Track_State_%d')])
        self._send_encoder_lights = ButtonMatrixElement(rows=[make_button_list([13,
          29,
          45,
          61,
          77,
          93,
          109,
          125], 'Top_Send_Encoder_Light_%d'), make_button_list([14,
          30,
          46,
          62,
          78,
          94,
          110,
          126], 'Bottom_Send_Encoder_Light_%d')])
        self._pan_device_encoder_lights = ButtonMatrixElement(rows=[make_button_list([15,
          31,
          47,
          63,
          79,
          95,
          111,
          127], 'Pan_Device_Encoder_Light_%d')])

    def _create_mixer(self):
        mixer = MixerComponent(NUM_TRACKS, is_enabled=True, auto_name=True)
        mixer.layer = Layer(track_select_buttons=self._select_buttons, send_controls=self._send_encoders, next_sends_button=self._down_button, prev_sends_button=self._up_button, pan_controls=self._pan_device_encoders, volume_controls=self._volume_faders, send_lights=self._send_encoder_lights, pan_lights=self._pan_device_encoder_lights)
        mixer.on_send_index_changed = partial(self._show_controlled_sends_message, mixer)
        for channel_strip in map(mixer.channel_strip, xrange(NUM_TRACKS)):
            channel_strip.empty_color = 'Mixer.NoTrack'

        mixer_modes = ModesComponent()
        mixer_modes.add_mode('mute', [AddLayerMode(mixer, Layer(mute_buttons=self._state_buttons))])
        mixer_modes.add_mode('solo', [AddLayerMode(mixer, Layer(solo_buttons=self._state_buttons))])
        mixer_modes.add_mode('arm', [AddLayerMode(mixer, Layer(arm_buttons=self._state_buttons))])
        mixer_modes.layer = Layer(mute_button=self._mute_mode_button, solo_button=self._solo_mode_button, arm_button=self._arm_mode_button)
        mixer_modes.selected_mode = 'mute'
        return mixer

    def _create_session(self):
        session = SessionComponent(num_tracks=NUM_TRACKS, is_enabled=True, auto_name=True, enable_skinning=True)
        session.layer = Layer(track_bank_left_button=self._left_button, track_bank_right_button=self._right_button)
        self._on_session_offset_changed.subject = session
        return session

    @subject_slot('offset')
    def _on_session_offset_changed(self):
        session = self._on_session_offset_changed.subject
        self._show_controlled_tracks_message(session)

    def _create_device(self):
        device = DeviceComponent(name='Device_Component', is_enabled=False)
        device.layer = Layer(parameter_controls=self._pan_device_encoders, parameter_lights=self._pan_device_encoder_lights, priority=1)
        device_settings_layer = Layer(bank_buttons=self._state_buttons, prev_device_button=self._left_button, next_device_button=self._right_button, priority=1)
        mode = DeviceModeComponent(component=device, device_settings_mode=[AddLayerMode(device, device_settings_layer)], is_enabled=True)
        mode.layer = Layer(device_mode_button=self._pan_device_mode_button)
        return device

    def _show_controlled_sends_message(self, mixer):
        if mixer.send_index is not None:
            send_index = mixer.send_index
            send_name1 = chr(ord('A') + send_index)
            if send_index + 1 < mixer.num_sends:
                send_name2 = chr(ord('A') + send_index + 1)
                self.show_message('Controlling Send %s and %s' % (send_name1, send_name2))
            else:
                self.show_message('Controlling Send %s' % send_name1)

    def _show_controlled_tracks_message(self, session):
        start = session.track_offset() + 1
        end = min(start + 8, len(session.tracks_to_use()))
        if start < end:
            self.show_message('Controlling Track %d to %d' % (start, end))
        else:
            self.show_message('Controlling Track %d' % start)