# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from sphinx.application import Sphinx

project = "sphinxcontrib-data-pipeline"
copyright = "2024, Michael Buehlmann"
author = "Michael Buehlmann"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib_data_pipeline",
    "sphinxcontrib.mermaid",
    "sphinx_tabs.tabs",
    "sphinx_toolbox.collapse",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# workflows parsers
driver_parser = "sphinxcontrib_data_pipeline.parsers.example_yaml_parser:parse_drivers"
data_product_parser = (
    "sphinxcontrib_data_pipeline.parsers.example_yaml_parser:parse_dataproducts"
)


def setup(app: Sphinx):
    app.add_css_file("custom.css")
