# Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_32_static/midi-remote-scripts/VCM600/__init__.py
from VCM600_2 import VCM600_2
from logly import *


def create_instance(c_instance):
    """ Creates and returns the ADA1 script """
    return VCM600_2(c_instance)
