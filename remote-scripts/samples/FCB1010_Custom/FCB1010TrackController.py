import Live
from FCB1010Component import FCB1010Component

from consts import *
from devices import *

class FCB1010TrackController(FCB1010Component):
    __module__ = __name__
    __doc__ = "Track controller for FCB1010 remote control surface"
    __filter_funcs__ = ["update_display", "log"]

    def __init__(self, parent):
	FCB1010Component.realinit(self, parent)

    def clip_is_recording(self, clip):
	return (clip.looping and clip.is_playing and (clip.loop_end == 63072000.0))

    def record_clip(self, track_idx):
	if (track_idx < len(self.song().tracks)):
	    track = self.song().tracks[track_idx]
	    scene = self.parent.song().view.selected_scene
	    if track.can_be_armed:
		if track.arm:
		    track.arm = 0
		else:
		    self.arm_track(track)

    def toggle_clip(self, track_idx):
	scene = self.parent.song().view.selected_scene
	if (track_idx < len(scene.clip_slots)):
	    slot = scene.clip_slots[track_idx]
	    if (slot.has_clip):
		clip = slot.clip
		if (clip.is_playing and not self.clip_is_recording(clip)):
		    clip.stop()
		else:
		    clip.fire()
	    else:
		slot.fire()

    def record_empty_clip_idx(self, track_idx):
	if (track_idx < len(self.song().tracks)):
	    self.record_empty_clip(self.song().tracks[track_idx])
	
    def find_similar_tracks(self, track):
	def first_word(string):
	    end = string.find(" ")
	    if (end == -1):
		return string
	    else:
		return string[0:end]

	name = first_word(track.name)
	return [ t for t in self.song().tracks if ((first_word(t.name) == name) and (t != track))]

    def arm_track_idx(self, track_idx):
	if (len(self.song().tracks) > track_idx):
	    return self.arm_track(self.song().tracks[track_idx])
    
    def arm_track(self, track):
	tracks = self.find_similar_tracks(track)
	for t in tracks:
	    if t.can_be_armed and t.arm:
		t.arm = 0
	track.arm = 1
    
    def record_empty_clip(self, track):
	def index_of(list, elt):
	    for i in range(0,len(list)):
		if (list[i] == elt):
		    return i
	
	if track.can_be_armed:
	    self.arm_track(track)
	else:
	    return
	
	start_idx = index_of(self.song().scenes, self.song().view.selected_scene)
	if not start_idx:
	    start_idx = 0

	for idx in range(start_idx, len(track.clip_slots)):
	    if not track.clip_slots[idx].has_clip:
		self.song().view.selected_scene = self.song().scenes[idx]
		track.clip_slots[idx].fire()
		return
	
    def find_first_rack_device(self, track):
	self.log("track name %s" % track.name)
	for dev in track.devices:
	    self.log("checking dev for rack %s" % dev.class_name)
	    if dev.class_name in ["AudioEffectGroupDevice",
				  "InstrumentGroupDevice",
				  "MidiEffectGroupDevice"]:
		return dev
	return None

    def find_last_rack_device(self, track):
	for i in range(0, len(track.devices)):
	    dev = track.devices[-(i+1)]
	    if dev.class_name in ["AudioEffectGroupDevice",
				  "InstrumentGroupDevice",
				  "MidiEffectGroupDevice"]:
		return dev
	return None
    
    def get_device_bob(self, device):
	return DEVICE_DICT[device.class_name]

    def get_parameter_by_name(self, device, name):
        result = 0
        for i in device.parameters:
            if (i.original_name == name):
		return i

        return None

    def rack_select(self, rack, idx):
	param = self.get_parameter_by_name(rack, "Chain Selector")
	param.value = idx * 8

    def first_rack_select(self, track_idx, idx):
	if (len(self.song().tracks) > track_idx):
	    track = self.song().tracks[track_idx]
	    rack = self.find_first_rack_device(track)
	    if rack:
		self.rack_select(rack, idx)

    def last_rack_select(self, track_idx, idx):
	if (len(self.song().tracks) > track_idx):
	    track = self.song().tracks[track_idx]
	    rack = self.find_last_rack_device(track)
	    if rack:
		self.rack_select(rack, idx)

    def master_first_rack_select(self, track_idx, idx):
	rack = self.find_first_rack_device(self.song().master_track)
	self.log("set rack select %s on master rack %s" % (idx, rack))
	if rack:
	    self.rack_select(rack, idx)

    def master_last_rack_select(self, track_idx, idx):
	rack = self.find_last_rack_device(self.song().master_track)
	self.log("set rack select %s on master rack %s" % (idx, rack))
	if rack:
	    self.rack_select(rack, idx)
	    
    def get_device_drywet(self, device):
	if (DRYWET_DICT.has_key(device.class_name)):
	    return self.get_parameter_by_name(device, DRYWET_DICT[device.class_name])

    def get_device_param(self, device, idx):
	bank = self.get_device_bob(device)
	return self.get_parameter_by_name(device, bank[idx])
    
    def find_first_device(self, track):
	if (len(track.devices) > 0):
	    return track.devices[0]

    def find_last_device(self, track):
	if (len(track.devices) > 0):
	    return track.devices[-1]
	
    def first_fx_param_1(self, track):
	device = self.find_first_device(track)
	if device:
	    return self.get_device_param(device, 0)
	
    def first_fx_param_2(self, track):
	device = self.find_first_device(track)
	if device:
	    return self.get_device_param(device, 1)

    def last_fx_param_1(self, track):
	device = self.find_first_device(track)
	if device:
	    return self.get_device_param(device, 0)
	
    def last_fx_param_2(self, track):
	device = self.find_first_device(track)
	if device:
	    return self.get_device_param(device, 1)
	    
    def first_rack_param_1(self, track):
	rack = self.find_first_rack_device(track)
	if rack:
	    return rack.parameters[1]

    def first_rack_param_2(track):
	rack = self.find_first_rack_device(self, track)
	if rack:
	    return rack.parameters[2]

    def last_rack_param_1(self, track):
	rack = self.find_last_rack_device(track)
	if rack:
	    return rack.parameters[1]

    def last_rack_param_2(track):
	rack = self.find_last_rack_device(self, track)
	if rack:
	    return rack.parameters[2]
	
    def track_volume(self, track):
	return track.mixer_device.volume
    
    def first_fx_drywet(self, track):
	device = self.find_first_device(track)
	if device:
	    return self.get_device_drywet(device)

    def last_fx_drywet(self, track):
	device = self.find_last_device(track)
	if device:
	    return self.get_device_drywet(device)
	
    def build_midi_map(self, script_handle, midi_map_handle):
	def map_cc(channel, cc, parameter, mode):
	    Live.MidiMap.map_midi_cc(midi_map_handle,
				     parameter, channel, cc,
				     mode)

	def map_pedal(type, cc, track):
	    mastertrack = self.song().master_track
	    parameter = None

	    ## XXX SENDS
	    if type == "FIRST_RACK_PARAM_1":
		parameter = self.first_rack_param_1(track)
	    elif type == "FIRST_RACK_PARAM_2":
		parameter = self.first_rack_param_2(track)
	    elif type == "LAST_RACK_PARAM_1":
		parameter = self.last_rack_param_1(track)
	    elif type == "LAST_RACK_PARAM_2":
		parameter = self.last_rack_param_2(track)
	    elif type == "FIRST_FX_PARAM_1":
		parameter = self.first_fx_param_1(track)
	    elif type == "FIRST_FX_PARAM_2":
		parameter = self.first_fx_param_2(track)
	    elif type == "LAST_FX_PARAM_1":
		parameter = self.first_fx_param_1(track)
	    elif type == "LAST_FX_PARAM_2":
		parameter = self.first_fx_param_2(track)
	    elif type == "FIRST_FX_DRYWET":
		parameter = self.first_fx_drywet(track)	
	    elif type == "LAST_FX_DRYWET":
		parameter = self.last_fx_drywet(track)
	    elif type == "TRACK_VOLUME":
		parameter = self.track_volume(track)

	    elif type == "MASTER_FIRST_RACK_PARAM_1":
		parameter = self.first_rack_param_1(mastertrack)
	    elif type == "MASTER_FIRST_RACK_PARAM_2":
		parameter = self.first_rack_param_2(mastertrack)
	    elif type == "MASTER_LAST_RACK_PARAM_1":
		parameter = self.last_rack_param_1(mastertrack)
	    elif type == "MASTER_LAST_RACK_PARAM_2":
		parameter = self.last_rack_param_2(mastertrack)
	    elif type == "MASTER_FIRST_FX_PARAM_1":
		parameter = self.first_fx_param_1(mastertrack)
	    elif type == "MASTER_FIRST_FX_PARAM_2":
		parameter = self.first_fx_param_2(mastertrack)
	    elif type == "MASTER_LAST_FX_PARAM_1":
		parameter = self.first_fx_param_1(mastertrack)
	    elif type == "MASTER_LAST_FX_PARAM_2":
		parameter = self.first_fx_param_2(mastertrack)
	    elif type == "MASTER_FIRST_FX_DRYWET":
		parameter = self.first_fx_drywet(mastertrack)	
	    elif type == "MASTER_LAST_FX_DRYWET":
		parameter = self.last_fx_drywet(mastertrack)
	    elif type == "MASTER_TRACK_VOLUME":
		parameter = self.track_volume(mastertrack)

	    if parameter:
		self.log("map pedal type %s, cc %s, track %s" % (type, cc, track))
		map_cc(FCB1010_CHANNEL, cc, parameter, Live.MidiMap.MapMode.absolute)
    
	for idx in range(0,9):
	    if (idx < len(self.song().tracks)):
		track = self.song().tracks[idx]
		type_a = TRACK_CONTROLLER[PEDAL_A]
		type_b = TRACK_CONTROLLER[PEDAL_B]
		cc_a = TRACK_PEDAL_CCS[idx+1][0]
		cc_b = TRACK_PEDAL_CCS[idx+1][1]
		map_pedal(type_a, cc_a, track)
		map_pedal(type_b, cc_b, track)

	mastertrack = self.song().master_track
	map_pedal(MAIN_CONTROLLER[PEDAL_A], TRACK_PEDAL_CCS[0][0], mastertrack)
	map_pedal(MAIN_CONTROLLER[PEDAL_B], TRACK_PEDAL_CCS[0][1], mastertrack)

    def disconnect(self):
	pass
    
