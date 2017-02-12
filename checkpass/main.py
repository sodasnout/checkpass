# Copyright (c) 2017 Sodasnout

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# CheckPass main

from __future__ import print_function

import bz2
import os
import argparse

PASSWORD_FILES_DIR = os.path.join(os.path.dirname(__file__), 'known-passwords', 'sorted')

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
	VERSION = f.read().strip()

def map_to_filename(password):
	"""
	Returns the filename a password would fall under by its prefix
	"""
	filename = os.path.join(PASSWORD_FILES_DIR, password[0:2].lower() + '.txt.bz2')
	if os.path.exists(filename):
		return filename
	return os.path.join(PASSWORD_FILES_DIR, 'special-chars.txt.bz2')

def check_password(password, ignore_case=False, exact_match=False):
	filename = map_to_filename(password)
	with open(filename, mode='rb') as f:
		data = str(bz2.decompress(f.read()), encoding='utf-8')
		password_list = data.split('\r\n')

	if ignore_case:
		password = password.lower()
	if not exact_match:
		password_length = len(password)

	matches = []
	for pw in password_list:
		if ignore_case:
			value = pw.lower()
		else:
			value = pw

		if exact_match:
			if value == password and matches.count(pw) == 0:
				matches.append(pw)
		else:
			value_length = len(value)
			if value_length > password_length and value.find(password) == 0 and matches.count(pw) == 0:
				matches.append(pw)
	return matches

def non_unicode_print(*objects):
	"""
	Handles printing unicode strings if stdout isn't using utf-8
	"""
	encoded_objects = []
	for o in objects:
		encoded_objects.append(bytes(o, encoding='utf-8').decode(os.sys.stdout.encoding))
	print(*encoded_objects)


def parse_args():
	"""
	Handles argument parsing
	"""
	parser = argparse.ArgumentParser(prog='CheckPass', description='Utility for verifying if a password if potentially unique.')
	parser.add_argument('password', help='Password to check for.')
	parser.add_argument('-i', '--ignore-case', help='Ignore case.', action='store_true', dest='ignoreCasing')
	parser.add_argument('-e', '--exact', help='Checks only for exact matches (casing is not checked with -i flag on).', action='store_true', dest='exactMatch')
	parser.add_argument('-v', '--version', help='Displays version.', action='version', version='%(prog)s ' + VERSION)
	return parser.parse_args()

def main():
	"""
	Main script entry point
	"""
	args = parse_args()
	try:
		matches = check_password(args.password, args.ignoreCasing, args.exactMatch)
	except Exception as e:
		print('An error occured: ', e)
		os.sys.exit(1)

	if os.sys.stdout.encoding == 'utf-8':
		if isinstance(__builtins__, dict):
			print = __builtins__['print']
		else:
			print = __builtins__.print
	else:
		print = non_unicode_print

	matches_length = len(matches)
	if matches_length <= 0:
		print("No matches found for '%s'" % args.password)
	else:
		index = 1
		for m in matches:
			print('%d. %s' % (index, m))
			index += 1

		if matches_length == 1:
			matches_str = "\nThere is 1 match for '%s'" % args.password
		else:
			matches_str = "\nThere are %d matches for '%s'" % (matches_length, args.password)
		print(matches_str)

if __name__ == '__main__':
	main()
