import os, subprocess
import sys

if len(sys.argv) != 2:
	print("Usage: python3 try.py <UUID of the TM disk>")
	exit(1)

UUID = sys.argv[1]

def tryPass(pwd):

	command = 'diskutil coreStorage unlockVolume %s -passphrase %s' % (UUID,pwd)

	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, timeout=3, universal_newlines=True)
		#raise subprocess.CalledProcessError(0,None)
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
