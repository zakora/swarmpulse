#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pixelmap as pm

class TestPixelMap(unittest.TestCase):
    
    def setUp(self):
        w = 100
        h = 50
        self.pm = pm.PixelMap(w, h)
        for i in range(w*h):
            self.pm.set(i, i) # TODO faire self.pm[index] = value

    def test_get(self):
        self.assertEqual(self.pm.get(0,0), 0)
        self.assertEqual(self.pm.get(10,10), 1010)
        self.assertRaises(IndexError, self.pm.get, -1)
        self.assertRaises(IndexError, self.pm.get, 10, -1)

if __name__ == '__main__':
    unittest.main()
