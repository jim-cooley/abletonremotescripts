import Live
from FCB1010Component import FCB1010Component

from consts import *

class FCB1010MainController(FCB1010Component):
    __module__ = __name__
    __doc__ = "Main controller for FCB1010 remote control surface"
    __filter_funcs__ = ["update_display", "log"]

    def __init__(self, parent):
	FCB1010Component.realinit(self, parent)

    def selected_scene_idx(self):
	def tuple_idx(tuple, obj):
	    for i in xrange(0,len(tuple)):
		if (tuple[i] == obj):
		    return i
	return tuple_idx(self.parent.song().scenes, self.parent.song().view.selected_scene)

    def scene_up(self):
	idx = self.selected_scene_idx() - 1
	new_idx = min(len(self.parent.song().scenes), max(0, idx))
	self.parent.song().view.selected_scene = self.parent.song().scenes[new_idx]
	
    def scene_down(self):
	idx = self.selected_scene_idx() + 1
	new_idx = min(len(self.parent.song().scenes), max(0, idx))
	self.parent.song().view.selected_scene = self.parent.song().scenes[new_idx]

    def scene_fire(self):
	self.parent.song().view.selected_scene.fire()
	
    def receive_midi_note(self, channel, status, note_no, note_vel):
	pass

    def build_midi_map(self, script_handle, midi_map_handle):
	pass

    def disconnect(self):
	pass
    
