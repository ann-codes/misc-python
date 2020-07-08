# Importing from the Standard Library (modules) https://docs.python.org/3/library/

import math
import random

print(math.factorial(4))
print(math.exp(3)) ## power of 3

rand = int(random.random() * 10) + 1
print(rand)

"""
MORE MODULES
csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
"""

########################################################

# Third party libraries can be installed using PIP
"""
// in command line: 

pip install package_name

// ie a time zone package

pip install pytz

// then import the module in script
"""

from datetime import datetime
import pytz

print(datetime.now(tz=pytz.utc))

# Python uses requirements.txt to manage dependencies
"""
// looks something like below

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

// you can use pip to install all the dependancies in CLI

pip install -r requirements.txt

// Useful Third-Party Packages

IPython - A better interactive Python interpreter***
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask - a lightweight framework for making web applications and APIs.
Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest - extends Python's builtin assertions and unittest module.
PyYAML - For reading and writing YAML files.
NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
ggplot - Another 2D plotting library, based on R's ggplot2 library.
Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet - A cross-platform application framework intended for game development.
Pygame - A set of Python modules designed for writing games.
pytz - World Timezone Definitions for Python
"""