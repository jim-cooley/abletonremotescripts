#!/usr/bin/env python

import Live
import time
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *
from _Framework.TransportComponent import TransportComponent
from ConfigurableButtonElement import ConfigurableButtonElement
from MIDI_Map import *

tempo_button_up_interval = 1.0 
tempo_button_down_interval = -1

class CustomTransportComponent(TransportComponent):
    """TransportComponent with custom tempo support"""
    
    def __init__(self):
        TransportComponent.__init__(self)
    
    def button(TransportComponent, note_num):
        return ButtonElement(True, MIDI_NOTE_TYPE, 2, note_num)
    
    def _replace_controller(self, attrname, cb, new_control):
        old_control = getattr(self, attrname, None)
        if old_control is not None:
            old_control.remove_value_listener(cb)
        setattr(self, attrname, new_control)
        new_control.add_value_listener(cb)
        self.update()

    def set_tempo_bumpers(self, bump_up_control, bump_down_control):
        self._replace_controller('_tempo_bump_up_control', self._tempo_up_value, bump_up_control)
        self._replace_controller('_tempo_bump_down_control', self._tempo_down_value, bump_down_control)

    def _tempo_shift(self, amount):
        old_tempo = self.song().tempo
        self.song().tempo = max(20, min(999, old_tempo + amount))

    def _tempo_up_value(self, value):
        if value!=0:
            self._tempo_shift(tempo_button_up_interval)
            
    def _tempo_down_value(self, value):
        if value!=0:
            self._tempo_shift(tempo_button_down_interval)
