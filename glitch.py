#! usr/bin/python
# -*- coding: utf-8 -*-

"""
Enjoy your glitch life!!

Usage:
  glitch [-h] -i=<input> [-o=<output>] [-n=<times>]

Options:
  -h  show this
  -i=<input>  base `jpg` file
  -o=<output>  52 glitched files[default: ./glitched.jpg]
  -n=<times>  output files N times[default: (26+26+20)**2]
"""


import base64
import random
import string
import docopt


def fetchAlphanumeric():
    an = list(string.ascii_letters + string.digits)
    random.shuffle(an)
    return (bytes([ord(an[i])]) for i in range(len(an)))

def glitch(infile, outfile, times):
    fan = [fetchAlphanumeric() for i in range(4)]
    for i in range(times):
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
    glitch(args[0], args[1], args[2])

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    print(main(args["-i"], args["-o"], args["-n"]))
