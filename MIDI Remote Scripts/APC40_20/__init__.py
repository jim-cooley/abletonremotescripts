# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from APC40plus20 import APC40plus20 

def create_instance(c_instance):
    ' Creates and returns the APC40 script '
    return APC40plus20(c_instance)

# local variables:
# tab-width: 4
