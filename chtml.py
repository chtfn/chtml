#!/usr/bin/env python

from html.parser import HTMLParser

# Define the parser for vanilla html
class html(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('({0}'.format(tag))
    def handle_endtag(self, tag):
        print(')')
    def handle_data(self, data):
        print(data)

vanilla = html()
vanilla.feed('<html><head><title>Test</title></head></html>')
