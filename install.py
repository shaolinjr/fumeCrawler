#!/usr/bin/env python

# Nosso script ira instalar os modulos basicos para rodar o FumeCrawler
# Our script will install the basic modules to run FumeCrawler

import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


python_v = sys.version_info

if python_v[0] < 3:
    print(bcolors.FAIL + "You have to use Python v3.x")
    print(bcolors.WARNING+ "[Try]: If you have Python 3 installed, try to call :python3 install.py")
    print(bcolors.WARNING+ "Also make sure that your pip version is set to Python 3.x as well. You can call pip3")
    exit()

print(bcolors.OKGREEN+ "Installing the modules to run FumeCrawler"+bcolors.WARNING)
# Get Selenium (Browser module to access the portal)
os.system('pip3 install selenium')
# Get Clint (Change the colors os commands in command line)
os.system('pip3 install clint')
print(bcolors.OKGREEN+ "We will need your password below to move the PhantomJS module to /usr/local/bin\n"+bcolors.ENDC)
# Get PhanomJS (Headless browser to make selenium work)
os.system('sudo cp phantomjs /usr/local/bin')



