
import Live
from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
#from consts import * #see below (not used)
#MANUFACTURER_ID = 71
#ABLETON_MODE = 65
#NOTE_MODE = 65 #67 = APC20 Note Mode; 65 = APC40 Ableton Mode 1

class ShiftableSelectorComponent(ModeSelectorComponent):
    __doc__ = ' SelectorComponent that assigns buttons to functions based on the shift button '
    #def __init__(self, select_buttons, master_button, arm_buttons, matrix, session, zooming, mixer, transport, slider_modes, mode_callback):
    def __init__(self, parent, select_buttons, master_button, arm_buttons, matrix, session, zooming, mixer, slider_modes, mode_callback):
        if not len(select_buttons) == 8:
            raise AssertionError
        if not len(arm_buttons) == 8:
            raise AssertionError
        ModeSelectorComponent.__init__(self)
        self._toggle_pressed = False
        self._note_mode_active = False
        self._invert_assignment = False
        self._select_buttons = select_buttons
        self._master_button = master_button
        self._slider_modes = slider_modes
        self._arm_buttons = arm_buttons
        #self._transport = transport
        self._session = session
        self._zooming = zooming
        self._matrix = matrix
        self._mixer = mixer
        self._mode_callback = mode_callback
        self._master_button.add_value_listener(self._master_value)
        self._parent = parent #use this to call methods of parent class (APC40plus20)


    def disconnect(self):
        ModeSelectorComponent.disconnect(self)
        self._master_button.remove_value_listener(self._master_value)
        self._select_buttons = None
        self._master_button = None
        self._slider_modes = None
        self._arm_buttons = None
        #self._transport = None
        self._session = None
        self._zooming = None
        self._matrix = None
        self._mixer = None
        self._mode_callback = None
        self._parent = None #added
        return None

    def set_mode_toggle(self, button):
        ModeSelectorComponent.set_mode_toggle(self, button) #called from APC20: self._shift_modes.set_mode_toggle(self._shift_button)
        self.set_mode(0)

    def invert_assignment(self):
        self._invert_assignment = True
        self._recalculate_mode()

    def number_of_modes(self):
        return 2

    def update(self):
        if self.is_enabled():
            if (self._mode_index == 0): # Non-Shifted Mode
                #for index in range(len(self._select_buttons)):
                    #strip = self._mixer.channel_strip(index)
                    #strip.set_select_button(None)              
                self._mixer.master_strip().set_select_button(None)
                #self._transport.set_play_button(self._select_buttons[0])
                #self._transport.set_stop_button(self._select_buttons[1])
                #self._transport.set_record_button(self._select_buttons[2])
                #self._transport.set_overdub_button(self._select_buttons[3])
                #self._session.set_track_bank_buttons(self._select_buttons[4], self._select_buttons[5])
                #self._session.set_scene_bank_buttons(self._select_buttons[6], self._select_buttons[7])
                #self._zooming.set_nav_buttons(self._select_buttons[6], self._select_buttons[7], self._select_buttons[4], self._select_buttons[5])                
                self._on_note_mode_changed()
            elif (self._mode_index == 1): # Shifted Mode
                #self._transport.set_play_button(None)
                #self._transport.set_stop_button(None)
                #self._transport.set_record_button(None)
                #self._transport.set_overdub_button(None)
                #self._session.set_track_bank_buttons(None, None)
                #self._session.set_scene_bank_buttons(None, None)
                #self._zooming.set_nav_buttons(None, None, None, None)
                #for index in range(len(self._select_buttons)):
                    #strip = self._mixer.channel_strip(index)
                    #strip.set_select_button(self._select_buttons[index])
                self._mixer.master_strip().set_select_button(self._master_button)
            else :
                assert False
            if self._mode_index == int(self._invert_assignment):
                self._slider_modes.set_mode_buttons(None)
                for index in range(len(self._arm_buttons)): #was: for index in range(len(self._select_buttons)):
                    self._mixer.channel_strip(index).set_arm_button(self._arm_buttons[index])
            else:
                for index in range(len(self._arm_buttons)): #was: for index in range(len(self._select_buttons)):
                    self._mixer.channel_strip(index).set_arm_button(None)
                self._slider_modes.set_mode_buttons(self._arm_buttons)      
        return None

    def _toggle_value(self, value): #"toggle" is shift button
        if not self._mode_toggle != None:
            raise AssertionError
        if not value in range(128):
            raise AssertionError
        self._toggle_pressed = value > 0
        self._recalculate_mode()
        self._parent._encoder_modes.update() #added to update track control encoders on shift
        return None

    def _recalculate_mode(self): #called if toggle (i.e. shift) is pressed
        self.set_mode((int(self._toggle_pressed) + int(self._invert_assignment)) % self.number_of_modes())

    def _master_value(self, value): #this is the master_button value_listener, i.e. called when the master_button is pressed
        if not self._master_button != None:
            raise AssertionError
        if not value in range(128):
            raise AssertionError
        if self.is_enabled() and self._invert_assignment == self._toggle_pressed:
            if not self._master_button.is_momentary() or value > 0: #if the master button is pressed:
                #for button in self._select_buttons: #turn off track select buttons (only needed for APC20)
                    #button.turn_off()
                self._matrix.reset() #turn off the clip launch grid LEDs
                #mode_byte = NOTE_MODE #= 67 for APC20 Note Mode, send as part of sysex string to enable Note Mode
                if self._note_mode_active: #if note mode is already on, turn it off:
                    #mode_byte = ABLETON_MODE #= 65 for APC40 Ableton Mode 1
                    for scene_index in range(5):
                        scene = self._session.scene(scene_index)
                        for track_index in range(8):
                            clip_slot = scene.clip_slot(track_index)
                            button = self._matrix.get_button(track_index, scene_index)
                            clip_slot.set_launch_button(button)
                            button.set_enabled(True)
                            button.turn_off()
                    self._rebuild_callback()
                #self._mode_callback(mode_byte) #send sysex to set Mode (NOTE_MODE or ABLETON_MODE)
                self._note_mode_active = not self._note_mode_active
                self._zooming.set_ignore_buttons(self._note_mode_active) #turn off matrix, scene launch, and clip stop buttons when in Note Mode
                #self._transport.update() #only needed for APC20
                self._on_note_mode_changed()
        return None

    def _on_note_mode_changed(self):
        if not self._master_button != None:
            raise AssertionError
        if self.is_enabled() and self._invert_assignment == self._toggle_pressed:
            if self._note_mode_active:
                self._master_button.turn_on()
                for scene_index in range(5):
                    #TODO: re-map scene_launch buttons to note velocity...
                    scene = self._session.scene(scene_index)
                    for track_index in range(8):
                        clip_slot = scene.clip_slot(track_index)
                        button = self._matrix.get_button(track_index, scene_index)
                        clip_slot.set_launch_button(None)                        
                        button.set_enabled(False)
                        button.set_channel(9) #remap all Note Mode notes to channel 10
                        if track_index < 4:
                            button.set_identifier(52 - (4 * scene_index) + track_index) #top row of left group (first 4 columns) notes 52 to 55
                            if (track_index % 2 == 0 and scene_index % 2 != 0) or (track_index % 2 != 0 and scene_index % 2 == 0):
                                button.send_value(1) #0=off, 1=green, 2=green blink, 3=red, 4=red blink, 5=yellow, 6=yellow blink, 7-127=green
                            else:
                                button.send_value(5)
                        else:
                            button.set_identifier(72 - (4 * scene_index) + (track_index -4)) #top row of right group (next 4 columns) notes 72 to 75
                            if (track_index % 2 == 0 and scene_index % 2 != 0) or (track_index % 2 != 0 and scene_index % 2 == 0):
                                button.send_value(1) #0=off, 1=green, 2=green blink, 3=red, 4=red blink, 5=yellow, 6=yellow blink, 7-127=green
                            else:
                                button.send_value(3)
                self._rebuild_callback()
            else:
                self._master_button.turn_off()
        return None

        