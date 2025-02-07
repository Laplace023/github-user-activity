#!/usr/bin/env python3
#main code

from utilities.gitGet import gitGet
import utilities.config as config

import argparse
import os

authKey = config.password

pars = argparse.ArgumentParser()

pars.add_argument("userName", help="Github user name")
arg = pars.parse_args()
userName = arg.userName

if arg.userName:
    gitGet(userName, authKey)
else:
    pass