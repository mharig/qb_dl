#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Download helper for qutebrowser, uses wget


__author__ = 'Michael Harig <floss@michaelharig.de>'
__version__ = '0.1'
__license__ = '''(c) 2022 AGPLv3'''


##### TODO
# 
# - DONE Function, that gets the content of the clipboard, preferably platform independent
# - Function, that spawns a wget -c, parameters: URL and filepath
# - Function, that combines an optional parameter to the qb download command, or the basename of the link, and the configured/current download directory to a target filepath
# - Function, that executes the qb command
# - progress indicator


from tkinter import Tk      # needed for clipboard
import subprocess as sp
from os import environ
from pathlib import Path
import sys

DLCMD = ['wget', '-q', '-c']


def qexec(_cmd):
    with open(environ['QUTE_FIFO'], 'w') as f:
        f.write(_cmd)


def getClipboard():
    """ Returns the clipboard content using Tk.
    :returns: String with clipboard content
    """
    t = Tk()
    t.withdraw()
    result = t.clipboard_get()
    t.update()
    t.destroy()
    return result


def spawnCmd(_cmd):
    pid = sp.Popen(_cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = pid.communicate()

    if err.decode() != '':
        qexec(f'message-info "{err.decode()}"')
    else:
        qexec(f'message-info "File {_cmd[5]} downloaded."')
    # TODO: progress bar?


def download():
    url = getClipboard()
    tn = url.split('/')[-1]
    tp = Path(environ['QUTE_DOWNLOAD_DIR']).joinpath(tn)
    cmd = DLCMD.copy()
    cmd.append(url.center(len(url)+2, '"'))     # quote
    cmd.append('-O')
    cmd.append(tp.center(len(tp)+2, '"'))       # quote

    spawnCmd(cmd)


if __name__ == '__main__':
    download()

