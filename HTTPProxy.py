#!/usr/bin/env python3
import sys

import http.server
from dateutil.relativedelta import *
import requests

from http.server import HTTPServer
from os import path

class RequestHandle(http.server.BaseHTTPRequestHandler):
   def do_CONNECT(self):
        print(self.headers)
        requests.get(f'https://{self.headers.get("Host")}'[:-4])
   def do_GET(self):
        requests.get(self.requestline)
        print(self.requestline)


suconds = int(open("confog.txt").read())
port = 32

server_address = ("127.0.0.1", port)
httpd = HTTPServer(server_address, RequestHandle)
httpd.serve_forever()