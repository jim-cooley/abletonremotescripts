# Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_32_static/midi-remote-scripts/VCM600/TrackFilterComponent.py
import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.EncoderElement import EncoderElement
from _Generic.Devices import get_parameter_by_name

from consts import *
from logly import *


FILTER_DEVICES = {'AutoFilter': {'Frequency': 'Frequency',
                                 'Resonance': 'Resonance'},
                  'Chorus': {'Frequency': 'Feedback',
                             'Resonance': 'Dry/Wet'},
                  'CrossDelay': {'Frequency': 'Feedback',
                                 'Resonance': 'Dry/Wet'},
                  'Eq8': {'Frequency': '3 Frequency A',
                          'Resonance': '3 Resonance A'},
                  'FilterEQ3': {'Frequency': 'FreqHi'},
                  'FilterDelay': {'Frequency': '2 Filter Freq',
                                  'Resonance': 'Dry'},
                  'Operator': {'Frequency': 'Filter Freq',
                               'Resonance': 'Filter Res'},
                  'OriginalSimpler': {'Frequency': 'Filter Freq',
                                      'Resonance': 'Filter Res'},
                  'PingPongDelay': {'Resonance': 'Dry/Wet'},
                  'MultiSampler': {'Frequency': 'Filter Freq',
                                   'Resonance': 'Filter Res'},
                  'Reverb': {'Resonance': 'Dry/Wet'},
                  'UltraAnalog': {'Frequency': 'F1 Freq',
                                  'Resonance': 'F1 Resonance'},
                  'StringStudio': {'Frequency': 'Filter Freq',
                                   'Resonance': 'Filter Reso'}}


class TrackFilterComponent(ControlSurfaceComponent):
    """ Class representing a track's filter, attaches to the last filter in the track """

    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._track = None
        self._device = None
        self._freq_control = None
        self._reso_control = None

    def disconnect(self):
        if self._freq_control != None:
            self._freq_control.release_parameter()
            self._freq_control = None
        if self._reso_control != None:
            self._reso_control.release_parameter()
            self._reso_control = None
        if self._track != None:
            self._track.remove_devices_listener(self._on_devices_changed)
            self._track = None
        self._device = None

    def on_enabled_changed(self):
        logly_message("VCM: Filter got enabled changed")
        self.update()

    def set_track(self, track):
        logly_message("VCM: Filter entering track change")
        assert (track == None or isinstance(track, Live.Track.Track))
        logly_message("VCM: Filter got track change")
        logly_message("%s" % FILTER_DEVICES)
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            if self._device is not None:
                if self._freq_control is not None: self._freq_control.release_parameter()
                if self._reso_control is not None: self._reso_control.release_parameter()
        self._track = track
        if self._track is not None:
            self._track.add_devices_listener(self._on_devices_changed)
            self._on_devices_changed()

    def set_filter_controls(self, freq, reso):
        assert isinstance(freq, EncoderElement)
        assert isinstance(reso, EncoderElement)
        if self._device is not None:
            if self._freq_control is not None: self._freq_control.release_parameter()
            if self._reso_control is not None: self._reso_control.release_parameter()
        self._freq_control = freq
        self._reso_control = reso
        self.update()

    def update(self):
        super(TrackFilterComponent, self).update()
        logly_message("VCM: Filter update called.")
        logly_message("VCM: Filter update called: Enabled(%s), device is %s" % (self.is_enabled(), "None" if self._device is None else "not None"))
        if self.is_enabled() and self._device is not None:
            logly_message("VCM: Filter updating device: %s" % self._device.class_name)
            device_dict = FILTER_DEVICES[self._device.class_name]
            if self._freq_control is not None:
                self._freq_control.release_parameter()
                if 'Frequency' in device_dict.keys():
                    parameter = get_parameter_by_name(self._device, device_dict['Frequency'])
                    if parameter is not None:
                        logly_message("VCM: Filter connecting 'Frequency' knob to %s" % parameter.original_name)
                        self._freq_control.connect_to(parameter)
            if self._reso_control is not None:
                self._reso_control.release_parameter()
                if 'Resonance' in device_dict.keys():
                    parameter = get_parameter_by_name(self._device, device_dict['Resonance'])
                    if parameter is not None:
                        logly_message("VCM: Filter connecting 'Resonance' knob to %s" % parameter.original_name)
                        self._reso_control.connect_to(parameter)

    def _on_devices_changed(self):
        logly_message("VCM: Filter got on device changed")
        logly_message("%s" % FILTER_DEVICES)
        self._device = None
        if self._track != None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                logly_message("VCM: Filter found " + device.class_name)
                if device.class_name in FILTER_DEVICES.keys():
                    self._device = device
                    break
        self.update()