# CheckPass Utility #
CheckPass is an utility you can use for verifying whether your password is potentially unique. It checks against the files
from the large known-passwords repository located at [https://github.com/nrakochy/known-passwords](https://github.com/nrakochy/known-passwords).

The password files have been compressed using bzip2 to save disk space.

Python 2.7.x or Python 3.x are required and optionally [Pip](https://wiki.python.org/moin/CheeseShopTutorial#Installing_Distributions).

## Installing with Pip ##

Open a command prompt and execute the command (Administrator privileges may be required):

`python -m pip install git+git://github.com/sodasnout/checkpass`

To uninstall with Pip (Administrator privileges may be required):

`python -m pip uninstall checkpass`


## Usage ##

```
checkpass [-h] [-i] [-e] password

positional arguments:
  password           Password to check for.

optional arguments:
  -h, --help         show this help message and exit
  -i, --ignore-case  Ignore case.
  -e, --exact        Checks only for exact matches (case is not checked with -i flag on)
```
