# Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_32_static/midi-remote-scripts/VCM600/TrackEQComponent.py
import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.EncoderElement import EncoderElement
from _Generic.Devices import get_parameter_by_name

from consts import *
from logly import *


EQ_DEVICES = {'Eq8': {'Gains': [ '%i Gain A' % (index + 1) for index in range(8) ]},
 'FilterEQ3': {'Gains': ['GainLo', 'GainMid', 'GainHi'],
               'Cuts': ['LowOn', 'MidOn', 'HighOn']}}


class TrackEQComponent(ControlSurfaceComponent):
    """ Class representing a track's EQ, it attaches to the last EQ device in the track """

    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._track = None
        self._device = None
        self._gain_controls = None
        self._cut_buttons = None
        return

    def disconnect(self):
        if self._gain_controls is not None:
            for control in self._gain_controls:
                control.release_parameter()
            self._gain_controls = None

        if self._cut_buttons is not None:
            for button in self._cut_buttons:
                button.remove_value_listener(self._cut_value)
            self._cut_buttons = None

        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            self._track = None
            self._device = None

        if self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if 'Cuts' in device_dict.keys():
                cut_names = device_dict['Cuts']
                for cut_name in cut_names:
                    parameter = get_parameter_by_name(self._device, cut_name)
                    if parameter is not None and parameter.value_has_listener(self._on_cut_changed):
                        parameter.remove_value_listener(self._on_cut_changed)
            # self._device = None ? - not in original source
        return

    def on_enabled_changed(self):
        self.update()

    def set_track(self, track):
        assert (track is None) or isinstance(track, Live.Track.Track)
        logly_message("VCM: got track change")
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            if (self._gain_controls is not None) and (self._device is not None):
                for control in self._gain_controls:
                    control.release_parameter()
        self._track = track
        if self._track is not None:
            self._track.add_devices_listener(self._on_devices_changed)
            self._on_devices_changed()
        return

    def set_cut_buttons(self, buttons):
        assert (buttons is None) or isinstance(buttons, tuple)
        if (buttons != self._cut_buttons) and (self._cut_buttons is not None):
            for button in self._cut_buttons:
                button.remove_value_listener(self._cut_value)
            self._cut_buttons = buttons
            if self._cut_buttons is not None:
                for button in self._cut_buttons:
                    button.add_value_listener(self._cut_value, identify_sender=True)
            self.update()
        return

    def set_gain_controls(self, controls):
        assert (controls is not None) and isinstance(controls, tuple) # is not None OR isInstance() - as previous
        if (self._device is not None) and (self._gain_controls is not None):
            for control in self._gain_controls:
                control.release_parameter()
        for control in controls:
            assert (control is not None) and isinstance(control, EncoderElement)
        self._gain_controls = controls
        self.update()
        return

    def update(self):
        super(TrackEQComponent, self).update()
        if self.is_enabled() and self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if self._gain_controls is not None:
                gain_names = device_dict['Gains']
                for index in range(len(self._gain_controls)):
                    self._gain_controls[index].release_parameter()
                    if len(gain_names) > index:
                        parameter = get_parameter_by_name(self._device, gain_names[index])
                        if parameter is not None:
                            self._gain_controls[index].connect_to(parameter)

            if self._cut_buttons is not None and 'Cuts' in device_dict.keys():
                cut_names = device_dict['Cuts']
                for index in range(len(self._cut_buttons)):
                    self._cut_buttons[index].turn_off()
                    if len(cut_names) > index:
                        parameter = get_parameter_by_name(self._device, cut_names[index])
                        if parameter is not None:
                            if parameter.value == 0.0: self._cut_buttons[index].turn_on()
                            if not parameter.value_has_listener(self._on_cut_changed):  parameter.add_value_listener(self._on_cut_changed)

        else:
            if self._cut_buttons is not None:
                for button in self._cut_buttons:
                    if button is not None: button.turn_off()

            if self._gain_controls is not None:
                for control in self._gain_controls:
                    control.release_parameter()

        return

    def _cut_value(self, value, sender):
        assert sender in self._cut_buttons
        assert value in range(128)
        if self.is_enabled() and self._device is not None:
            if not sender.is_momentary() or value != 0:
                device_dict = EQ_DEVICES[self._device.class_name]
                if 'Cuts' in device_dict.keys():
                    cut_names = device_dict['Cuts']
                    index = list(self._cut_buttons).index(sender)
                    if index in range(len(cut_names)):
                        parameter = get_parameter_by_name(self._device, cut_names[index])
                        if (parameter is not None) and parameter.is_enabled: parameter.value = float(int(parameter.value + 1) % 2)
        return

    def _on_devices_changed(self):
        logly_message("VCM: got device change")
        if self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if 'Cuts' in device_dict.keys():
                cut_names = device_dict['Cuts']
                for cut_name in cut_names:
                    parameter = get_parameter_by_name(self._device, cut_name)
                    if (parameter is not None) and parameter.value_has_listener(self._on_cut_changed):
                        parameter.remove_value_listener(self._on_cut_changed)
                self._device = None

        if self._track is not None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                logly_message("VCM: Looking for EQ: " + device.class_name)
                if device.class_name in EQ_DEVICES.keys():
                    self._device = device
                    break

        self.update()
        return

    def _on_cut_changed(self):
        assert self._device is not None
        assert 'Cuts' in EQ_DEVICES[self._device.class_name].keys()
        if self.is_enabled() and self._cut_buttons is not None:
            cut_names = EQ_DEVICES[self._device.class_name]['Cuts']
            for index in range(len(self._cut_buttons)):
                self._cut_buttons[index].turn_off()
                if len(cut_names) > index:
                    parameter = get_parameter_by_name(self._device, cut_names[index])
                    if (parameter is not None) and parameter.value == 0.0:
                        self._cut_buttons[index].turn_on()
        return