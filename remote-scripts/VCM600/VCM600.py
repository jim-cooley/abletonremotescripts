# Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_32_static/midi-remote-scripts/VCM600/VCM600.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import *
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.ClipSlotComponent import ClipSlotComponent
from _Framework.SceneComponent import SceneComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.ChannelTranslationSelector import ChannelTranslationSelector

from consts import *
from ViewTogglerComponent import ViewTogglerComponent
from MixerComponent import MixerComponent
from logly import *


class VCM600(ControlSurface):
    """ Script for Vestax's VCM600 Controller """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._setup_session_control()
            self._setup_mixer_control()
            self._setup_device_control()
            self._setup_transport_control()
            self._setup_view_control()
        logly_set_logger(self)
        logly_message("VCM600 loaded.")

    def _setup_session_control(self):
            is_momentary = True
            down_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, SCENE_WHEEL_DOWN)
            up_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, SCENE_WHEEL_UP)
            session = SessionComponent(NUM_TRACKS, NUM_SCENES)
            session.set_select_buttons(down_button, up_button)
            session.selected_scene().set_launch_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, SCENE_WHEEL_CLICK))
            track_stop_buttons = [ ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_STOP) for track in range(NUM_TRACKS) ]
            session.set_stop_track_clip_buttons(tuple(track_stop_buttons))
            for track in range(NUM_TRACKS):
                session.selected_scene().clip_slot(track).set_launch_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_PLAY))

    def _setup_mixer_control(self):
        is_momentary = True
        mixer = MixerComponent(NUM_TRACKS, NUM_RETURNS)
        for track in range(NUM_TRACKS):
            strip = mixer.channel_strip(track)
            strip.set_volume_control(SliderElement(MIDI_CC_TYPE, track, TRACK_VOLUME))
            strip.set_pan_control(EncoderElement(MIDI_CC_TYPE, track, TRACK_PAN, Live.MidiMap.MapMode.absolute))
            strip.set_send_controls((EncoderElement(MIDI_CC_TYPE, track, TRACK_SEND_A, Live.MidiMap.MapMode.absolute), EncoderElement(MIDI_CC_TYPE, track, TRACK_SEND_B, Live.MidiMap.MapMode.absolute)))
            strip.set_solo_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_SOLO))
            strip.set_mute_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_MUTE))
            strip.set_crossfade_toggle(ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_CF_ASSIGN))
            eq = mixer.track_eq(track)
            eq.set_gain_controls(tuple([ EncoderElement(MIDI_CC_TYPE, track, TRACK_GAIN_LOW - index, Live.MidiMap.MapMode.absolute) for index in range(NUM_TRACK_GAINS) ]))
            eq.set_cut_buttons(tuple([ ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_LOW_CUT - index) for index in range(NUM_TRACK_GAINS) ]))
            filter = mixer.track_filter(track)
            filter.set_filter_controls(EncoderElement(MIDI_CC_TYPE, track, TRACK_FREQUENCY, Live.MidiMap.MapMode.absolute), EncoderElement(MIDI_CC_TYPE, track, TRACK_RESONANCE, Live.MidiMap.MapMode.absolute))

        for ret_track in range(NUM_RETURNS):
            strip = mixer.return_strip(ret_track)
            strip.set_volume_control(SliderElement(MIDI_CC_TYPE, VCM_CHANNEL, RETURN_VOLUME + ret_track))
            strip.set_pan_control(EncoderElement(MIDI_CC_TYPE, VCM_CHANNEL, RETURN_PAN + ret_track, Live.MidiMap.MapMode.absolute))
            strip.set_mute_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, RETURN_MUTE + ret_track))

        mixer.set_crossfader_control(SliderElement(MIDI_CC_TYPE, VCM_CHANNEL, CROSS_FADER))
        mixer.set_prehear_volume_control(EncoderElement(MIDI_CC_TYPE, VCM_CHANNEL, CUE_VOLUME, Live.MidiMap.MapMode.absolute))
        mixer.master_strip().set_volume_control(SliderElement(MIDI_CC_TYPE, VCM_CHANNEL, MASTER_VOLUME))
        mixer.master_strip().set_pan_control(EncoderElement(MIDI_CC_TYPE, VCM_CHANNEL, MASTER_PAN, Live.MidiMap.MapMode.absolute))
        return mixer

    def _setup_device_control(self):
        is_momentary = True
        device_bank_buttons = []
        device_param_controls = []
        for index in range(NUM_DEVICE_BUTTONS):
            device_bank_buttons.append(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, DEVICE_BUTTON_ROW_1 + index))
            device_param_controls.append(EncoderElement(MIDI_CC_TYPE, VCM_CHANNEL, DEVICE_PARAM_ROW_1 + index, Live.MidiMap.MapMode.absolute))

        device = DeviceComponent()
        device.set_bank_buttons(tuple(device_bank_buttons))
        device.set_parameter_controls(tuple(device_param_controls))
        device_translation_selector = ChannelTranslationSelector()
        device_translation_selector.set_controls_to_translate(tuple(device_param_controls))
        device_translation_selector.set_mode_buttons(tuple(device_bank_buttons))
        self.set_device_component(device)

    def _setup_transport_control(self):
        is_momentary = True
        transport = TransportComponent()
        transport.set_play_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, TRANSPORT_PLAY))
        transport.set_record_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, TRANSPORT_RECORD))
        transport.set_nudge_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, TEMPO_NUDGE_RIGHT), ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, TEMPO_NUDGE_LEFT))
        transport.set_loop_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, TRANSPORT_LOOP))
        transport.set_punch_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, LOOP_IN), ButtonElement(is_momentary, MIDI_NOTE_TYPE, VCM_CHANNEL, LOOP_OUT))
        transport.set_tempo_control(SliderElement(MIDI_CC_TYPE, VCM_CHANNEL, TEMPO_COURSE), SliderElement(MIDI_CC_TYPE, VCM_CHANNEL, TEMPO_FINE))

    def _setup_view_control(self):
        is_momentary = True
        view = ViewTogglerComponent(NUM_TRACKS)
        view.set_buttons(tuple([ ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_VIEW_DEVICE) for track in range(NUM_TRACKS) ]), tuple([ ButtonElement(is_momentary, MIDI_NOTE_TYPE, track, TRACK_VIEW_CLIP) for track in range(NUM_TRACKS) ]))

    def handle_sysex(self, midi_bytes):
        self._suppress_send_midi = False
        self._suppress_session_highlight = False
        self.set_enabled(True)
#       self._on_selected_track_changed()
#       self._do_combine()