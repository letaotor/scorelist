#! /usr/bin/env python

from html.parser import HTMLParser
import sys
import re

class MyHTMLParser(HTMLParser):
    def __init__(self, content=''):
        HTMLParser.__init__(self, strict=False)
        self.result = content
        return

    def handle_starttag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag == "tr":
            self.result = self.result + "\n"
        elif tag == "td":
            self.result = self.result + '\t'
        else:
            pass
        return

    def handle_data(self, data):
        #tt=re.sub(r"[[:alpha:]_][[:alpnum:]_]*[[:space:]]*\(.*\)", "", data)
        tt=re.sub(r"[a-zA-Z_][a-zA-Z0-9_]*\(.*\).*;", "", data)
        self.result = self.result + tt.strip()
        return

    def get_result(self):
        return self.result

o = False
if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], "<input file>", "[output file]")
elif len(sys.argv) >= 3:
    o = True
f = open(sys.argv[1], 'r')
data = f.read()
parser = MyHTMLParser()
parser.feed(data)
if o:
    output = open(sys.argv[2], 'w')
    output.write(parser.get_result())
else:
    print(parser.get_result())
