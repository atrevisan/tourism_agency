# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# main.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_file = [(r'C:\Users\Allan\Google Drive\UTFPR\2014-2\SISDIST\TRABALHO5\TourismAgency\TourismAgencyClient\TourismAgencyClient\com\tourism\webservice\webservice_url.pkl',
				 r'com\tourism\webservice\webservice_url.pkl')]
	
options = {
	
    'build_exe': {
		'include_files': include_file,
		'namespace_packages': ['suds'],
        'includes': 'atexit'
    }	
}

executables = [
    Executable('main.py', base=base)
]

setup(name='Tourism agency client',
      version='0.1',
      description='Client side of a touristic agency sw',
      options=options,
      executables=executables
      )