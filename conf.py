#!/usr/bin/env python3
"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
# pylint: disable=invalid-name,redefined-builtin

author = 'Xander Harris'
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = True
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv/*',
    '.tmp/*',
    '.pytest_cache/*',
    'resources/templates/NOTES.txt',
]

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoyaml',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = '_static/img/StorageClasses.png'
html_favicon = '_static/img/StorageClasses.png'
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/edwardtheharris/helm-storage-classes",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "GitHub Pages",
            "url": "https://edwardtheharris.github.io/helm-storage-classes/index.html",
            "icon": "_static/githubpages.png",
            "type": "local"
        },
        {
            "name": "Helm",
            "url": "https://helm.sh",
            "icon": "_static/helm.png",
            "type": "local"
        }
   ]
}
myst_dmath_double_inline=True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = 'StorageClasses'
rst_epilog = """
.. sectionauthor:: Xander Harris <xandertheharris@gmail.com>
"""
release = '0.0.1'
show_authors=True
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
}
templates_path = ['_templates']
