# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from _Framework.SessionComponent import SessionComponent 
class APCSessionComponent(SessionComponent):
    " Special SessionComponent for the APC controllers' combination mode "
    __module__ = __name__

    def __init__(self, num_tracks, num_scenes):
        SessionComponent.__init__(self, num_tracks, num_scenes)


    def link_with_track_offset(self, track_offset):
        assert (track_offset >= 0)
        if self._is_linked():
            self._unlink()
        self._change_offsets(track_offset, 0)
        self._link()


# local variables:
# tab-width: 4
