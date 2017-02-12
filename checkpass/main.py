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

import bzip2
import os.path

def map_to_filename(password):
	"""
	Returns the filename a password would fall under by its prefix
	"""
	prefix = password[0:2]
	filename = os.path.join(PASSWORD_FILES_DIR, prefix.lower() + '.txt.bz2')
	if os.path.exists(filename):
		return filename
	return os.path.join(PASSWORD_FILES_DIR, 'special-chars.txt.bz2')


def main():
	"""
	Main script entry point
	"""



if __name__ == '__main__':
	main()
