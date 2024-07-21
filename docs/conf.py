"""Sphinx configuration file."""

import os
import sys
import time


# General configuration.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
author = "@Robpol86"
copyright = "{}, {}".format(time.strftime("%Y"), author)
html_last_updated_fmt = f"%c {time.tzname[time.localtime().tm_isdst]}"
master_doc = "index"
project = __import__("setup").NAME
pygments_style = "friendly"
release = version = __import__("setup").VERSION
templates_path = ["_templates"]
extensions = []


# Options for HTML output.
html_context = dict(
    conf_py_path="/docs/",
    display_github=True,
    github_repo=os.environ.get("TRAVIS_REPO_SLUG", "/" + project).split("/", 1)[1],
    github_user=os.environ.get("TRAVIS_REPO_SLUG", "robpol86/").split("/", 1)[0],
    github_version=os.environ.get("TRAVIS_BRANCH", "master"),
    source_suffix=".rst",
)
html_copy_source = False
html_favicon = "favicon.ico"
html_theme = "sphinx_rtd_theme"
html_title = project


# autodoc
extensions.append("sphinx.ext.autodoc")


# extlinks.
extensions.append("sphinx.ext.extlinks")
extlinks = {
    "github": (
        f"https://github.com/robpol86/{project}/blob/v{version}/%s",
        "",
    )
}


# google analytics
extensions.append("sphinxcontrib.googleanalytics")
googleanalytics_id = "UA-82627369-1"


# SCVersioning.
scv_banner_greatest_tag = True
scv_grm_exclude = (".gitignore", ".nojekyll", "README.rst")
scv_overflow = ("-W",)
scv_show_banner = True
scv_sort = ("semver", "time")
