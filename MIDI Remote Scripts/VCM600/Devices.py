



EQ_DEVICES = {'Eq8': {'Gains': ( '%i Gain A' % (index + 1) for index in range(8) ),
                      'Cuts': ( '%i Filter On A' % (index + 1) for index in range(8))},
              'FilterDelay': {'Gains': ('1 Volume', '2 Volume', '3 Volume'),
                              'Cuts': ('1 Filter On', '2 Filter On', '3 Filter On')}}

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


# Need Banks for parameters & best of for bank #1 if there are more than two

#Rack devices (may have rack specific over-rides in separate dict)
RCK_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7', 'Macro 8')
RCK_BANKS = (RCK_BANK1,)
RCK_BOBS = (RCK_BANK1,)
RCK_BNK_NAMES = ('Macros',)

# UltraAnalog (Instrument)
ALG_BANK1 = ('OSC1 Level', 'OSC1 Octave', 'OSC1 Semi', 'OSC1 Shape', 'OSC2 Level', 'OSC2 Octave', 'OSC2 Semi', 'OSC2 Shape')
ALG_BANK2 = ('OSC1 Balance', 'F1 Freq', 'F1 Resonance', 'F1 Type', 'OSC2 Balance', 'F2 Freq', 'F2 Resonance', 'F2 Type')
ALG_BANK3 = ('FEG1 Attack', 'FEG1 Decay', 'FEG1 Sustain', 'FEG1 Rel', 'FEG2 Attack', 'FEG2 Decay', 'FEG2 Sustain', 'FEG2 Rel')
ALG_BANK4 = ('F1 On/Off', 'F1 Freq < LFO', 'F1 Freq < Env', 'F1 Res < LFO', 'F2 On/Off', 'F2 Freq < LFO', 'F2 Freq < Env', 'F2 Res < LFO')
ALG_BANK5 = ('AEG1 Attack', 'AEG1 Decay', 'AEG1 Sustain', 'AEG1 Rel', 'AEG2 Attack', 'AEG2 Decay', 'AEG2 Sustain', 'AEG2 Rel')
ALG_BANK6 = ('AMP1 Level', 'AMP1 Pan', 'LFO1 Shape', 'LFO1 Speed', 'AMP2 Level', 'AMP2 Pan', 'LFO2 Shape', 'LFO2 Speed')
ALG_BANK7 = ('Volume', 'Noise On/Off', 'Noise Level', 'Noise Color', 'Unison On/Off', 'Unison Detune', 'Vib On/Off', 'Vib Amount')
ALG_BOB = ('F1 Freq', 'F1 Resonance', 'OSC1 Shape', 'OSC1 Octave', 'OSC2 Shape', 'OSC2 Octave', 'OSC2 Detune', 'Volume')
ALG_BANKS = (ALG_BANK1,
             ALG_BANK2,
             ALG_BANK3,
             ALG_BANK5,
             ALG_BANK6,
             ALG_BANK4,
             ALG_BANK7)
ALG_BOBS = (ALG_BOB,)
ALG_BNK_NAMES = ('Oscillators', 'Filters', 'Filter Envelopes', 'Volume Envelopes', 'Mix', 'Filter Modulation', 'Output')
ALG_SWITCH1 = ('OSC1 On/Off', 'F1 On/Off', 'Unison On/Off', 'Noise On/Off', 'OSC 2 On/Off', 'F2 On/Off', 'Vib On/Off', '')
ALG_SWITCHES = (ALG_SWITCH1,)

#Collision (Instrument)
COL_BANK1 = ('Mallet On/Off', 'Mallet Volume', 'Mallet Noise Amount', 'Mallet Stiffness', 'Mallet Noise Color', '', '', '')
COL_BANK2 = ('Noise Volume', 'Noise Filter Type', 'Noise Filter Freq', 'Noise Filter Q', 'Noise Attack', 'Noise Decay', 'Noise Sustain', 'Noise Release')
COL_BANK3 = ('Res 1 Decay', 'Res 1 Material', 'Res 1 Type', 'Res 1 Quality', 'Res 1 Tune', 'Res 1 Fine Tune', 'Res 1 Pitch Env.', 'Res 1 Pitch Env. Time')
COL_BANK4 = ('Res 1 Listening L', 'Res 1 Listening R', 'Res 1 Hit', 'Res 1 Brightness', 'Res 1 Inharmonics', 'Res 1 Radius', 'Res 1 Opening', 'Res 1 Ratio')
COL_BANK5 = ('Res 2 Decay', 'Res 2 Material', 'Res 2 Type', 'Res 2 Quality', 'Res 2 Tune', 'Res 2 Fine Tune', 'Res 2 Pitch Env.', 'Res 2 Pitch Env. Time')
COL_BANK6 = ('Res 2 Listening L', 'Res 2 Listening R', 'Res 2 Hit', 'Res 2 Brightness', 'Res 2 Inharmonics', 'Res 2 Radius', 'Res 2 Opening', 'Res 2 Ratio')
COL_BOB = ('Res 1 Brightness', 'Res 1 Type', 'Mallet Stiffness', 'Mallet Noise Amount', 'Res 1 Inharmonics', 'Res 1 Decay', 'Res 1 Tune', 'Volume')
COL_BANKS = (COL_BANK1,
             COL_BANK2,
             COL_BANK3,
             COL_BANK4,
             COL_BANK5,
             COL_BANK6)
COL_BOBS = (COL_BOB,)
COL_BNK_NAMES = ('Mallet', 'Noise', 'Resonator 1, Set A', 'Resonator 1, Set B', 'Resonator 2, Set A', 'Resonator 2, Set B')
COL_SWITCH1 = ('Mallet On/Off', 'Res 1 On/Off', 'LFO 1 On/Off', 'LFO 1 Sync', 'Noise On/Off', 'Res 2 On/Off', 'LFO 2 On/Off', 'LFO 2 Sync')
COL_SWITCHES = (COL_SWITCH1,)

# Electric (Instrument)
ELC_BANK1 = ('M Stiffness', 'M Force', 'Noise Pitch', 'Noise Decay', 'Noise Amount', 'F Tine Color', 'F Tine Decay', 'F Tine Vol')
ELC_BANK2 = ('F Tone Decay', 'F Tone Vol', 'F Release', 'Damp Tone', 'Damp Balance', 'Damp Amount', '', '')
ELC_BANK3 = ('P Symmetry', 'P Distance', 'P Amp In', 'P Amp Out', 'Pickup Model', '', '', '')
ELC_BANK4 = ('M Stiff < Vel', 'M Stiff < Key', 'M Force < Vel', 'M Force < Key', 'Noise < Key', 'F Tine < Key', 'P Amp < Key', '')
ELC_BANK5 = ('Volume', 'Voices', 'Semitone', 'Detune', 'KB Stretch', 'PB Range', '', '')
ELC_BOB = ('M Stiffness', 'M Force', 'Noise Amount', 'F Tine Vol', 'F Tone Vol', 'F Release', 'P Symmetry', 'Volume')
ELC_BANKS = (ELC_BANK1,
             ELC_BANK2,
             ELC_BANK3,
             ELC_BANK4,
             ELC_BANK5)
ELC_BOBS = (ELC_BOB,)
ELC_BNK_NAMES = ('Mallet and Tine', 'Tone and Damper', 'Pickup', 'Modulation', 'Global')

#InstrumentImpulse
IMP_BANK1 = ('1 Start', '1 Transpose', '1 Stretch Factor', '1 Saturator Drive', '1 Filter Freq', '1 Filter Res', '1 Pan', '1 Volume')
IMP_BANK2 = ('2 Start', '2 Transpose', '2 Stretch Factor', '2 Saturator Drive', '2 Filter Freq', '2 Filter Res', '2 Pan', '2 Volume')
IMP_BANK3 = ('3 Start', '3 Transpose', '3 Stretch Factor', '3 Saturator Drive', '3 Filter Freq', '3 Filter Res', '3 Pan', '3 Volume')
IMP_BANK4 = ('4 Start', '4 Transpose', '4 Stretch Factor', '4 Saturator Drive', '4 Filter Freq', '4 Filter Res', '4 Pan', '4 Volume')
IMP_BANK5 = ('5 Start', '5 Transpose', '5 Stretch Factor', '5 Saturator Drive', '5 Filter Freq', '5 Filter Res', '5 Pan', '5 Volume')
IMP_BANK6 = ('6 Start', '6 Transpose', '6 Stretch Factor', '6 Saturator Drive', '6 Filter Freq', '6 Filter Res', '6 Pan', '6 Volume')
IMP_BANK7 = ('7 Start', '7 Transpose', '7 Stretch Factor', '7 Saturator Drive', '7 Filter Freq', '7 Filter Res', '7 Pan', '7 Volume')
IMP_BANK8 = ('8 Start', '8 Transpose', '8 Stretch Factor', '8 Saturator Drive', '8 Filter Freq', '8 Filter Res', '8 Pan', '8 Volume')
IMP_BOB1 = ('Global Volume', 'Global Time', 'Global Transpose', '', '1 Transpose', '2 Transpose', '3 Transpose', '4 Transpose')
IMP_BOB2 = ('1 Transpose', '2 Transpose', '3 Transpose', '4 Transpose', '5 Transpose', '6 Transpose', '7 Transpose', '8 Transpose')
IMP_BOB3 = ('1 Start', '2 Start', '3 Start', '4 Start', '5 Start', '6 Start', '7 Start', '8 Start')
IMP_BANKS = (IMP_BANK1,
             IMP_BANK2,
             IMP_BANK3,
             IMP_BANK4,
             IMP_BANK5,
             IMP_BANK6,
             IMP_BANK7,
             IMP_BANK8)
IMP_BOBS = (IMP_BOB1, IMP_BOB2, IMP_BOB3,)
IMP_BNK_NAMES = ('Pad 1', 'Pad 2', 'Pad 3', 'Pad 4', 'Pad 5', 'Pad 6', 'Pad 7', 'Pad 8')
IMP_SWITCH1 = ('1 Stretch Mode', '2 Stretch Mode', '3 Stretch Mode', '4 Stretch Mode', '5 Stretch Mode', '6 Stretch Mode', '7 Stretch Mode', '8 Stretch Mode')
IMP_SWITCHES = (IMP_SWITCH1,)

#Operator
OPR_BANK1 = ('Ae Attack', 'Ae Decay', 'Ae Sustain', 'Ae Release', 'A Coarse', 'A Fine', 'Osc-A Lev < Vel', 'Osc-A Level')
OPR_BANK2 = ('Be Attack', 'Be Decay', 'Be Sustain', 'Be Release', 'B Coarse', 'B Fine', 'Osc-B Lev < Vel', 'Osc-B Level')
OPR_BANK3 = ('Ce Attack', 'Ce Decay', 'Ce Sustain', 'Ce Release', 'C Coarse', 'C Fine', 'Osc-C Lev < Vel', 'Osc-C Level')
OPR_BANK4 = ('De Attack', 'De Decay', 'De Sustain', 'De Release', 'D Coarse', 'D Fine', 'Osc-D Lev < Vel', 'Osc-D Level')
OPR_BANK5 = ('Le Attack', 'Le Decay', 'Le Sustain', 'Le Release', 'LFO Rate', 'LFO Amt', 'LFO Type', 'LFO R < K')
OPR_BANK6 = ('Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release', 'Filter Freq', 'Filter Res', 'Fe R < Vel', 'Fe Amount')
OPR_BANK7 = ('Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release', 'Pe Init', 'Glide Time', 'Pe Amount', 'Spread')
OPR_BANK8 = ('Time < Key', 'Panorama', 'Pan < Key', 'Pan < Rnd', 'Algorithm', 'Time', 'Tone', 'Volume')
OPR_BOB = ('Filter Freq', 'Filter Res', 'A Coarse', 'A Fine', 'B Coarse', 'B Fine', 'Osc-B Level', 'Volume')
OPR_BANKS = (OPR_BANK1,
             OPR_BANK2,
             OPR_BANK3,
             OPR_BANK4,
             OPR_BANK5,
             OPR_BANK6,
             OPR_BANK7,
             OPR_BANK8)
OPR_BOBS = (OPR_BOB,)
OPR_BNK_NAMES = ('Oscillator A', 'Oscillator B', 'Oscillator C', 'Oscillator D', 'LFO', 'Filter', 'Pitch Modulation', 'Routing')

#MultiSampler
SAM_BANK1 = ('Volume', 'Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'Vol < Vel', 'Ve R < Vel', 'Time')
SAM_BANK2 = ('Filter Type', 'Filter Morph', 'Filter Freq', 'Filter Res', 'Filt < Vel', 'Filt < Key', 'Fe < Env', 'Shaper Amt')
SAM_BANK3 = ('Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release', 'Fe End', 'Fe Mode', 'Fe Loop', 'Fe Retrig')
SAM_BANK4 = ('L 1 Wave', 'L 1 Sync', 'L 1 Sync Rate', 'L 1 Rate', 'Vol < LFO', 'Filt < LFO', 'Pan < LFO', 'Pitch < LFO')
SAM_BANK5 = ('L 2 Wave', 'L 2 Sync', 'L 2 Sync Rate', 'L 2 Rate', 'L 2 R < Key', 'L 2 St Mode', 'L 2 Spin', 'L 2 Phase')
SAM_BANK6 = ('L 3 Wave', 'L 3 Sync', 'L 3 Sync Rate', 'L 3 Rate', 'L 3 R < Key', 'L 3 St Mode', 'L 3 Spin', 'L 3 Phase')
SAM_BANK7 = ('O Mode', 'O Volume', 'O Coarse', 'O Fine', 'Oe Attack', 'Oe Decay', 'Oe Sustain', 'Oe Release')
SAM_BANK8 = ('Transpose', 'Spread', 'Pe < Env', 'Pe Attack', 'Pe Peak', 'Pe Decay', 'Pe Sustain', 'Pe Release')
SAM_BOB = ('Filter Freq', 'Filter Res', 'Fe < Env', 'Fe Decay', 'Ve Attack', 'Ve Release', 'Transpose', 'Volume')
SAM_BANKS = (SAM_BANK1,
             SAM_BANK2,
             SAM_BANK3,
             SAM_BANK4,
             SAM_BANK5,
             SAM_BANK6,
             SAM_BANK7,
             SAM_BANK8)
SAM_BOBS = (SAM_BOB,)
SAM_BNK_NAMES = ('Volume', 'Filter', 'Filter Envelope', 'LFO 1', 'LFO 2', 'LFO 3', 'Oscillator', 'Pitch')

#OriginalSimpler
SIM_BANK1 = ('Ve Attack', 'Ve Decay', 'Ve Sustain', 'Ve Release', 'S Start', 'S Loop Length', 'S Length', 'S Loop Fade')
SIM_BANK2 = ('Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release', 'Filter Freq', 'Filter Res', 'Filt < Vel', 'Fe < Env')
SIM_BANK3 = ('L Attack', 'L Rate', 'L R < Key', 'L Wave', 'Vol < LFO', 'Filt < LFO', 'Pitch < LFO', 'Pan < LFO')
SIM_BANK4 = ('Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release', 'Glide Time', 'Spread', 'Pan', 'Volume')
SIM_BOB = ('Filter Freq', 'Filter Res', 'S Start', 'S Length', 'Ve Attack', 'Ve Release', 'Transpose', 'Volume')
SIM_BANKS = (SIM_BANK1,
             SIM_BANK2,
             SIM_BANK3,
             SIM_BANK4)
SIM_BOBS = (SIM_BOB,)
SIM_BNK_NAMES = ('Amplitude', 'Filter', 'LFO', 'Pitch Modifiers')

#StringStudio
TNS_BANK1 = ('Excitator Type', 'String Decay', 'Str Inharmon', 'Str Damping', 'Exc ForceMassProt', 'Exc FricStiff', 'Exc Velocity', 'E Pos')
TNS_BANK2 = ('Damper On', 'Damper Mass', 'D Stiffness', 'D Velocity', 'Damp Pos', 'D Damping', 'D Pos < Vel', 'D Pos Abs')
TNS_BANK3 = ('Term On/Off', 'Term Mass', 'Term Fng Stiff', 'Term Fret Stiff', 'Pickup On/Off', 'Pickup Pos', 'T Mass < Vel', 'T Mass < Key')
TNS_BANK4 = ('Body On/Off', 'Body Type', 'Body Size', 'Body Decay', 'Body Low-Cut', 'Body High-Cut', 'Body Mix', 'Volume')
TNS_BANK5 = ('Vibrato On/Off', 'Vib Delay', 'Vib Fade-In', 'Vib Speed', 'Vib Amount', 'Vib < ModWh', 'Vib Error', 'Volume')
TNS_BANK6 = ('Filter On/Off', 'Filter Type', 'Filter Freq', 'Filter Reso', 'Freq < Env', 'Freq < LFO', 'Reso < Env', 'Reso < LFO')
TNS_BANK7 = ('FEG On/Off', 'FEG Attack', 'FEG Decay', 'FEG Sustain', 'FEG Release', 'LFO On/Off', 'LFO Shape', 'LFO Speed')
TNS_BANK8 = ('Unison On/Off', 'Uni Detune', 'Porta On/Off', 'Porta Time', 'Voices', 'Octave', 'Semitone', 'Volume')
TNS_BOB = ('Filter Freq', 'Filter Reso', 'Filter Type', 'Excitator Type', 'E Pos', 'String Decay', 'Str Damping', 'Volume')
TNS_BANKS = (TNS_BANK1,
             TNS_BANK2,
             TNS_BANK3,
             TNS_BANK4,
             TNS_BANK5,
             TNS_BANK6,
             TNS_BANK7,
             TNS_BANK8)
TNS_BOBS = (TNS_BOB,)
TNS_BNK_NAMES = ('Excitator and String', 'Damper', 'Termination and Pickup', 'Body', 'Vibrato', 'Filter', 'Envelope and LFO', 'Global')


DEVICE_DICT = {'AudioEffectGroupDevice': {'Banks': RCK_BANKS},
               'MidiEffectGroupDevice': {'Banks': RCK_BANKS},
               'InstrumentGroupDevice': {'Banks': RCK_BANKS},
               'DrumGroupDevice': {'Bamks': RCK_BANKS},

#              'InstrumentImpulse': IMP_BANKS,

               'Operator': {'Frequency': ('Filter Freq',),
                            'Resonance': ('Filter Res',),
                            'Banks': OPR_BANKS},
               'UltraAnalog': {'Frequency':   ('F1 Freq',),
                               'Resonance':   ('F1 Resonance',),
                               'Banks': ALG_BANKS},
               'OriginalSimpler': {'Frequency': ('Filter Freq',),
                                   'Resonance': ('Filter Res',),
                                   'Banks': SIM_BANKS},
               'MultiSampler': {'Frequency':   ('Filter Freq',),
                                'Resonance':   ('Filter Res',),
                                'Banks': SAM_BANKS},

#              'MidiArpeggiator': ARP_BANKS,
#              'LoungeLizard': ELC_BANKS,

               'StringStudio':  {'Frequency':   ('Filter Freq',),
                                'Resonance':   ('Filter Res',),
                                'Banks': TNS_BANKS},

#              'Collision': COL_BANKS,
#              'MidiChord': CRD_BANKS,
#              'MidiNoteLength': NTL_BANKS,
#              'MidiPitcher': PIT_BANKS,
#              'MidiRandom': RND_BANKS,
#              'MidiScale': SCL_BANKS,
#              'MidiVelocity': VEL_BANKS,

               'AutoFilter': {'Frequency': ('Frequency',),
                              'Resonance': ('Resonance',),
                              'Banks': AFL_BANKS},

#              'AutoPan': APN_BANKS,
#              'BeatRepeat': BRP_BANKS,

               'Chorus': {'Frequency': ('Delay 1 HiPass',),
                          'Feedback': ('Feedback',),
                          'TimeDelay': ('Delay 1 Time', 'Delay 2 Time'),
                          'DryWet': ('Dry/Wet',),
                          'DelayMode': ('Delay 2 Mode',),
                          'Banks': CHR_BANKS},

#              'Compressor2': CP3_BANKS,
#              'Corpus': CRP_BANKS,

               'Eq8': {'Frequency': ('3 Frequency A',), #( '%i Frequency A' % (index + 1) for index in range(8) ),
                       'Resonance': ('3 Resonance A',), #( '%i Resonance A' % (index + 1) for index in range(8) ),
                       'Gains': ( '%i Gain A' % (index + 1) for index in range(8) ),
                       'Cuts':  ( '%i Filter On A' % (index + 1) for index in range(8)),
                       'Banks': EQ8_BANKS},
               'FilterEQ3': {'Frequency': ('FreqHi',),
                             'Gains': ('GainLo', 'GainMid', 'GainHi'),
                             'Cuts':  ('LowOn', 'MidOn', 'HighOn'),
                             'Banks': EQ3_BANKS},

#              'Erosion': ERO_BANKS,

               'FilterDelay': {'Frequency': ('2 Filter Freq',), # L+R
                               'Resonance': ('Dry',),
                               'Gains': ( '%i Volume' % (index + 1) for index in range(3) ),
                               'Cuts': ( '%i Filter On' % (index + 1) for index in range(3) ),
                               'Banks': FLD_BANKS},

#              'Flanger': FLG_BANKS,
#              'FrequencyShifter': FRS_BANKS,

               'GrainDelay': {'Frequency': ('Frequency',),
                              'Resonance': ('DryWet',),
                              'Banks': GRD_BANKS},

               'Looper': {'Banks': LPR_BANKS},

#               'MultibandDynamics': MBD_BANKS,
#               'Overdrive': OVR_BANKS,
#               'Phaser': PHS_BANKS,
#               'Redux': RDX_BANKS,

               'Saturator': {'Banks': SAT_BANKS},
               'Resonator': {'Banks': RSN_BANKS},
               'CrossDelay':   {'Feedback': ('Feedback',),
                                'Resonance': ('Dry/Wet',),
                                'TimeDelay': ('L Time Delay', 'R Time Delay'),
                                'BeatDelay': ('L Beat Delay', 'R Beat Delay'),
                                'DryWet': ('Dry/Wet',)
                                'DelayMode': ('Delay Mode',),
                                'Banks': SMD_BANKS},

#              'StereoGain': UTL_BANKS,

               'Tube': {'Banks': DTB_BANKS},
               'Reverb': {'Resonance': ('Dry/Wet',),
                          'Banks': RVB_BANKS},

#              'Vinyl': VDS_BANKS,

               'Gate': {'Banks': GTE_BANKS},

               'PingPongDelay': {'Frequency': ('Filter Freq',),
                                 'FilterWidth': ('Filter Width',),
                                 'Feedback': ('Feedback',),
                                 'Resonance': ('Dry/Wet',),
                                 'Banks': PPG_BANKS},

#              'Vocoder': VOC_BANKS,
#              'Amp': AMP_BANKS,
#              'Cabinet': CAB_BANKS,

               'GlueCompressor': {'Banks': GLU_BANKS}
}

#             EQ Lo, EQ Mid, EQ Hi, Mid Freq, Freq, Reverb Amount, Reverb Decay, Rack Dry/Wet, Rack Vol
GRP1_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7', 'Macro 8')
GRP1_BANKS = (GRP1_BANK1,)
GRP1_MAP = {'Frequency': ('Macro 4',),
            'Gains': ('Macro 1', 'Macro 2', 'Macro 3'),
            'Banks': GRP1_BANKS}

#             Bass Gain, Mid Gain, Hi Gain, Mid Freq, Comp Gain/Attack, Comp Thresh, Comp Dry/Wet, Lim Gain/Sat Drive
GRP2_BANK1 = ('Macro 1', 'Macro 2', 'Macro 4', 'Macro 3', 'Macro 6', 'Macro 5', 'Macro 7', 'Macro 8')
GRP2_BANKS = (GRP2_BANK1,)
GRP2_MAP = {'Frequency': ('Macro 3',),
               'Gains': ('Macro 1', 'Macro 2', 'Macro 4'),
               'Banks': GRP2_BANKS}

GRP3_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 6', 'Macro 4', 'Macro 5', 'Macro 7', 'Macro 8')
GRP3_BANKS = (GRP3_BANK1,)
GRP3_MAP = {'Frequency': ('Macro 3',),
            'Gains': ('Macro 1', 'Macro 2', 'Macro 4'),
            'Banks': GRP3_BANKS}

#             Satur Drive, Sat Color, Sat Amount, Lim Gain, Comp SC Freq, Comp Thresh, Comp Gain, Comp Dry/Wet
GRP4_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 8', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7')
GRP4_BANKS = (GRP4_BANK1,)
GRP4_MAP = {'Frequency': ('Macro 4',),
            'Gains': ('Macro 3', 'Macro 8', 'Macro 6'),
            'DryWet': ('Macro 7',),
            'Banks': GRP4_BANKS}

RACK_DEVICE_DICT = {
    'Aggressive Dance Master': GRP2_MAP,
    'Boombox Drums': GRP2_MAP,
    'Bright & Edgy Master': GRP1_MAP,
    'Crushed Drums': GRP2_MAP,
    'DJ Master Channel': GRP1_MAP,
    'EQ & Cabinet Channel Strip': GRP2_MAP,
    'EQ & Compressor Master': GRP2_MAP,
    'EQ & Glue Master': GRP1_MAP,
    'Full Chain Master': GRP1_MAP,
    'Meaty Analogue Master': GRP4_MAP,
    'Multband & Limiter': GRP2_MAP,
    'MultiComp & EQ Three': GRP3_MAP,
    'Overdriven Drums': GRP1_MAP,
    'Punchy Dance Master': GRP2_MAP,
    'Sample Magic Beat Selection Processing Rack': GRP1_MAP
}

EXTENDED_DEVICE_DICT = {
    'AutoFilter':   {'Frequency':   ('Frequency',),
                     'Resonance':   ('Resonance',)},
    'Chorus':       {'Frequency':   ('Delay 1 HiPass',),
                    'Feedback':     ('Feedback',),
                    'TimeDelay':    ('Delay 1 Time', 'Delay 2 Time'),
                    'DryWet':       ('Dry/Wet',),
                    'DelayMode':    ('Delay 2 Mode',)},
    'CrossDelay':   {'Feedback':    ('Feedback',),
                     'Resonance':   ('Dry/Wet',),
                     'TimeDelay':   ('L Time Delay', 'R Time Delay',),
                     'BeatDelay':   ('L Beat Delay', 'R Beat Delay',),
                     'DryWet':      ('Dry/Wet',),
                     'DelayMode':   ('Delay Mode',)},
    'Eq8':          {'Frequency':   ( '%i Frequency A' % (index + 1) for index in range(8) ),
                     'Resonance':   ( '%i Resonance A' % (index + 1) for index in range(8) ),
                     'Gains':       ( '%i Gain A' % (index + 1) for index in range(8) ),
                     'Cuts':        ( '%i Filter On A' % (index + 1) for index in range(8)),
                     'SmartFreq':   ('3 Frequency A',),
                     'SmartRes':    ('3 Resonance A',)},
    'FilterEQ3':    {'Frequency':   ('FreqLo','FreqHi',),
                     'Gains':       ('GainLo', 'GainMid', 'GainHi'),
                     'Cuts':        ('LowOn', 'MidOn', 'HighOn'),
                     'SmartFreq':   ('FreqHi',)},
    'FilterDelay':  {'Frequency':   ( '%i Filter Freq' % (index + 1) for index in range(3) ),
                     'SmartFreq':   ('2 Filter Freq',),
                     'Resonance':   ('Dry',),
                     'Gains':       ( '%i Volume' % (index + 1) for index in range(3) ),
                     'Cuts':        ( '%i Filter On' % (index + 1) for index in range(3) )},
    'GrainDelay':    {'Frequency':  ('Frequency',),
                      'Resonance':  ('DryWet',)},
    'Operator':     {'Frequency':   ('Filter Freq',),
                     'Resonance':   ('Filter Res',)},
    'OriginalSimpler': {'Frequency': ('Filter Freq',),
                        'Resonance': ('Filter Res',)},
    'PingPongDelay':{'Frequency':   ('Filter Freq',),
                     'FilterWidth': ('Filter Width',),
                     'Feedback':    ('Feedback',),
                     'Resonance':   ('Dry/Wet',)},
    'MultiSampler': {'Frequency':   ('Filter Freq',),
                     'Resonance':   ('Filter Res',)},
    'Reverb':       {'Resonance':   ('Dry/Wet',)},
    'UltraAnalog':  {'Frequency':   ('F1 Freq',),
                     'Resonance':   ('F1 Resonance',)}
}

def print_device_list():
    return