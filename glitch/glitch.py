#! usr/bin/python
# -*- coding: utf-8 -*-

"""
Enjoy your glitch life!!

Usage:
  glitch [-h] -i=<input> [-o=<output>] [-n=<times>] [max] [intense]

Options:
  -h  show this
  -i=<input>  '*.jpg' file
  -o=<output>  '*.jpg' glitched file[default: ./glitched.jpg]
  -n=<times>  output files N times[default: 10]
  max  create max(62) files
  intense  intense glitch
"""


import base64
import random
import string
import docopt


def mostbytes(text, removeword=None):
    text = list(set(text))
    if removeword:
        if not isinstance(removeword, int):
            removeword = ord(removeword)
        text.remove(removeword)
    if len(text) <= 1: return bytes([ord(chr(text))])
    ruleout = [ord(w) for w in ['+', '=', '/', '\n']]
    most = max(text, key=text.index)
    if most in ruleout:
        mostbytes(text, most)
    return bytes([ord(chr(most))])

def fetchAlphanumeric():
    an = list(string.ascii_letters + string.digits)
    random.shuffle(an)
    return (bytes([ord(an[i])]) for i in range(len(an)))

def glitch(infile, outfile="glitched.jpg", times=10, max=False, intense=False):
    if max:
        times = len(string.ascii_letters + string.digits)
    with open(infile, 'rb') as f:
        graphictext = base64.encodestring(f.read())
    if intense:
        fan = [fetchAlphanumeric() for i in range(4)]
    else:
        fan = [fetchAlphanumeric() for i in range(2)]
        most = mostbytes(graphictext)
        most += mostbytes(graphictext, ord(most))
    for i in range(int(times)):
        gt = graphictext[:]
        if intense: most = next(fan[2]) + next(fan[3])
        glitched = base64.decodestring(gt.replace(most, next(fan[0])+next(fan[1])))
        with open(outfile.replace(".jpg","{0}.jpg".format(i)), "wb") as f:
            f.write(glitched)
    njo, litc = map(list, ("njo", "litc"))
    a = list(map(random.shuffle, (njo, litc)))
    del(a)
    return "E" + "".join(njo) + "y G" + "".join(litc) + "h."

def main(*args):
    return glitch(*args)

if __name__ == '__main__':
    args = docopt.docopt(__doc__, version=1.0)
    print(main(args["-i"], args["-o"], args["-n"], args["max"], args["intense"]))
