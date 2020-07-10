#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
from importlib import import_module
import sys
import os
import glob


if __name__ == '__main__':
    # This is run when you run this on the command line.

    # Get test modules to import.
    if len(sys.argv) > 1:
        modules = sys.argv[1:]
    else:
        modules = glob.glob(os.path.join(os.path.dirname(__file__), 'test/integration', '*_test.py'))
        print(modules)

    # Load each test module.
    test_results = []
    for module in modules:
        module_name = module[2:-3].replace('/', '.')
        print('Importing module: %s' % module_name)
        mod = import_module(module_name, '')
        print('Running module: %s' % module_name)
        tests = getattr(mod, 'tests')

        # Run each test class in the test module.
        for test_name, test_class in tests:
            print('Running test: %s' % test_name)
            result = False

            # Run the test class, taching all errors.
            try:
                result = test_class.run()
            except Exception as e:
                print(e)
                result = False

            if result:
                print('Test PASSED!')
            else:
                print('Test FAILED!')
            test_results.append((test_name, result))
    print("\n")

    # Print summary of results.
    for name, res in test_results:
        res_str = "PASSED" if res else "FAILED"
        print("%s: %s" % (name, res_str))
    print("P:F = %d:%d" % (len([test_name for test_name, result in test_results if result]),
                           len([test_name for test_name, result in test_results if not result])))
    print('yay!')
