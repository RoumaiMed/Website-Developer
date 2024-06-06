# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
from datetime import datetime
from collections import OrderedDict

project = 'Roumai Medical Documentation'
copyright = f'{datetime.now().year}, Roumai Medical Co., Ltd.'
language = 'zh_CN'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'myst_parser',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_js_files = ['js/selector.js']

products_versions = OrderedDict({
    "emg-single": ['latest', 'v0.0.2', 'v0.0.1'],
    "emg-wristband-16": ['latest', 'v0.0.3', 'v0.0.2', 'v0.0.1']
})

current_path = os.path.dirname(os.path.abspath(__file__))
current_product = current_path.split('\\')[-2]
current_version = current_path.split('\\')[-1]

products_versions.move_to_end(current_product, last=False)

if current_version in products_versions[current_product]:
    products_versions[current_product].remove(current_version)
    products_versions[current_product].insert(0, current_version)

html_context = {
    'products_versions': products_versions,
    'current_product': current_product,
    'current_version': current_version,
}

version = current_version
