=============
calliope-plot
=============

A collection of plots for calliope inputs and results.

Installation
============

Install local repository in your environment:

    pip install -e <path to repo>

You can also point to the GitHub repository in your project's dependencies.
In conda environment.yaml:

   - pip
   - pip:
     - git+https://github.com/<repository>.git@<commit or tag id>

In virtualenv requirements.txt:

    -e git+https://github.com/<repository>.git@<commit or tag id>

Development
===========

Install dev dependencies:
    
    pip install calliope-plot[dev]

Activate pre-commit hooks:

    pre-commit install

Docs
----

Minimal: Document usage in README.rst
Extended: Use sphinx docs, focus on API.

Build docs locally:
    
    cd docs
    make html
