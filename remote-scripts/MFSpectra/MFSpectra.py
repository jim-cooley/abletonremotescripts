#!/usr/bin/env python

from __future__ import with_statement
import Live
import time
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.ClipSlotComponent import ClipSlotComponent
from _Framework.CompoundComponent import CompoundComponent
from _Framework.ControlElement import ControlElement
from _Framework.ControlSurface import ControlSurface
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent 
from _Framework.InputControlElement import *
from _Framework.MixerComponent import MixerComponent
from _Framework.SceneComponent import SceneComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.TransportComponent import TransportComponent
from ConfigurableButtonElement import ConfigurableButtonElement
from tempo_control import CustomTransportComponent
from MIDI_Map import *

class MFSpectra(ControlSurface):
    __module__ = __name__
    __doc__ = " Midi Fighter Spectra Control Script "
    
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._suppress_session_highlight = True
            self._suppress_send_midi = True
            self.box_width = box_width
            self.box_height = box_height
            self._session = None
            self._mixer = None
            self._setup_mixer_control()
            self._setup_session_control()
            self._setup_transport_control()
            self.session.set_mixer(self._mixer)
            self._suppress_session_highlight = False

    def _setup_session_control(self):
        is_momentary = True
        num_tracks = 4
        num_scenes = 3
        self.session = SessionComponent(num_tracks, num_scenes)
        self.session.name = 'Session_Control'
        up_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 3, up) 
        up_button.name = 'Bank_Select_Up_Button'
        down_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 3, down)
        down_button.name = 'Bank_Select_Down_Button'
        self.session.set_scene_bank_buttons(down_button, up_button)
        right_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 3, right)
        right_button.name = 'Bank_Select_Right_Button'
        left_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 3, left)
        left_button.name = 'Bank_Select_Left_Button'
        self.session.set_track_bank_buttons(right_button, left_button)
        matrix = ButtonMatrixElement()
        matrix.name = 'Button_Matrix'
        track_stop_buttons = [self.set_button(2, stop_track_buttons[index], RED, RED) for index in range(len(stop_track_buttons))]
        for index in range(len(track_stop_buttons)):
            track_stop_buttons[index].name = 'Track_' + str(index) + '_Stop_Button'
        self.session.set_stop_track_clip_buttons(tuple(track_stop_buttons))
        launch_button_list_len = len(launch_button_list)
        launch_ctr = launch_button_list_len -1
        launch_button_list.reverse()
        self.clip_loaded_stopped = BLUE
        self.clip_currently_playing = GREEN
        self.clip_triggered_to_play = YELLOW
        for scene_index in range(self.box_height):
            scene = self.session.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            button_row = []
            for track_index in range(self.box_width): 
                button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 2, launch_button_list[launch_ctr])
                launch_ctr = launch_ctr -1
                button.name = str(track_index) + '_Clip_' + str(scene_index) + '_Button'
                button_row.append(button)
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
                clip_slot.set_stopped_value(self.clip_loaded_stopped )
                clip_slot.set_started_value(self.clip_currently_playing)
                clip_slot.set_triggered_to_play_value(self.clip_triggered_to_play)                   
                clip_slot.set_launch_button(button)
            matrix.add_row(tuple(button_row))
        self.set_highlighting_session_component(self.session)
        return None

    def _setup_mixer_control(self):
        is_momentary = True
        self._mixer = MixerComponent(4)
        self._mixer.name = 'Mixer'
        self._mixer.selected_strip().name = 'Selected_Channel_Strip'  
        for index in range(self.box_width):
            strip = self._mixer.channel_strip(index)
            strip.name = 'Channel_Strip_' + str(index)
            strip.set_arm_button(self.set_button(2, arm_track_buttons[index], RED, REDLOW))
            strip.set_mute_button(self.set_button(2, mute_track_buttons[index], YELLOWLOW, YELLOW))
            strip.set_select_button(self.set_button(2, select_track_buttons[index], AQUA, OFF))
            strip.set_invert_mute_feedback(True)
            
    def _setup_transport_control(self):
        is_momentary = True
        transport = CustomTransportComponent()
        transport.name = 'Transport'
        transport.set_play_button(self.set_button(2, play, GREEN, GREENLOW))
        transport.set_stop_button(self.set_button(2, stop, RED, RED))
        transport.set_tempo_bumpers(transport.button(tempo_button_up), transport.button(tempo_button_down))
        
    def set_button(self, _channel, _note, _on_color, _off_color):
        button = None
        if not _note is -1:
            button = ConfigurableButtonElement(True, MIDI_NOTE_TYPE, _channel, _note, _on_color, _off_color)
        return button

    def disconnect(self):
        ControlSurface.disconnect(self)
        return None
