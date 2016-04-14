# -*- coding: utf-8 -*-
#
# nilearn documentation build configuration file, created by
# sphinx-quickstart on Fri Jan  8 09:13:42 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shutil
import sphinx

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath('sphinxext'))
import sphinx_gallery

# We also add the directory just above to enable local imports of nilearn
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.imgmath'  # only available for sphinx >= 1.4
              if sphinx.version_info[:2] >= (1, 4)
              else 'sphinx.ext.pngmath',
              'sphinx.ext.intersphinx',
              'numpydoc.numpydoc',
              'sphinx_gallery.gen_gallery',
              ]

autosummary_generate = True

autodoc_default_flags = ['members', 'inherited-members']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# generate autosummary even if no references
autosummary_generate = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# Generate the plots for the gallery
plot_gallery = True

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Nilearn'
copyright = u'The nilearn developers 2010-2015'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
import nilearn
release = nilearn.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []
exclude_patterns = ['tune_toc.rst',
                    'includes/big_toc_css.rst',
                    'includes/bigger_toc_css.rst',
                    ]

# List of directories, relative to source directory, that shouldn't be
# searched for source files.
exclude_trees = ['_build', 'templates', 'includes']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'nilearn'

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'nature.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {'oldversion':False, 'collapsiblesidebar': False}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Machine learning for NeuroImaging"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Nilearn'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logos/nilearn-logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'logos/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['images']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'PythonScientic'


# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
  ('index', 'nilearn.tex', u'NeuroImaging with scikit-learn',
   ur"""Gaël Varoquaux and Alexandre Abraham"""
   + r"\\\relax ~\\\relax http://nilearn.github.io",
   'manual'),

]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "logos/nilearn-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r"""
\usepackage{amsmath}\usepackage{amsfonts}\usepackage{bm}\usepackage{morefloats}
\let\oldfootnote\footnote
\def\footnote#1{\oldfootnote{\small #1}}
"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []
latex_elements = {
  'classoptions': ',oneside',
  'babel': '\\usepackage[english]{babel}',
  # Get completely rid of index
  'printindex': '',
}

# If false, no module index is generated.
latex_use_modindex = False
latex_domain_indices = False

# Show the page numbers in the references
latex_show_pagerefs = True

# Show URLs in footnotes
latex_show_urls = 'footnote'

trim_doctests_flags = True

_python_doc_base = 'http://docs.python.org/2.7'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    _python_doc_base: None,
    'http://docs.scipy.org/doc/numpy': None,
    'http://docs.scipy.org/doc/scipy/reference': None,
    'http://matplotlib.org/': None,
    'http://scikit-learn.org/stable': None,
    'http://nipy.org/nibabel': None,
    #'http://scikit-image.org/docs/0.8.0/': None,
    #'http://docs.enthought.com/mayavi/mayavi/': None,
    #'http://statsmodels.sourceforge.net/': None,
    #'http://pandas.pydata.org': None,
}

extlinks = {
    'simple': (_python_doc_base + '/reference/simple_stmts.html#%s', ''),
    'compound': (_python_doc_base + '/reference/compound_stmts.html#%s', ''),
}

sphinx_gallery_conf = {
    'doc_module'        : 'nilearn',
    'reference_url'     : {
        'nilearn': None,
        'matplotlib': 'http://matplotlib.org',
        'numpy': 'http://docs.scipy.org/doc/numpy-1.6.0',
        'scipy': 'http://docs.scipy.org/doc/scipy-0.11.0/reference',
        'nibabel': 'http://nipy.org/nibabel',
        'sklearn': 'http://scikit-learn.org/stable'}
    }

# Get rid of spurious warnings due to some interaction between
# autosummary and numpydoc. See
# https://github.com/phn/pytpm/issues/3#issuecomment-12133978 for more
# details
numpydoc_show_class_members = False


def touch_example_backreferences(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    examples_path = os.path.join(app.srcdir, "modules", "generated",
                                 "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, 'w').close()

# Add the 'copybutton' javascript, to hide/show the prompt in code
# examples
def setup(app):
    app.add_javascript('copybutton.js')
    app.connect('autodoc-process-docstring', touch_example_backreferences)
