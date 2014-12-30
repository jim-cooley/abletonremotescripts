from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement


class MainControllerComponent(ModeSelectorComponent):

    def __init__(self, *a, **k):
        ModeSelectorComponent.__init__(self, *a, **k)
        self._mode_index = 0
        self._number_of_modes = 0
        self._offset = 0
        self._buttons = None
        self._last_preset = 0

    def set_offset(self, offset = 0):
        assert isinstance(offset, int)
        self._offset = offset
        self.update()

    def assign_buttons(self, buttons, offset = 0):
        assert isinstance(offset, int)
        self._offset = offset
        if(buttons != None):
            for button in buttons:
                assert isinstance(button, MonoButtonElement)
            self._buttons = buttons
        self.update()

    def set_mode_buttons(self, buttons):
        for button in self._modes_buttons:
            button.remove_value_listener(self._mode_value)
        self._modes_buttons = []
        if (buttons != None):
            for button in buttons:
                assert isinstance(button, ButtonElement or MonoButtonElement)
                identify_sender = True
                button.add_value_listener(self._mode_value, identify_sender)
                self._modes_buttons.append(button)
                self._number_of_modes = len(self._modes_buttons) + self._offset
            for index in range(len(self._modes_buttons)):
                if (index + self._offset) == self._last_preset:
                    self._modes_buttons[index].turn_on()
                else:
                    self._modes_buttons[index].turn_off()

    def set_mode_toggle(self, button):
        assert ((button == None) or isinstance(button, ButtonElement or MonoButtonElement))
        if (self._mode_toggle != None):
            self._mode_toggle.remove_value_listener(self._toggle_value)
        self._mode_toggle = button
        if (self._mode_toggle != None):
            self._mode_toggle.add_value_listener(self._toggle_value)

    def number_of_modes(self):
        return self._number_of_modes

    def update(self):
        if(self.is_enabled() is False):
            self.set_mode_buttons(None)
        elif(self.is_enabled() is True):
            if(len(self._modes_buttons) is 0):
                self.set_mode_buttons(self._buttons)
                #self.set_mode_buttons(tuple(self._script._grid[index][5] for index in range(8)))
                #self.set_mode_buttons(self._modes_buttons
        key = str('p'+ str(self._mode_index + 1 + self._offset))
        preset = None

        for track in range(len(self.song().tracks)):
            #self._script.log_message(self.enumerate_track_device(self.song().tracks[track]))
            for device in self.enumerate_track_device(self.song().tracks[track]):
                if(match(key, str(device.name)) != None):
                    preset = device
        for return_track in range(len(self.song().return_tracks)):
            for device in self.enumerate_track_device(self.song().return_tracks[return_track]):
                if(match(key, str(device)) != None):
                    preset = device
        for device in self.enumerate_track_device(self.song().master_track.devices):
            if(match(key, str(device)) != None):
                preset = device

        if(preset != None):
            #self._script._device.set_device(preset)
            self._script.set_appointed_device(preset)
            self._last_preset = self._mode_index + self._offset
        #self._script._device._update()
        for index in range(len(self._modes_buttons)):
            button = self._modes_buttons[button]
            if isinstance(button, ButtonElement):
                if (index + self._offset) == self._last_preset:
                    self._modes_buttons[button].turn_on()
                else:
                    self._modes_buttons[button].turn_off()

    def enumerate_track_device(self, track):
        devices = []
        if hasattr(track, 'devices'):
            for device in track.devices:
                devices.append(device)
                if device.can_have_chains:
                    for chain in device.chains:
                        for chain_device in self.enumerate_track_device(chain):
                            devices.append(chain_device)
        return devices

    def on_enabled_changed(self):
        if(self.is_enabled() is False):
            self.set_mode_buttons(None)
        elif(self.is_enabled() is True):
            if(len(self._modes_buttons) is 0):
                self.set_mode_buttons(self._buttons)
                #self.set_mode_buttons(tuple(self._script._grid[index][5] for index in range(8)))
        for button in range(len(self._modes_buttons)):
            if (button + self._offset) == self._last_preset:
                self._modes_buttons[button].turn_on()
            else:
                self._modes_buttons[button].turn_off()

    def _on_timer(self):
        if (self.is_enabled() and (self._track != None)):
            if (self._toggle_fold_ticks_delay > -1):
                assert self._track.is_foldable
                if (self._toggle_fold_ticks_delay == 0):
                    self._track.fold_state = (not self._track.fold_state)
                self._toggle_fold_ticks_delay -= 1