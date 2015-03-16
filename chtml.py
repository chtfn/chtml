#!/usr/bin/env python

from html.parser import HTMLParser

# Define the parser for vanilla html
class vanhtml(HTMLParser):
    def starttag(self, tag, attrs):
        pass
    def endtag(self, tag):
        pass
    def contents(self, data):
        pass
