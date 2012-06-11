#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import app.pixelmap as pm

class TestPixelMap(unittest.TestCase):
    
    def setUp(self):
        self.w = 100
        self.h = 50
        self.pm = pm.PixelMap(self.w, self.h)
        for i in range(self.w*self.h):
            self.pm[i] = i

    def test_get(self):
        self.assertEqual(self.pm.get(0,0), 0)
        self.assertEqual(self.pm.get(1,2), self.w*2+1)
        self.assertEqual(self.pm.get(10,10), 1010)
        self.assertRaises(IndexError, self.pm.get, -1)
        self.assertRaises(IndexError, self.pm.get, 10, -1)

    def test_set(self):
        self.assertRaises(IndexError, self.pm.set, -1, 1)
        self.assertRaises(IndexError, self.pm.set, 0, 10000, 1)

if __name__ == '__main__':
    unittest.main()
