#! usr/bin/python
# -*- coding: utf-8 -*-

"""
Enjoy your glitch life!!
Replace: 任意の箇所のバイト列を、同サイズの任意のバイト列に置き換える
Increase: 任意の箇所のバイト列を、それより大きなサイズの任意のバイト列に置き換える
Decrease: 任意の箇所のバイト列を、削除する
Swap: 任意の箇所のバイト列と他の任意の箇所のバイト列を入れ替える
http://ucnv.org/openspace2013/map.html

Usage:
    glitch [-h] -i=<input> [-o=<output>] [-n=<times>] [maximum] [hard] [-m=<mode>]

Options:
  -h  show this
  -i=<input>  '*.jpg' file
  -o=<output>  '*.jpg' glitched file[default: ./glitched.jpg]
  -n=<times>  output files N times[default: 10]
  maximum  create 62 files
  hard  hard glitch
  -m=<mode> glitch mode, r: replace,
                         i: increase,
                         d: decreace,
                         s: swap
                         [default: r]
"""


import base64
import random
import string
import docopt

class Glitch:
    def __init__(self):
        self.glitch_mode = {
            'r': self.replace,
            'i': self.increase,
            'd': self.decrease,
            's': self.swap
        }

    def glitch(self, infile, outfile='glitched.jpg', times=10, maximum=False, hard=False, mode='r'):
        setting, mode, times = self.prepare_glitchfile(infile, hard, mode, times, maximum)
        self.factory(outfile, setting, mode, times)
        return self.enjoyglitch()

    def enjoyglitch(self):
        njo, litc = map(list, ("njo", "litc"))
        a = list(map(random.shuffle, (njo, litc)))
        njo, litc = "".join(njo), "".join(litc)
        return "E" + njo + "y G" + litc + "h."
    
    def factory(self, outfile, setting, mode, times):
        for i in range(times):
            filename = outfile.replace(".jpg", "{0}_{1}.jpg".format(i, mode.__name__))
            with open(filename, "wb") as f:
                g = self.machine(setting, mode)
                f.write(g)

    def prepare_glitchfile(self, infile, hard, mode, times, maximum):
        mode = self.glitch_mode[mode]
        times = self.set_glitch_times(times, maximum)
        with open(infile, 'rb') as f:
            graphictext = base64.encodestring(f.read())

        if hard:
            fan = [self.fetchAlphanumeric() for i in range(4)]
            most = None
        else:
            fan = [self.fetchAlphanumeric() for i in range(2)]
            most = self.mostbytes(graphictext)
            most += self.mostbytes(graphictext, most)

        return ((graphictext, fan, most), mode, times)

    def machine(self, setting, mode):
        infile, fan, most = setting
        if most is None:
            most = next(fan[2]) + next(fan[3])
        return mode(infile, fan, most)

    def set_glitch_times(self, times, maximum):
        if maximum:
            return len(string.ascii_letters + string.digits)
        else:
            return int(times)

    def mostbytes(self, text, remove_key=None):
        if isinstance(remove_key, bytes):
            remove_key = ord(remove_key)
        text = list(text)
        ruleout = [ord(w) for w in ['+', '=', '/', '\n']]

        if remove_key:
            text.remove(remove_key)

        most = max(text, key=text.count)
        if most in ruleout:
            most = self.mostbytes(text, most)
        try:
            return bytes([ord(chr(most))])
        except TypeError as e:
            return most

    def fetchAlphanumeric(self):
        an = list(string.ascii_letters + string.digits)
        random.shuffle(an)
        return (bytes([ord(an[i])]) for i in range(len(an)))

    def replace(self, infile, fan, most):
        glitchfile = infile[:]
        return base64.decodestring(glitchfile.replace(most, next(fan[0])+next(fan[1])))

    def increase(self):
        return 'Not yet.'

    def decrease(self):
        return 'Not yet.'

    def swap(self, infile, outfile, hard):
        return 'Not yet.'


def main(*args):
    g = Glitch()
    return g.glitch(*args)

if __name__ == '__main__':
    args = docopt.docopt(__doc__, version=1.0)
    print(main(args["-i"], args["-o"], args["-n"], args["maximum"], args["hard"], args["-m"]))
