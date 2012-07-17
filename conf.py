# -*- coding: utf-8 -*-



import sys, os
project = u'Django 最佳实践'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'
master_doc = 'contents'
language = 'zh_CN'
exclude_patterns = ['_build']
extensions = ['sphinx.ext.pngmath']
pygments_style = 'sphinx'

html_title = u'Django 最佳实践'
html_theme = 'yeetheme'
html_theme_path = ['../../../templates/sphinx', ]
htmlhelp_basename = 'django-best-practices'
html_add_permalinks = None

file_insertion_enabled = False
latex_documents = [
  ('index', 'django-best-practices.tex', u'Django 最佳实践',
   u'', 'manual'),
]


#Add sponsorship and project information to the template context.
context = {
    'MEDIA_URL': "/media/",
    'slug': 'django-best-practices',
    'name': u'Django 最佳实践',
    'analytics_code': '',
}

html_context = context

