#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Comunidad Python M\xe9xico'
SITENAME = u'Python M\xe9xico'
SITEURL = ''

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Python.org', 'http://python.org/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/pythonmexico'),
          ('Facebook', 'https://www.facebook.com/PythonMexico'),
          ('Google+', 'https://plus.google.com/communities/102212072697662445782'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/pelican-bootstrap3"
