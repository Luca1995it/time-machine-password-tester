#!/usr/bin/env python3

import os, subprocess
import sys

def tryPass(pwd):

	command = 'diskutil coreStorage unlockVolume 8D9DB037-6993-48EA-A800-DBBA6220B928 -passphrase %s' % pwd

	try:
		output = subprocess.check_output(
			command, stderr=subprocess.STDOUT, shell=True, timeout=3,
			universal_newlines=True)

	except subprocess.CalledProcessError as exc:
		return False
	else:
		#out_stream.write("Output: \n{}\n".format(output))
		print("Password: %s" % pwd)
		return True


number = 0

while number <= 10000000:

	pwd = "%s%s" % ("AF",str(number))

	if tryPass(pwd):
		break
	if number % 1000 == 0:
		print("Tried %d psw" % number)
	number += 1
