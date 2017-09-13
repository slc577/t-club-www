#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'MIT Transportation Club'
SITENAME = 'MIT Transportation Club'
SITEURL = ''

PATH = 'content'
IGNORE_FILES = ['activities.md']
THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']


CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['image', 'extra/custom.css', 'extra/htaccess']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/htaccess': {'path': '.htaccess'},
    'image/logo.ico': {'path': 'favicon.ico'}
    }

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

TWITTER_USERNAME = 'TClubMIT'
TWITTER_WIDGET_ID = '525779245268615168'

MENUITEMS = (
    #('Activities', '/activities'),
    ('Executive', '/executive'),
    ('Showcase', '/showcase'),
    )

# Blogroll
#LINKS = (
#    ('Pelican', 'http://getpelican.com/'),
#    ('Python.org', 'http://python.org/'),
#    ('Jinja2', 'http://jinja.pocoo.org/'),
#    ('You can modify those links in your config file', '#'),
#    )

# Social widget
#SOCIAL = (('twitter', 'https://twitter.com/TClubMIT'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
