
####### ALL CONTROLS ARE CC

num_tracks = 8
num_scenes = 0
session_left = 82
session_right = 81
session_up = 80
session_down = 83
send_up = 45
send_down = 44
# initial_mod = 42 : not implemented
shift_mod = 46
alt_mod = 40
ctrl_mod = 47
modifiers_buttons = [shift_mod, alt_mod, ctrl_mod]

# INITIAL MODE CONSTS
mixer_volumefader_cc = [0, 1, 2, 3, 4, 5, 6, 7]
mixer_sendknob_cc = [8, 9, 10, 11, 12, 13, 14, 15]
track_solo_cc = [16,17,18,19,20,21,22,23]
track_mute_cc = [24,25,26,27,28,29,30,31]
track_arm_cc = [32,33,34,35,36,37,38,39]

# SHIFT MODE CONSTS

# ALT MODE CONSTS
track_resetsend_cc =[16,17,18,19,20,21,22,23]
track_select_cc = [24,25,26,27,28,29,30,31]
stop_track_cc = [32,33,34,35,36,37,38,39]

# CTRL MODE CONSTS
detailclip_view_cc = [16,17,18,19,20,21,22,23]
lock_device_cc = 43
onoff_device_cc = 60
device_param_cc = [8, 9, 10, 11, 12, 13, 14, 15]
device_left_cc = 44
device_right_cc = 45
transport_stop_cc = 48
transport_play_cc = 49
transport_record_cc = 50
transport_quantization_cc = 35
transport_tempodown_cc = 36
transport_tempoup_cc = 37
transport_metronome_cc = 42
session_stopall_cc = 39
session_scenelaunch_cc = [24,25,26]
# mixer_masterselect_cc = 31   : Not implemented
# mixer_mastervol_cc = 7         : Not implemented

CHANNEL = 0 # Channels are numbered 0 through 15, this script only makes use of one MIDI Channel (Channel 1)