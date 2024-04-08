# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'pythainlp-tutorials'
copyright = '2019 - 2024, PyThaiNLP'
author = 'PyThaiNLP'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- Get version information and date from Git ----------------------------

try:
    from subprocess import check_output
    release = check_output(['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
    today = check_output(['git', 'show', '-s', '--format=%ad', '--date=short'])
    today = today.decode().strip()
except Exception:
    release = '<unknown>'
    today = '<unknown date>'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# Custom css file
html_css_files = ["style.css"]

# Don't add .txt suffix to source files (available for Sphinx >= 1.5):
html_sourcelink_suffix = ''

nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}
{% set docname = docname.split('/')[1] %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::
        Interactive online version: 
        :raw-html:`<a target="_blank" href="https://mybinder.org/v2/gh/pythainlp/tutorials/master?filepath=source/notebooks/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`
        :raw-html:`<a target="_blank" href="https://colab.research.google.com/github/PyThaiNLP/tutorials/blob/master/source/notebooks/{{ docname }}"><img alt="Google Colab badge" src="https://colab.research.google.com/assets/colab-badge.svg" style="vertical-align:text-bottom"></a>`
.. raw:: latex

    \nbsphinxstartnotebook{The following section was created from
    \texttt{\strut{}{{ docname }}}:}
"""

nbsphinx_epilog = r"""
.. raw:: latex

    \nbsphinxstopnotebook{\hfill End of notebook.}
"""

master_doc = 'index'
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
