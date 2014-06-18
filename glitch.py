#! usr/bin/python
# -*- coding: utf-8 -*-

"""
Enjoy your glitch life!!

Usage:
  glitch [-h] -i=<input> [-o=<output>] [-n=<times>] [max]

Options:
  -h  show this
  -i=<input>  '*.jpg' file
  -o=<output>  '*.jpg' glitched file[default: ./glitched.jpg]
  -n=<times>  output files N times[default: 10]
  max  create max(62) files
"""


import base64
import random
import string
import docopt


def fetchAlphanumeric():
    an = list(string.ascii_letters + string.digits)
    random.shuffle(an)
    return (bytes([ord(an[i])]) for i in range(len(an)))

def glitch(infile, outfile="glitched.jpg", times=10, max=False):
    if max:
        times = len(string.ascii_letters + string.digits)
    fan = [fetchAlphanumeric() for i in range(4)]
    for i in range(int(times)):
        graphictext = base64.encodestring(open(infile, "rb").read())
        glitched = base64.decodestring(graphictext.replace(
                                                           next(fan[0])+next(fan[1]),
                                                           next(fan[2])+next(fan[3])
                                                           ))
        open(outfile.replace(".jpg","{0}.jpg".format(i)), "wb").write(glitched)
    njo, litc = map(list, ("njo", "litc"))
    a = list(map(random.shuffle, (njo, litc)))
    del(a)
    return "E" + "".join(njo) + "y G" + "".join(litc) + "h."

def main(*args):
    return glitch(*args)

if __name__ == '__main__':
    args = docopt.docopt(__doc__, version=1.0)
    print(main(args["-i"], args["-o"], args["-n"], args["max"]))
