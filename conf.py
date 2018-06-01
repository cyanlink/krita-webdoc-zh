# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Krita Manual'
propername = 'Krita Manual'
description = 'The official Krita Documentation'
copyright = 'licensed under the GNU Free Documentation License 1.3+ unless stated otherwise'
author = 'Krita Foundation'

import os
import subprocess

# Get the git description if possible, to put it in the footer.

try:
    gitcommitfriendly = subprocess.check_output(["git", "describe", "--always"]).decode("utf-8").strip()
except subprocess.CalledProcessError as exc:
    gitcommitfriendly = None

# We use the full githash for the epub identifier, if not, use the release number.
try:
    gitcommithash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode("utf-8").strip()
except subprocess.CalledProcessError as exc:
    gitcommithash = release

# The short X.Y version
version = '4.0'
# The full version, including alpha/beta/rc tags
release = '4.0.3'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_extra_path = ['.htaccess'] # copy over .htaccess file to each langaguge

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A string of reStructuredText that will be included at the end of every source file that is read.
# This is a possible place to add substitutions that should be available in every file (another being rst_prolog).
rst_epilog = """
.. |mouseleft| image:: /images/icons/Krita_mouse_left.png 

.. |mouseright| image:: /images/icons/Krita_mouse_right.png 

.. |mousemiddle| image:: /images/icons/Krita_mouse_middle.png 

.. |mousescroll| image:: /images/icons/Krita_mouse_scroll.png

.. |toolshapeselection| image:: /images/icons/shape_select_tool.svg

.. |toolshapeedit| image:: /images/icons/shape_edit_tool.svg

.. |tooltext| image:: /images/icons/text-tool.svg

.. |toolcalligraphy| image:: /images/icons/calligraphy_tool.svg

.. |toolgradientedit| image:: /images/icons/gradient_edit_tool.svg

.. |toolpatternedit| image:: /images/icons/pattern_tool.svg

.. |toolfreehandbrush| image:: /images/icons/freehand_brush_tool.svg

.. |toolline| image:: /images/icons/line_tool.svg

.. |toolrectangle| image:: /images/icons/rectangle_tool.svg

.. |toolellipse| image:: /images/icons/ellipse_tool.svg

.. |toolpolygon| image:: /images/icons/polygon_tool.svg

.. |toolpolyline| image:: /images/icons/polyline_tool.svg

.. |toolbeziercurve| image:: /images/icons/bezier_curve.svg

.. |toolfreehandpath| image:: /images/icons/freehand_path_tool.svg

.. |tooldyna| image:: /images/icons/dyna_tool.svg

.. |toolmultibrush| image:: /images/icons/multibrush_tool.svg

.. |toolassistant| image:: /images/icons/assistant_tool.svg

.. |toolmove| image:: /images/icons/move_tool.svg

.. |tooltransform| image:: /images/icons/transform_tool.svg

.. |toolgrid| image:: /images/icons/grid_tool.svg

.. |toolperspectivegrid| image:: /images/icons/perspectivegrid_tool.svg

.. |toolmeasure| image:: /images/icons/measure_tool.svg

.. |toolcolorpicker| image:: /images/icons/color_picker_tool.svg

.. |toolfill| image:: /images/icons/fill_tool.svg

.. |toolgradient| image:: /images/icons/gradient_drawing_tool.svg

.. |toolcolorizemask| image:: /images/icons/colorizemask_tool.svg

.. |toolsmartpatch| image:: /images/icons/smart_patch_tool.svg

.. |toolcrop| image:: /images/icons/crop_tool.svg

.. |toolselectrect| image:: /images/icons/rectangular_select_tool.svg

.. |toolselectellipse| image:: /images/icons/elliptical_select_tool.svg

.. |toolselectpolygon| image:: /images/icons/polygonal_select_tool.svg

.. |toolselectpath| image:: /images/icons/path_select_tool.svg

.. |toolselectoutline| image:: /images/icons/outline_select_tool.svg

.. |toolselectcontiguous| image:: /images/icons/contiguous_select_tool.svg

.. |toolselectsimilar| image:: /images/icons/similar_select_tool.svg

.. |toolpan| image:: /images/icons/pan_tool.svg

.. |toolzoom| image:: /images/icons/zoom_tool.svg

"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'theme'
html_theme_path = ['.'] # make sphinx search for themes in current dir

# the favicon has a property to set it in the documentation, but we don't need to use this
# sphinx appears to automatically search in the theme folder and find the file
#html_favicon = './theme/static/images/favicon.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
	'sticky_navigation': True,
	'collapse_navigation': True,
	'prev_next_buttons_location': 'bottom'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['theme/static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_title = project + " version " + release

html_context = {
    'build_id': os.getenv('BUILD_NUMBER', None),
    'build_url': os.getenv('BUILD_URL', None),
    'commit' : gitcommitfriendly
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'documentationProjectNamedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    'maxlistdepth': '8',
    'figure_align':'ht!',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage[export]{adjustbox}
\let\oincludegraphics\includegraphics
\renewcommand{\includegraphics}[2][]{
    \oincludegraphics[#1,max width=\linewidth,max height=\textheight]{#2}
}
    ''',
    'tableofcontents':'\sphinxtableofcontents',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'kritaManual.tex', project,
     author, 'manual'),
]
latex_show_pagerefs=True
# copy latex scripts to build dir
latex_additional_files = [
    "latexImageMakefile",
]

# -- Internationalization Options --------------------------------------------

locale_dirs = ['locale/']   # Where the PO files will be stored at
gettext_compact = False     # optional.
gettext_additional_targets = ['image'] # allows images to be translatable



# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, propername,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, propername,
     author, project, description,
     'Manual'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
# filename
# epub_basename = project.replace(' ', '_') + '_' + language
epub_title = project+" "+version
epub_description = description

# Technically speaking dublincore accepts multiple author and contributor elements, but
# the sphinx builder only accepts one.
epub_author = author
epub_publisher = author
epub_copyright = copyright


epub_cover = ('_static/images/manual_cover.png', '')

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# The above is false and perhaps a mistake in sphinx' documentation.
# epub_uid maps to id, which is the dc identifier id
# which in turn should be the used scheme.

if os.getenv('BUILD_ID', None) is None:
    # There is no uniform resource name for git, but just randomly pasting a githash is bad form.
    epub_identifier = 'git:'+gitcommithash
    epub_uid = 'githash'
    if gitcommithash == release:
        epub_uid = 'release'
        # there's also no urn for releases, as technically some database thing should be used for that.
        epub_identifier = '_'.join(['Krita_Manual_Build', language, release])
else:
    epub_uid = 'url'
    epub_identifier = os.getenv('BUILD_URL', '')

# Not actually used anywhere? Docs say that this should be what the epub uid is used for but...
epub_scheme = 'URL'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html', '.htaccess']

epub_tocscope = 'includehidden'

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
