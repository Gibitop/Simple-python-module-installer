#!/usr/bin/python

#### Simple Python Module Installer ####

# MIT License

# Copyright (c) 2019 Ilia Nikishin

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


# Default install command
cmd = 'pip3 install' 


from importlib.util import find_spec
from contextlib import redirect_stdout
from os import listdir
from os.path import isfile
from subprocess import call, check_output
from pkg_resources import working_set
from sys import argv
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Installs python dependencies for all files in directory')
    parser.add_argument('-c', '--command', help='Override \'pip install\' command')
    parser.add_argument('-d', '--directory', help='Choose directory')
    args = parser.parse_args()


    if not args.command:
        global cmd
    else:
        cmd = args.command
        
    if args.directory:
        path = args.directory
    else:
        path = '.'


    libs = []
    dirlist = listdir(path)


    for name in dirlist:
        if name.endswith('.py') and isfile(name):
            for line in open(name).read().split('\n'):
                if line.replace(' ', '').startswith('from'):
                    lib = line.split('from ')[1].split(' ')[0]
                elif line.replace(' ', '').startswith('import '):
                    lib = line.split('import ')[1].split(' ')[0]
                else:
                    continue
                lib = lib.split('.')[0]
                if lib not in libs and lib + '.py' not in dirlist:
                    libs.append(lib)
                    if find_spec(lib) is None:
                        call(cmd.split(' ') + [lib])

if __name__ == "__main__":
    main()
