#!/usr/bin/env python
# -*- coding: utf-8 -*-
#test.py
#11/2015

from subprocess import Popen
from shlex import split as ssplit

def test():
    command = 'python alfie.py -i test/homo_y.fasta test/pan_y.fasta -g test/y.gtf -o tmp/'
    command = ssplit(command)
    a = Popen(command)
    a.wait()

test()
