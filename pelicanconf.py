#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Levi G.'
SITENAME = u'Happy Coding'
SITEURL = ''
BIO = u'科技粉、开源文化拥趸、游戏迷、电影爱好者。'

PLUGIN_PATHS = ['plugins']
#PLUGINS = ['extract_toc']
PLUGINS = ['render_math']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

DEFAULT_METADATA = {
    'status': 'draft',
}

# ERR
"""
THEME = "pelican-themes/backdrop"
THEME = "pelican-themes/bold"
THEME = "pelican-themes/burrito"
THEME = "pelican-themes/chameleon"
THEME = "pelican-themes/irfan"
THEME = "pelican-themes/maggner-pelican"
THEME = "pelican-themes/mnmlist"
THEME = "pelican-themes/pelican-twitchy"
THEME = "pelican-themes/pjport"
THEME = "pelican-themes/sora"
THEME = "pelican-themes/syte"
THEME = "pelican-themes/twenty-html5up"
THEME = "pelican-themes/water-iris" # X 乱码
"""

# Neeeeds turning
"""
THEME = "pelican-themes/cebong"
THEME = "pelican-themes/chunk"
THEME = "pelican-themes/elegant"
THEME = "pelican-themes/iris"
THEME = "pelican-themes/lannisport"
THEME = "pelican-themes/lightweight"
THEME = "pelican-themes/neat"
THEME = "pelican-themes/nikhil-theme"
THEME = "pelican-themes/pelipress" 
"""

# Pretty
"""
THEME = "pelican-themes/Nuja" # 只需加公式，改中文 X 没有缩略
THEME = "pelican-themes/blue-penguin" # 只需加公式，改中文 X 没有缩略
THEME = "pelican-themes/blueidea" # 只需加公式，改中文 X 只有一个文章
THEME = "pelican-themes/foundation-default-colours" # 只需改中文，调大小
THEME = "pelican-themes/fresh" # 格式不错，只需加公式，改中文，调颜色
THEME = "pelican-themes/html5-dopetrope" # 很漂亮，结构、布局很喜欢，正文缩进格式有问题，没有公式
THEME = "pelican-themes/martin-pelican" # 论文一样，没有链接位，用的是 googleapi X 行公式有问题
THEME = "pelican-themes/notmyidea-cms" # 只需加公式，改中文 X 只有一个文章
THEME = "pelican-themes/pelican-bootstrap3" # 只需加公式，改中文，加表格
THEME = "pelican-themes/pelican-cait" # 简洁漂亮。只需加公式，改中文，加表格 X 没有外链
THEME = "pelican-themes/pujangga" # 干净整洁。只需加公式，改中文 X 没有缩略
THEME = "pelican-themes/pure" # 简洁漂亮。只需加公式，改中文，加表格 X 没有外链
THEME = "pelican-themes/relapse" # 整齐干净。只需加公式，改中文，加表格
THEME = "pelican-themes/simple-bootstrap" # 简洁漂亮。只需加公式，改中文，加表格 X 没有外链
THEME = "pelican-themes/sneakyidea" # 只需加公式，改中文，调表格 X 只有一个文章
THEME = "pelican-themes/subtle" # 只需加公式，改中文，调表格 X 只有一个文章
THEME = "pelican-themes/sundown" # 只需加公式，改中文，调表格 X 没有外链
THEME = "pelican-themes/svbhack" # 整齐干净。只需加公式，改中文，加表格，加头像
THEME = "pelican-themes/svbtle" # 只需加公式，改中文，加表格
THEME = "pelican-themes/zurb-F5-basic" # 只需加公式，改中文，调表格

THEME = "pelican-themes/graymill" # X 无公式，美感略差
THEME = "pelican-themes/franticworld" # 动态，暗系，有表格 X 无公式，美感略差
THEME = "pelican-themes/Flex"
THEME = "pelican-themes/pelican-cait" # 简洁漂亮。只需加公式，改中文，加表格 X 没有外链
THEME = "pelican-themes/zurb-F5-basic" # 只需加公式，改中文，调表格
THEME = "pelican-themes/Casper2Pelican" # X 有广告
"""

THEME = "pelican-themes/mnmlist" # X error
THEME = "pelican-themes/monospace" # X error
THEME = "pelican-themes/nmnlist" # X error
THEME = "pelican-themes/blue-penguin" # X error
THEME = "pelican-themes/voce" # X error
THEME = "pelican-themes/uikit" # X error
THEME = "pelican-themes/tuxlite_zf" # X error
THEME = "pelican-themes/zurb-F5-basic" # X error
THEME = "pelican-themes/subtle" # X error
THEME = "pelican-themes/clean-blog" # X
THEME = "pelican-themes/martin-pelican" # X

THEME = "pelican-themes/medius" # X 移动版
THEME = "pelican-themes/Nuja"
THEME = "pelican-themes/elegant"
THEME = "pelican-themes/nest"
THEME = "pelican-themes/alchemy" #
THEME = "pelican-themes/Flex"
THEME = "pelican-themes/hyde"
THEME = "pelican-bootstrap3" # err
THEME = "fresh" # ****
THEME = "relapse" # ***
THEME = "Flex" # *
THEME = "cebong" # ****
THEME = "subtle" # *****
THEME = "foundation-default-colours" # X latex
THEME = "franticworld" # *****
THEME = "alchemy"

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Lex Chow的博客', 'https://chou.it'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('envelope', 'mailto:leaveye@hotmail.com'),
          ('github', 'https://github.com/leaveye'),
          ('qq', '14517405'),)

DEFAULT_PAGINATION = 20

# Disqus

DISQUS_SITENAME = 'blog-levi-g-info'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
