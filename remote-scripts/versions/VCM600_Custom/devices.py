
# eq device mappings
EQ_DEVICES = {
    'Eq8':
        {'Gains': [ '%i Gain A' % (index + 1) for index in range(8) ]},

        'FilterDelay': {'Gains': ['GainLo', 'GainMid', 'GainHi'],
                        'Cuts': ['LowOn', 'MidOn', 'HighOn']},

        'FilterEQ3': {'Gains': ['1 Volume', '2 Volume', '3 Volume'],
                        'Cuts': ['1 Filter On', '2 Filter On', '3 Filter On']}
}

# filter device mappings
FILTER_DEVICES = {
    'AutoFilter':   { 'Frequency': 'Frequency',
                      'Resonance': 'Resonance'},

    'Chorus':       {'Frequency': 'Feedback',
                     'Resonance': 'Dry/Wet'},

    'CrossDelay':   {'Frequency': 'Feedback',
                     'Resonance': 'Dry/Wet'},

    'FilterDelay':  {'Frequency': '2 Filter Freq',
                     'Resonance': 'Dry'},

    'Operator':     {'Frequency': 'Filter Freq',
                     'Resonance': 'Filter Res'},

    'OriginalSimpler': {'Frequency': 'Filter Freq',
                        'Resonance': 'Filter Res'},

    'PingPongDelay': {'Frequency': 'Feedback',
                      'Resonance': 'Dry/Wet'},

    'MultiSampler': {'Frequency': 'Filter Freq',
                     'Resonance': 'Filter Res'},

    'Reverb':       {'Frequency': 'DecayTime',
                     'Resonance': 'Dry/Wet'},

    'UltraAnalog':  {'Frequency': 'F1 Freq',
                     'Resonance': 'F1 Resonance'},

    'StringStudio': {'Frequency': 'Filter Freq',
                     'Resonance': 'Filter Reso'}
}
