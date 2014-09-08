#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from wizard import create

database_path = os.getcwd() + "/test.db"

if os.path.isfile(database_path):
	print('yes')
else:
	create()
