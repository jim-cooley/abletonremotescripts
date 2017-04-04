# http://remotescripts.blogspot.com
# This is a stripped-down script, which uses the Framework classes to assign MIDI notes to play, stop and record.

from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework
from _Framework.TransportComponent import TransportComponent # Class encapsulating all functions in Live's transport section
from _Framework.ButtonElement import ButtonElement # Class representing a button a the controller

class Transport(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        transport = TransportComponent() #Instantiate a Transport Component
        transport.set_play_button(ButtonElement(True, 0, 0, 61)) #ButtonElement(is_momentary, msg_type, channel, identifier)
        transport.set_stop_button(ButtonElement(True, 0, 0, 63))
        transport.set_record_button(ButtonElement(True, 0, 0, 66))
