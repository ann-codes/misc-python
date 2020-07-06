# Importing scripts

## can only import from the same directory and can only start with alpha
import import_me 

## can also import w/ an alias
import import_me as im

## can import specific function, seperated by commas
from import_me import add_two, num

## can import specific function and then give alias (csv is from standard lib)
from csv import reader as csvreader

## not recommended to import * because it imports all functions and can lead to naming/definition issues of where it originates from 
# from random import *

## there are sub modules from modules
import os.path

## use below to import the variable
print(import_me.num)

## can use functions from imported file
add_two = import_me.add_two

print(add_two(22))
print(im.add_two(33)) ## using alias

## using __main__ block
print(__name__) ## good practice to have executable with underscores like __main__
print(im.__name__)

print(im.__name__)
