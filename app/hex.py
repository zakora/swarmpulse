#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hex(object):
    """Hex is the basic unit of SwarmPulse.

    There is two kind of Hex:
    - the pulsing Hex which have a defined pulse function, they are able to
    generate a pulse, they are also affected by their neighbors.
    - the non-pulsing Hex that don't generate anything, they just have input
    from their neighbors.

    All the Hex share the same basic set of behoviour rules. From these rules
    will emerge a collective behaviour flow.

    """
    
    def __init__(self, idy, pulse_f=None):
        """Build a Hex given an id `idy` and a pulse function `pulse_f`.
        
        Arguments:
        - `idy`: an integer used to identify a Hex.
        - `pulse_f`: a pulse function.

        Attributes:
        - `_idy`: an integer used to identify a Hex.
        - `_pulse_f`: a pulse function.
        - `_pulse_state`: the state of the Hex, in [-1.0:1.0].
        - `_neigh`: the neighbor ids of the current Hex, a list of integers.
        - `_pixels`: a list of pixel (in 1D space of PixelMap) belonging to
        this Hex.
        """
        self._idy = idy
        self._pulse_f = pulse_f
        self._pulse_state = None
        self._neigh = None
        self._pixels = []

    def __repr__(self):
        """Representation of a Hex, returns its id and its state"""
        res = "[%d] " % self._idy
        if self._pulse_state:
            res += str(self._pulse_state)
        else:
            res += "-"
        return res
        
    def is_pulsing(self):
        """Returns True if the Hex is able to pulse, ie. has pulse function."""
        return self._pulse_f != None
