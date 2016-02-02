#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from ws import PyWebSocket
import os

class MyApp():
    ws = []

    def __init__(self):
        MyApp.ws.append(PyWebSocket(self.callback))
        
    def callback(self, info):
        print 'info:', info


if __name__ == '__main__':
    for i in range(200):
        app = MyApp()

    while 1:
        a = raw_input('>')
        if a.upper() in ['EXIT', 'QUIT', 'SAIR', 'END']:
            print 'bye'
            os._exit(0)
