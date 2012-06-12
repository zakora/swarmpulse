#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import tests.pixelmap as pm
import tests.hex as hx

if __name__ == '__main__':
    # PixelMap
    pm_suite = unittest.TestLoader().loadTestsFromTestCase(pm.TestPixelMap)
    unittest.TextTestRunner(verbosity=2).run(pm_suite)
    # Hex
    hex_suite = unittest.TestLoader().loadTestsFromTestCase(hx.TestHex)
    unittest.TextTestRunner(verbosity=2).run(hex_suite)
