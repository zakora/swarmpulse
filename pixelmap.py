#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PixelMap(object):
    """Describes a PixelMap
    """
    
    def __init__(self, w, h, init_value = None):
        """Initialize a pixel map given its size.
        
        Arguments:
        - `w`: width of the map.
        - `h`: height of the map.
        - `init_value`: initial value for the map.
        """
        self._w = w
        self._h = h
        self._map = [None]*w*h
        self._n = w*h

    def set(self, v1, v2, v3=None):
        if v3 == None:
            # 1D space
            index = v1
            value = v2
            self._map[index] = value
        else:
            x, y = v1, v2
            value = v3
            self._map[self.get(x, y)] = value

    def get(self, v1, v2=None):
        """Get the value in a 1D or 2D space.
        
        Arguments:
        - `v1`: 1D position of the element in the map if v2==None, x position
        of the element in the map otherwise.
        - `v2`: if None we select an element in a 1D space, y position
        otherwise.
        """
        if v2 == None:
            # 1D get
            if v1 < 0 or v1 > self._n - 1:
                raise IndexError("Index out of the map.")
            return self._map[v1]
        else:
            # 2D get
            if v1 < 0 or v1 > self._w - 1 or v2 < 0 or v2 > self._h - 1:
                raise IndexError("Index out of the map.")
            return self._map[self._w*v2+v1]
            
