#!/usr/bin/env python3
import sys

import http.server
from dateutil.relativedelta import *

import datetime
from http.server import HTTPServer
from os import path

class RequestHandle(http.server.BaseHTTPRequestHandler):
   def do_GET(self):
        newDate = datetime.datetime.now() + relativedelta(seconds=+suconds)
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        text = f'<html>\n<meta http-equiv=\'refresh\' content=\"1\" >\n<meta charset=\"utf-8\" />\n<h2>{newDate.year} {newDate.month} {newDate.day} {newDate.hour} {newDate.minute} {newDate.second}</h2>\n</html>'
        self.wfile.write(bytearray(text,"utf-8"))

suconds = int(open("confog.txt").read())
port = 123

server_address = ("localhost", port)
httpd = HTTPServer(server_address, RequestHandle)
httpd.serve_forever()
