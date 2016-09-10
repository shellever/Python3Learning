#!/usr/bin/python
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
# from html.entities import name2codepoint


# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，
# 可以一部分一部分塞进去

class MyHTMLParser(HTMLParser):

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data.strip())

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
    <!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


'''
<html>

<head>
<head>

<body>

<!--  test html parser  -->

<p>
Some
<a>
html
<a>
HTML tutorial...
<br>
END
<p>

<body>
<html>
'''


