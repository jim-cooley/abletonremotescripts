MASTER_CHAN = VCM_CHANNEL
MASTER_CC = { 'channel':        MASTER_CHAN,

              # media control
              'all_stop':       MASTER_I,
              'scene_play':     MASTER_J,

              # scene control
              'scene_up':       SCENE_WHEEL_UP,
              'scene_down':     SCENE_WHEEL_DOWN,
              'scene_select':   SCENE_WHEEL_CLICK,

              # tempo control
              'tempo_course':   TEMPO_COURSE,
              'tempo_fine':     TEMPO_FINE,
              'tempo_increase': TEMPO_NUDGE_RIGHT,
              'tempo_decrease': TEMPO_NUDGE_LEFT,

              # master control
              'cue_level':      CUE_LEVEL,
              'cross_fade':     CROSS_FADER,
              'master_pan':     MASTER_PAN,
              'master_level':   MASTER_LEVEL,
            }


RETURNS_CC = [ # RETURN A
             {'channel':        MASTER_CHAN,
              'pan':            RETURN_PAN,
              'mute':           RETURN_MUTE
              'level':          RETURN_LEVEL,
              },

              # RETURN B
             {'channel':        MASTER_CHAN,
              'pan':            RETURN_PAN + 1 },
              'mute':           RETURN_MUTE + 1 }
              'level':          RETURN_LEVEL + 1 },
              }
            ]


TRACKS_CHAN = [ 0, 1, 2, 3, 4, 5 ]
TRACKS_CC_TEMPLATE = {'channel':          0,

             # track control
             'select'            TRACK_SELECT,
             'clip_start':       TRACK_CLIP_START,
             'clip_stop':        TRACK_CLIP_STOP,
             'mute':             TRACK_MUTE,
             'solo':             TRACK_SOLO,

             'view_clip':        TRACK_VIEW_CLIP,
             'view_device':      TRACK_VIEW_DEVICE,

             # EQ
             'eq_gains':         [ TRACK_GAIN_LOW,   TRACK_GAIN_MED,     TRACK_GAIN_HIGH ],
             'eq_qs':            [ None,             TRACK_RESONANCE,    None ],
             'eq_freqs':         [ None,             TRACK_FREQUENCY,    None ],
             'eq_cuts':          [ TRACK_LOW_CUT,    TRACK_MED_CUT,      TRACK_HIGH_CUT ],

             # pan, send, cross-fader
             'pan':              TRACK_PAN,
             'sends':            [ TRACK_SEND_A, TRACK_SEND_B ],
             'cf_assign':        TRACK_CF_ASSIGN,
            }

DEVICES_CHAN = VCM_CHANNEL
DEVICES_CC ={'buttons':         [ DEVICE_BANK_1 + 0,  DEVICE_BANK_1 + 1,  DEVICE_BANK_1 + 2,  DEVICE_BANK_1 + 3,
                                  DEVICE_BANK_1 + 4,  DEVICE_BANK_1 + 5,  DEVICE_BANK_1 + 6,  DEVICE_BANK_1 + 7 ],
             'gains':           [ DEVICE_PARAM_1 + 0, DEVICE_PARAM_1 + 1, DEVICE_PARAM_1 + 2, DEVICE_PARAM_1 + 3,
                                  DEVICE_PARAM_1 + 4, DEVICE_PARAM_1 + 5, DEVICE_PARAM_1 + 6, DEVICE_PARAM_1 + 7 ],
            }

# mode-changing toggles
TOGGLES_CC ={'user_mode':       0,
             'bank_mode':       0,
            }

BANK_CHAN = VCM_CHANNEL
BANK_SIZE = 12
BOARD_SIZE= 6
BANK_CC =   {'bank_select':     0,
             'bank_next':       0,
             'bank_prev':       0,  # switch next bank (set of BANK_SIZE)
             'board_ab':        0,  # switch between two banks a/b (BOARD_SIZE)

             # direct nav
             'bank_1':          0,
             'bank_2':          0,
             'bank_3':          0,
             'bank_4':          0,
             'bank_5':          0,
             'bank_6':          0,
            }

#
# USER_MODE
#
USER_MODE_CHAN = VCM_CHANNEL
USER_MODE_CC = { 'channel':        MASTER_CHAN,

              # media control
              'all_stop':       MASTER_I,
              'scene_play':     MASTER_J,

              # scene control
              'scene_up':       SCENE_WHEEL_UP,
              'scene_down':     SCENE_WHEEL_DOWN,
              'scene_select':   SCENE_WHEEL_CLICK,

              # tempo control
              'tempo_course':   TEMPO_COURSE,
              'tempo_fine':     TEMPO_FINE,
              'tempo_increase': TEMPO_NUDGE_RIGHT,
              'tempo_decrease': TEMPO_NUDGE_LEFT,

              # master control
              'cue_level':      CUE_LEVEL,
              'cross_fade':     CROSS_FADER,
              'master_pan':     MASTER_PAN,
              'master_level':   MASTER_LEVEL,
            }


USER_RETURNS_CC = [ # RETURN A
             {'channel':        MASTER_CHAN,
              'pan':            RETURN_PAN,
              'mute':           RETURN_MUTE
              'level':          RETURN_LEVEL,
              },

              # RETURN B
             {'channel':        MASTER_CHAN,
              'pan':            RETURN_PAN + 1 },
              'mute':           RETURN_MUTE + 1 }
              'level':          RETURN_LEVEL + 1 },
              }
            ]


USER_TRACKS_CHAN = [ 0, 1, 2, 3, 4, 5 ]
USER_TRACKS_CC_TEMPLATE = {'channel':          0,

             # track control
             'select'            TRACK_SELECT,
             'clip_start':       TRACK_CLIP_START,
             'clip_stop':        TRACK_CLIP_STOP,
             'mute':             TRACK_MUTE,
             'solo':             TRACK_SOLO,

             'view_clip':        TRACK_VIEW_CLIP,
             'view_device':      TRACK_VIEW_DEVICE,

             # EQ
             'eq_gains':         [ TRACK_GAIN_LOW,   TRACK_GAIN_MED,     TRACK_GAIN_HIGH ],
             'eq_qs':            [ None,             TRACK_RESONANCE,    None ],
             'eq_freqs':         [ None,             TRACK_FREQUENCY,    None ],
             'eq_cuts':          [ TRACK_LOW_CUT,    TRACK_MED_CUT,      TRACK_HIGH_CUT ],

             # pan, send, cross-fader
             'pan':              TRACK_PAN,
             'sends':            [ TRACK_SEND_A, TRACK_SEND_B ],
             'cf_assign':        TRACK_CF_ASSIGN,
            }

USER_DEVICES_CHAN = VCM_CHANNEL
USER_DEVICES_CC ={ 'buttons':   [ DEVICE_BANK_1 + 0,  DEVICE_BANK_1 + 1,  DEVICE_BANK_1 + 2,  DEVICE_BANK_1 + 3,
                                  DEVICE_BANK_1 + 4,  DEVICE_BANK_1 + 5,  DEVICE_BANK_1 + 6,  DEVICE_BANK_1 + 7 ],
                   'gains':     [ DEVICE_PARAM_1 + 0, DEVICE_PARAM_1 + 1, DEVICE_PARAM_1 + 2, DEVICE_PARAM_1 + 3,
                                  DEVICE_PARAM_1 + 4, DEVICE_PARAM_1 + 5, DEVICE_PARAM_1 + 6, DEVICE_PARAM_1 + 7 ],
                 }
