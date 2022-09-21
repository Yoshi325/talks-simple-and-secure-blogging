#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Yoshi325'
SITENAME = 'Simple and Secure Blogging'
SITEURL = ''

IGNORE_FILES = [
    'raw-html',
]

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 50

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'theme/'
# Theme specific
SIDEBAR_DIGEST = 'What a [Static] Site!'
SOCIAL = (
    ('github', 'https://github.com/Yoshi325'),
    ('twitter', 'https://twitter.com/charleslyost'),
)

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('About This Site', '/pages/about-this-site'),
    ('Synopsis', '/pages/synopsis'),
)
PAGE_EXCLUDES = [
    'extra',
]
ARTICLE_URL     = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_EXCLUDES = [
    'extra',
]
STATIC_PATHS = [
    'extra',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME' : {'path': 'CNAME'},
}
PLUGIN_PATHS = [
    f'{THEME}plugins/',
]
PLUGINS = []