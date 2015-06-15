#!/usr/bin/python2

from jinja2 import Environment, FileSystemLoader
import os
from route import route

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(THIS_DIR),trim_blocks=True)

SRX110 = route("10.1.3.254","root","password")

print "Content-type: text/html\r\n\r\n"
print j2_env.get_template('./html/index.tmpl').render(routes=SRX110.show())
