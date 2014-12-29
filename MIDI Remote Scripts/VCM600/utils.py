# Utility functions

import Live
from _Generic.Devices import get_parameter_by_name
from logly import *


def print_track_info(track):
    if track is not None:
        logly_message("Track: " + track.name)
        logly_message("Type: %s %s %s" % ("Audio" if track.has_audio_input else "MIDI", " Group" if track.is_foldable else "", " Master/Send" if not track.can_be_armed else ""))
        logly_message("Status: %s" % "Solo" if track.can_be_armed and track.solo else "Mute" if track.mute else "Playing " + track.playing_slot_index if track.playing_slot_index >= 0 else "Stopped")
        logly_message("Visible: %s" % track.is_visible)
        logly_message("Selected: %s" % track.is_part_of_selection)
        logly_message("Clip Slots: %d" % len(track.clip_slots))
        logly_message("Devices (%d):" % len(track.devices))
        for i in track.devices:
            print_device_info(i)
            logly_message("")

def print_device_info(device):
    if device is not None:
        logly_message("Device: %s = %s[%s]" % (device.name, device.class_display_name, device.class_name))
        logly_message("Type: %s" % device.type)
        logly_message("Is Rack: %s" % device.can_have_chains)
        logly_message("Is Drums: %s" % device.can_have_drum_pads)
        logly_message("Parameters: ")
        for i in device.parameters:
            logly_message("   %s[%s] = %s" % (i.name, i.original_name, i.value))

        bank_count = device.get_bank_count()
        logly_message("Bank Count: %d" % bank_count)
        if bank_count>0:
            logly_message("Bank Names: ")
            for i in range(device.get_bank_count()):
                logly_message("  Bank: %s" % device.get_bank_name(i))
                for j in device.get_bank_parameters(i):
                    logly_message("Parameter: %s[%s] = %s" % (j.name, j.original_name, j.value))
    else:
        logly_message("Device: None")