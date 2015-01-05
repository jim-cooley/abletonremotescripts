import Live

RCK_BANK = ('Macro 1', 'Macro 2')

IMP_BANK = ('Global Time', 'Global Transpose')
OPR_BANK = ('Filter Freq', 'Volume')
SIM_BANK = ('Filter Freq', 'Volume')
SAM_BANK = ('Filter Freq', 'O Volume')

ARP_BANK = ('Synced Rate', 'Gate')
CRD_BANK = ('Shift1', 'Shift2')
NTL_BANK = ('Synced Length', 'Gate')
PIT_BANK = ('Pitch', 'Range')
RND_BANK = ('Chance', 'Choices')
SCL_BANK = ('Base', 'Transpose')
VEL_BANK = ('Out Hi', 'Out Low')

AFL_BANK = ('Frequency', 'LFO Amount')
APN_BANK = ('Amount', 'Frequency')
BRP_BANK = ('Chance', 'Interval')
CHR_BANK = ('Dry/Wet', 'LFO Amount')
CP1_BANK = ('Threshold', 'Ratio')
CP2_BANK = ('Threshold', 'Ratio')
DTB_BANK = ('Drive', 'Tone')
EQ8_BANK = ('1 Frequency A', '1 Gain A')
EQ3_BANK = ('GainMid', 'GainHi')
ERO_BANK = ('Frequency', 'Amount')
FLD_BANK = ('Dry', '2 EQ Freq')
FLG_BANK = ('Dry/Wet', 'Feedback')
GRD_BANK = ('DryWet', 'Frequency')
PHS_BANK = ('Dry/Wet', 'Frequency')
RDX_BANK = ('Bit Depth', 'Sample Hard')
SAT_BANK = ('Dry/Wet', 'Drive')
RSN_BANK = ('Dry/Wet', 'Frequency')
SMD_BANK = ('Dry/Wet', 'Feedback')
UTL_BANK = ('Gain', 'Panorama')
RVB_BANK = ('Dry/Wet', 'DecayTime')
VDS_BANK = ('Tracing Freq.', 'Crackle Volume')
GTE_BANK = ('Threshold', 'Floor')
PPG_BANK = ('Dry/Wet', 'Feedback')

DEVICE_DICT = {'AudioEffectGroupDevice': RCK_BANK,
	       'Midieffectgroupdevice':  RCK_BANK,
	       'InstrumentGroupDevice':  RCK_BANK,
	       'InstrumentImpulse':      IMP_BANK,
	       'Operator':               OPR_BANK,
	       'OriginalSimpler':        SIM_BANK,
	       'MultiSampler':           SAM_BANK,
	       'MidiArpeggiator':        ARP_BANK,
	       'MidiChord':              CRD_BANK,
	       'MidiNoteLength':         NTL_BANK,
	       'MidiPitcher':            PIT_BANK,
	       'MidiRandom':             RND_BANK,
	       'MidiScale':              SCL_BANK,
	       'MidiVelocity':           VEL_BANK,
	       'AutoFilter':             AFL_BANK,
	       'AutoPan':                APN_BANK,
	       'BeatRepeat':             BRP_BANK,
	       'Chorus':                 CHR_BANK,
	       'Compressor':             CP1_BANK,
	       'Compressor2':            CP2_BANK,
	       'Tube':                   DTB_BANK,
	       'Eq8':                    EQ8_BANK,
	       'FilterEQ3':              EQ3_BANK,
	       'Erosion':                ERO_BANK,
	       'FilterDelay':            FLD_BANK,
	       'Flanger':                FLG_BANK,
	       'GrainDelay':             GRD_BANK,
	       'Phaser':                 PHS_BANK,
	       'Redux':                  RDX_BANK,
	       'Saturator':              SAT_BANK,
	       'Resonator':              RSN_BANK,
	       'CrossDelay':             SMD_BANK,
	       'StereoGain':             UTL_BANK,
	       'Vinyl':                  VDS_BANK,
	       'Gate':                   GTE_BANK,
	       'PingPongDelay':          PPG_BANK,
	       'Reverb':                 RVB_BANK}

DRYWET_DICT = {'Chorus':        'Dry/Wet',
	       'BeatRepeat':    'Volume',
	       'Tube':          'Dry/Wet',
	       'FilterDelay':   'Dry',
	       'Saturator':     'Dry/Wet',
	       'CrossDelay':    'Dry/Wet',
	       'GrainDelay':    'DryWet',
	       'Flanger':       'Dry/Wet',
	       'Resonator':     'Dry/Wet',
	       'Phaser':        'Dry/Wet',
	       'Reverb':        'Dry/Wet',
	       'PingPongDelay': 'Dry/Wet'}
