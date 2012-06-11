#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pixelmap as pm

if __name__ == '__main__':
    pm_suite = unittest.TestLoader().loadTestsFromTestCase(pm.TestPixelMap)
    unittest.TextTestRunner(verbosity=2).run(pm_suite)
