# Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_32_static/midi-remote-scripts/VCM600/MixerComponent.py
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
from .TrackEQComponent import TrackEQComponent
from .TrackFilterComponent import TrackFilterComponent

from logly import *
from utils import *


class SpecialMixerComponent(MixerComponentBase):

    def __init__(self, num_tracks, *a, **k):
        self._track_eqs = [ TrackEQComponent() for _ in xrange(num_tracks) ]
        self._track_filters = [ TrackFilterComponent() for _ in xrange(num_tracks) ]
        super(SpecialMixerComponent, self).__init__(num_tracks, *a, **k)
        map(self.register_components, self._track_eqs)
        map(self.register_components, self._track_filters)

    def track_eq(self, index):
        assert index in range(len(self._track_eqs))
        return self._track_eqs[index]

    def track_filter(self, index):
        assert index in range(len(self._track_filters))
        return self._track_filters[index]

    def _reassign_tracks(self):
        super(SpecialMixerComponent, self)._reassign_tracks()
        tracks = self.tracks_to_use()
        for index in range(len(self._channel_strips)):
            track_index = self._track_offset + index
            track = tracks[track_index] if len(tracks) > track_index else None
            if len(self._track_eqs) > index:
                self._track_eqs[index].set_track(track)
            if len(self._track_filters) > index:
                self._track_filters[index].set_track(track)
        return

    def on_selected_track_changed(self):
        logly_message("VCM: Mixer received selected track change.")
        selected_track = self.song().view.selected_track
        print_track_info(selected_track)
        MixerComponentBase.on_selected_track_changed(self)