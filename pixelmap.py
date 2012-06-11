#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PixelMap(object):
    """A PixelMap is  a rectangle made of many units called pixel.

    The aim of this class is to provide basic functionnality in order to make
    life easier.

    The map is implemented as a 1D list because of pointer problem in 2D list in
    python.
    We will notice that we speak of "1D-space" and "2D-space". In fact we make
    an equivalence between the 1D list stored in this class, and the 2D
    rectangular representation of the map.
    
    """
    
    def __init__(self, w, h, init_value = None):
        """Initialize a PixelMap given its size.
        
        Arguments:
        - `w`: width of the map.
        - `h`: height of the map.
        - `init_value`: initial value for the map.

        Attributes:
        - `_w`: width of the map.
        - `_h`: height of the map.
        - `_n`: the number of pixels.
        - `_map`: the map, as a 1D list.
        
        """
        self._w = w
        self._h = h
        self._n = w*h
        self._map = [init_value]*w*h

    def __getitem__(self, key):
        """Returns the value of `_map` at the 1D position `key`."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Sets the value `value` at the 1D position `key` in `_map`."""
        self.set(key, value)

    def __repr__(self):
        """Returns a 2D text representation of the map."""
        res = ""
        for y in range(self._h):
            for x in range(self._w):
                res += str(self.get(x, y)) + " "
            res += "\n"
        return res

    def set(self, v1, v2, v3=None):
        """Set the value in a 1D or 2D space. If v3 == None we are in a 1D
        space, otherwise we are in a 2D space.

        Arguments:
        - `v1`: index, absolute position in 1D space, x positino if in 2D space.
        - `v2`: value if in 1D space, y position if in 2D space.
        - `v3`: if None we are in a 1D space, if not None it's the value to set.
        """
        if v3 == None:
            # 1D space
            if self.is_in_map_1d(v1):
                index = v1
                value = v2
                self._map[index] = value
        else:
            # 2D space
            if self.is_in_map_2d(v1, v2):
                x, y = v1, v2
                value = v3
                self._map[self.get(x, y)] = value

    def get(self, v1, v2=None):
        """Returns the value of a given index in a 1D or 2D space.
        
        Arguments:
        - `v1`: 1D position of the element in the map if v2 == None, x position
        of the element in the map otherwise.
        - `v2`: if None we select an element in a 1D space, y position
        otherwise.
        """
        if v2 == None:
            # 1D space
            if self.is_in_map_1d(v1):
                return self._map[v1]
        else:
            # 2D space
            if self.is_in_map_2d(v1, v2):
                return self._map[self._w*v2+v1]

    def is_in_map_1d(self, index):
        """See if index is a correct position in 1D in the map.

        Returns True if index is inside the map.
        Raise IndexError otherwise.
        """
        if index >= 0 and index < self._n:
            return True
        else:
            raise IndexError("Index out of the map: "+str(index)+" not in "
                             +"[0:"+str(self._n-1)+"].")
            
    def is_in_map_2d(self, x, y):
        """See if index is a correct position in 2D in the map.

        Returns True if index is inside the map.
        Raise IndexError otherwise.
        """
        if x >= 0 and y >= 0 and x < self._w and y < self._h:
            return True
        else:
            raise IndexError("Index out of the map: "+str(x)+","+str(y)+
                             " not in [0:"+str(self._w-1)+"],"+
                             "[0:"+str(self._h-1)+"].")
