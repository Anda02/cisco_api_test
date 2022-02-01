from distutils.core import setup
import py2exe
from getpass import getpass
from output import *
from netmiko import ConnectHandler

setup(console=['ap_login.py'],
options = {
              "py2exe":{
                  "packages": ["getpass","output","netmiko","_cffi_backend"]
                  }
              })