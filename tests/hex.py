#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import app.hex as hx

class TestHex(unittest.TestCase):
    
    def setUp(self):
        self.hexone = hx.Hex(0)
        self.hextwo = hx.Hex(0, lambda x: sin(x))

    def test_is_pulsing(self):
        self.assertFalse(self.hexone.is_pulsing())
        self.assertTrue(self.hextwo.is_pulsing())

if __name__ == '__main__':
    unittest.main()
