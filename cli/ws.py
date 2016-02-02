#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import ssl

__author__ = 'cleytonpedroza'

from websocket import create_connection
import sys
from threading import Thread
import time
import json

URL_WS = "wss://p-websocket.socialbase.com.br/ws"

class ThConection(Thread):
    def __init__(self, _callback):
        Thread.__init__(self)
        self.callback = _callback
        self.ws = None
        self.loop = True

    def run(self):
        while self.loop:
            if self.ws:
                try:
                    result = self.ws.recv()
                    self.callback(result)
                    time.sleep(0.01)
                except Exception, e:
                    print "Exception:", sys.exc_info()[0], e
                    self.ws = None
            else:
                self.ws = None
                time.sleep(1.0)
                self.try_connection()

    def try_connection(self):
        try:
            self.ws = create_connection(URL_WS, sslopt={"cert_reqs": ssl.CERT_NONE})
            print '<+> ws connected'
            self.callback(json.dumps({"type": "chat",
                                      "payload": {"user_login": "system",
                                                  "message": "",
                                                  "command": "login"}}))
        except Exception, e:
            print "Exception:", sys.exc_info()[0], e
            print '<-> not ws connected'


class PyWebSocket:
    def __init__(self, _callback):
        self.callback = _callback

        self.thread_conection = ThConection(self.callback)
        self.thread_conection.start()

    def send(self, info_to_send):
        if self.thread_conection.ws:
            print 'info to send:', info_to_send[:120]
            self.thread_conection.ws.send(info_to_send)

    def close(self):
        self.thread_conection.loop = False
        self.send("close")

    def get_connection(self):
        if not self.thread_conection.ws:
            return False
        return True





