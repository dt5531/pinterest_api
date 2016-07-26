#!/usr/bin/env python3

import sys
import glob
import importlib
import pip

PY_MAJOR, PY_MINOR = sys.version_info[ 0 : 2 ]
if not (PY_MAJOR == 3 and PY_MINOR >= 3):
    sys.exit('This Pinterest API require Python >= 3.3; '
            'your version of Python is ' + sys.version )

dependecies = ['requests']

for package in dependecies:
    try:
        importlib.import_module(package)
        print ("Already have package " + package)
    except ImportError:
        print ("Does not have package " + package + ". Installing...")
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

print ("Setup Complete!")
