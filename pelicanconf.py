#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime
import pelican

# If `DEVMODE = True`, show a red warning banner at the top
DEVMODE = False   # pelicanconf-dev.py will override this

# By default, use agressive caching.
# The Makefile ensures we use `--ignore-cache` for production builds.
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CONTENT_CACHING_LAYER = 'generator'  # This causes an empty news page
WITH_FUTURE_DATES = False

ANALYTICS = ()   # pelicanconf-live.py will override this

AUTHOR = u'Thomas Barclay'
SITENAME = "TESS"
BANNER_SUBTITLE = "Community Science Center"
SITEURL = "https://tessgi.gsfc.nasa.gov"
SITELOGO = 'images/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = False

BANNER = "images/tess-banner.jpg"
HIDE_SITENAME = False

IGNORE_FILES = [
    "README.md",
]

# Enable RSS feeds
# FEED_DOMAIN = "https://keplerscience.arc.nasa.gov"
FEED_DOMAIN = ""
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# We don't need per-author or per-category or per-translation feeds
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_BREADCRUMBS = False

HIDE_SIDEBAR = True

if pelican.__version__ >= '3.7.0':
    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.toc': {},
        },
    }
else:
    MD_EXTENSIONS = (['toc'])


# Which static data dirs should be uploaded as part of the website?
STATIC_PATHS = (['images', 'data'])

# Directories that contain html files we want to exclude
# because they are sub-pages included through rst includes
PAGE_EXCLUDES = ['pages/k2-observing/approved-programs']

# The fancy table of contents sidebar requires a plugin
PLUGIN_PATHS = [os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "plugins")]
PLUGINS = ['extract_toc']

# Defines the menu items in the top bar
MENUITEMS = (
        ('News', 'archives.html'),
        ('Mission', (
            ('Objectives', 'objectives.html'),
            ('Telescope', 'the-tess-space-telescope.html'),
            ('Operations', 'operations.html'),
            ('Science', 'primary-science.html'),
            ('Publications', 'publications.html'),
            # ('Conferences', 'conferences.html'),
            # ('Users Panel', 'users-panel.html'),
            )
         ),
        ('Using TESS', (
            ('Guest Investigator Program', 'proposing-targets.html'),
            ('Status', 'status.html'),
            ('Technical details', 'observing-technical.html'),
            # ('Campaign fields', 'k2-fields.html'),
            # ('Targets &amp; programs', 'k2-approved-programs.html'),
            # ('Data release notes', 'k2-data-release-notes.html'),
            ('Proposal tools', 'proposal-tools.html'),
            ('Discretionary targets', 'ddt.html'),
            ('FAQ', 'faq.html'),
            # ('C9 Microlensing experiment', 'k2-c9.html'),
            # ('C16 Supernova experiment', 'supernova-experiment'),
            )
         ),
        ('Data analysis', (
            ('Data access', 'data-access.html'),
            ('Follow-up program', 'followup.html'),
            ('Analysis software', 'software.html'),
            ('Documentation', 'documentation.html'),
            )
         ),
        )

# Defines the "key information" box on the front page
KEY_INFORMATION = (
    ('Status', 'status.html'),
    ('Observatory guidebook', 'documentation.html'),
    ('Frequently asked questions', 'faq.html'),
    ('Volunteer to serve on a review panel',
        'https://goo.gl/forms/p4ZqiTQSEHjbM6nz2'),
    ('Simulated data', 'data-access.html#simulated-data'),
) # make the simulated data link work!

# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
            ('<b>30 Jun 2017 tbc</b>',
             'Release of Cycle 1 call for proposals',
             'k2-proposing-targets.html'), # link to a new item?
            ('<b>01 Oct 2017 tbc</b>',
             'Cycle 1 proposal submission deadline ',
             'k2-proposing-targets.html'), # link to a new item?
            ('<b>20 Mar 2018</b>',
             'Planned mission launch date',
             'operations.html'), # link to a news item?
         )

# Defines the "meetings" box on the front page
MEETINGS = (
            ('<b>4–8 Jun 2017</b><br>'
             'AAS 230th Meeting',
             'https://aas.org/meetings/aas230'),
            ('<b>19–23 Jun 2017</b><br>'
             'Kepler & K2 SciCon IV',
             'https://keplerscience.arc.nasa.gov/scicon4/'),
            ('<b>16-21 Jul 2017</b><br>'
             'Tessting Stellar Astrophysics, TASC3 KASC10 Workshop',
             'http://www.tasc3kasc10.com/'),
            )

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ('News, Media, and Education Resources',
             'https://tess.gsfc.nasa.gov/'),
            ('TESS @ MIT',
             'http://space.mit.edu/TESS/TESS/TESS_Overview.html'),
            # ('TESS @ Orbital ATK',
            #  'http://www.ballaerospace.com/page.jsp?page=72'),
            ('TESS @ MAST',
             'http://archive.stsci.edu/tess'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

BOOTSTRAP_NAVBAR_INVERSE = True


DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
