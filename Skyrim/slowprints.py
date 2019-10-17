import time, sys, random
import os


#these functions print the strings letter by letter, gives better aesthetics

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def inputslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    return("")


def separate():
    for letter in "_______________________________________________________________________":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0025)
    print()


def ps(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
