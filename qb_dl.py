#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Download helper for qutebrowser, uses wget


__author__ = 'Michael Harig <floss@michaelharig.de>'
__version__ = '0.1'
__license__ = '''(c) 2022 AGPLv3'''


##### TODO
# 
# - Function, that gets the content of the clipboard, preferably platform independent
# - Function, that spawns a wget -c, parameters: URL and filepath
# - Function, that combines an optional parameter to the qb download command, or the basename of the link, and the configured/current download directory to a target filepath
# - Function, that executes the qb command
# - progress indicator


from tkinter import Tk
import subprocess as sp

DLCMD = ['wget', '-q', '-c']


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


def spawnDownload(_cmd, _url, _filepath):
    pid = sp.Popen(_cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = pid.communicate()

    if err.decode() != '':
        print('error:', err.decode())
    # TODO


def getTargetPath(_param, _outDir, _url):
    pass        # TODO


def download():
    pass        # TODO
