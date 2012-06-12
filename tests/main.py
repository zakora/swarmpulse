#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import tests.pixelmap as pm
import tests.hex as hx

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(pm.TestPixelMap))
    suite.addTest(unittest.makeSuite(hx.TestHex))
    unittest.TextTestRunner(verbosity=2).run(suite)
