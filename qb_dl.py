#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Download helper for qutebrowser, uses wget


__author__ = 'Michael Harig <floss@michaelharig.de>'
__version__ = '0.1'
__license__ = '''(c) 2022 MIT'''


##### TODO
# 
# - Debug: After downloading, qb prints: ": no such command
# - Test: What happens, when URL contains space(s)?
# - DONE Function, that gets the content of the clipboard, preferably platform independent
# - DONE Function, that spawns a wget -c, parameters: URL and filepath
# - What did I mean with this? Function, that combines an optional parameter to the qb download command, or the basename of the link, and the configured/current download directory to a target filepath
# - DONE Function, that executes the qb command
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
        qexec('message-info "%s"'%(err.decode(),))
    # TODO: progress bar?


def download():
    url = getClipboard()
    tn = url.split('/')[-1]
    if not tn:
        qexec('message-info "URL %s is not a filepath. %s"'%(url, tn))
        sys.exit()
    tp = Path(environ['QUTE_DOWNLOAD_DIR']).joinpath(tn)
    cmd = DLCMD.copy()
    # cmd.append(url.center(len(url)+2, '"'))     # quote
    cmd.append(url)
    cmd.append('-O')
    tp = str(tp)
    # tp = tp.center(len(tp)+2, '"')              # quote
    cmd.append(tp)
    qexec('message-info "Spawning command %s."'%(str(cmd),))
    spawnCmd(cmd)


if __name__ == '__main__':
    download()

