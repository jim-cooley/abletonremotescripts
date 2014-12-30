#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/Launch_Control_XL/__init__.py
from VCM600_XL import VCM600_XL


def create_instance(c_instance):
    return VCM600_XL(c_instance)