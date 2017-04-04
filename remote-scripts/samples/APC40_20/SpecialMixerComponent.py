# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

from _Framework.MixerComponent import MixerComponent 
from SpecialChannelStripComponent import SpecialChannelStripComponent 
from _Framework.ButtonElement import ButtonElement #added
from _Framework.EncoderElement import EncoderElement #added

class SpecialMixerComponent(MixerComponent):
    ' Special mixer class that uses return tracks alongside midi and audio tracks, and only maps prehear when shifted '
    __module__ = __name__

    def __init__(self, num_tracks):
        MixerComponent.__init__(self, num_tracks)
        self._shift_button = None #added
        self._shift_pressed = False #added

        
    def set_shift_button(self, button): #added
        assert ((button == None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if (self._shift_button != button):
            if (self._shift_button != None):
                self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = button
            if (self._shift_button != None):
                self._shift_button.add_value_listener(self._shift_value)
            self.update()

            
    def _shift_value(self, value): #added
        assert (self._shift_button != None)
        assert (value in range(128))
        self._shift_pressed = (value != 0)
        self.update()
        

    def update(self): #added override
        if self._allow_updates:
            master_track = self.song().master_track
            if self.is_enabled():
                if (self._prehear_volume_control != None):
                    if self._shift_pressed: #added 
                        self._prehear_volume_control.connect_to(master_track.mixer_device.cue_volume)
                    else:
                        self._prehear_volume_control.release_parameter() #added        
                if (self._crossfader_control != None):
                    self._crossfader_control.connect_to(master_track.mixer_device.crossfader)
            else:
                if (self._prehear_volume_control != None):
                    self._prehear_volume_control.release_parameter()
                if (self._crossfader_control != None):
                    self._crossfader_control.release_parameter()
                if (self._bank_up_button != None):
                    self._bank_up_button.turn_off()
                if (self._bank_down_button != None):
                    self._bank_down_button.turn_off()
                if (self._next_track_button != None):
                    self._next_track_button.turn_off()
                if (self._prev_track_button != None):
                    self._prev_track_button.turn_off()
            self._rebuild_callback()
        else:
            self._update_requests += 1


    def tracks_to_use(self):
        return (self.song().visible_tracks + self.song().return_tracks)



    def _create_strip(self):
        return SpecialChannelStripComponent()


    def disconnect(self): #added
        MixerComponent.disconnect(self)
        if (self._shift_button != None):
            self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = None
            

# local variables:
# tab-width: 4
