"""
This script checks if the user has all the required packages for the tutorial
"""
from __future__ import print_function

required = ['telfit', 'numpy', 'scipy', 'matplotlib', 'astropy', 'IPython',
            'lockfile', 'pysynphot', 'fortranformat', 'cython', 'requests']
for package in required:
	try:
		exec('import {}'.format(package))
		print('Found package {}!'.format(package))
	except ImportError:
		print('\nYou need to install the package "{}"'.format(package))
		print('Run one of the following: ')
		print('\tpip install {}'.format(package))
		print('\tconda install {}\n'.format(package))