# Utility functions

import Live
from _Generic.Devices import get_parameter_by_name
from logly import *

MAX_DEVICES = ('MxDeviceInstrument', 'MxDeviceAudioEffect', 'MxDeviceMidiEffect')


def print_track_info(track):
    if track is not None:
        logly_message("Track: " + track.name)
        logly_message("Type: %s %s %s" % ("Audio" if track.has_audio_input else "MIDI", "Group" if track.is_foldable else "", "Master/Send" if is_master_track(track) else ""))
        logly_message("Muted: %s" %  track.mute)
        if not is_master_track(track):
            logly_message("Status: %s" %  "Solo" if track.solo else "Playing %d" % track.playing_slot_index if track.playing_slot_index >= 0 else "Stopped")
        logly_message("Visible: %s" % track.is_visible)
        logly_message("Selected: %s" % track.is_part_of_selection)
        logly_message("Clip Slots: %d" % len(track.clip_slots))
        logly_message("Devices (%d):" % len(track.devices))
        for i in track.devices:
            print_device_info(i)
            logly_message("")

def is_master_track(track):
    return not track.can_be_armed

def print_device_info(device):
    if device is not None:
        logly_message("Device: %s = %s[%s]" % (device.name, device.class_display_name, device.class_name))
        logly_message("Type: %s" % device.type)
        logly_message("Is Rack: %s" % device.can_have_chains)
        logly_message("Is Drums: %s" % device.can_have_drum_pads)
        logly_message("Parameters: ")
        for i in device.parameters:
            logly_message("   %s[%s] = %s" % (i.name, i.original_name, i.value))

        banks = 0
        if device.class_name in MAX_DEVICES:
            try:
                banks = device.get_bank_count()
            except:
                banks = 0
        logly_message("Bank Count: %d" % banks)

        if banks>0:
            logly_message("Bank Names: ")
            for i in range(device.get_bank_count()):
                logly_message("  Bank: %s" % device.get_bank_name(i))
                for j in device.get_bank_parameters(i):
                    logly_message("Parameter: %s[%s] = %s" % (j.name, j.original_name, j.value))
    else:
        logly_message("Device: None")

def enumerate_track_devices(self, track, expand_rack_devices=False):
    devices = []
    if hasattr(track, 'devices'):
        for device in track.devices:
            devices.append(device)
            if expand_rack_devices and device.can_have_chains:
                for chain in device.chains:
                    for chain_device in self.enumerate_track_device(chain, expand_rack_devices):
                        devices.append(chain_device)
    return devices

def get_parameter_by_name(device, name):
    """ Find the given device's parameter that belongs to the given name """
    for i in device.parameters:
        if i.original_name == name:
            return i