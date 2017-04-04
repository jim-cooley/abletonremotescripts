# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from _Framework.SessionZoomingComponent import SessionZoomingComponent 
from _Framework.ButtonElement import ButtonElement 
class ShiftableZoomingComponent(SessionZoomingComponent):
    ' Special ZoomingComponent that uses clip stop buttons for stop all when zoomed '
    __module__ = __name__

    def __init__(self, session, stop_buttons):
        SessionZoomingComponent.__init__(self, session)
        self._stop_buttons = stop_buttons
        self._ignore_buttons = False
        for button in self._stop_buttons:
            assert isinstance(button, ButtonElement)
            button.add_value_listener(self._stop_value, identify_sender=True)




    def disconnect(self):
        SessionZoomingComponent.disconnect(self)
        for button in self._stop_buttons:
            button.remove_value_listener(self._stop_value)




    def set_ignore_buttons(self, ignore):
        assert isinstance(ignore, type(False))
        if (self._ignore_buttons != ignore): #if ignore state changes..
            self._ignore_buttons = ignore #set new state
            if (not self._is_zoomed_out): #if in session/clip view..
                if ignore: #disable clip slots on ignore
                    for scene_index in range(5):
                        scene = self._session.scene(scene_index)
                        for track_index in range(8):
                            clip_slot = scene.clip_slot(track_index)
                            clip_slot.set_enabled(False)                          
                else: #re-enable clip slots on ignore
                    for scene_index in range(5):
                        scene = self._session.scene(scene_index)
                        for track_index in range(8):
                            clip_slot = scene.clip_slot(track_index)
                            clip_slot.set_enabled(True)                          
                #self._session.set_enabled((not ignore)) 
            self.update()



    def update(self):
        if (not self._ignore_buttons):
            SessionZoomingComponent.update(self)
        elif self.is_enabled():
            if (self._scene_bank_buttons != None):
                for button in self._scene_bank_buttons:
                    button.turn_off()




    def _stop_value(self, value, sender):
        assert (value in range(128))
        assert (sender != None)
        if (self.is_enabled() and ((not self._ignore_buttons) and self._is_zoomed_out)):
            if ((value != 0) or (not sender.is_momentary())):
                self.song().stop_all_clips()



    def _zoom_value(self, value):
        assert (self._zoom_button != None)
        assert (value in range(128))
        if self.is_enabled():
            if self._zoom_button.is_momentary():
                self._is_zoomed_out = (value > 0)
            else:
                self._is_zoomed_out = (not self._is_zoomed_out)
            if (not self._ignore_buttons):
                if self._is_zoomed_out:
                    self._scene_bank_index = int(((self._session.scene_offset() / self._session.height()) / self._buttons.height()))
                else:
                    self._scene_bank_index = 0
                self._session.set_enabled((not self._is_zoomed_out))
                if self._is_zoomed_out:
                    self.update()



    def _matrix_value(self, value, x, y, is_momentary):
        if (not self._ignore_buttons):
            SessionZoomingComponent._matrix_value(self, value, x, y, is_momentary)



    #def _nav_up_value(self, value): #comment out to allow shifted navigation on APC40 in Note Mode
        #if (not self._ignore_buttons):
            #SessionZoomingComponent._nav_up_value(self, value)



    #def _nav_down_value(self, value): #comment out to allow shifted navigation on APC40 in Note Mode
        #if (not self._ignore_buttons):
            #SessionZoomingComponent._nav_down_value(self, value)



    #def _nav_left_value(self, value): #comment out to allow shifted navigation on APC40 in Note Mode
        #if (not self._ignore_buttons):
            #SessionZoomingComponent._nav_left_value(self, value)



    #def _nav_right_value(self, value): #comment out to allow shifted navigation on APC40 in Note Mode
        #if (not self._ignore_buttons):
            #SessionZoomingComponent._nav_right_value(self, value)



    def _scene_bank_value(self, value, sender):
        if (not self._ignore_buttons):
            SessionZoomingComponent._scene_bank_value(self, value, sender)


# local variables:
# tab-width: 4
