# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="calliope-plot",
    version="0.0.1.dev",
    author="Jann Launer",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="",
    package_dir={"calliope_plot": "src"},
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=["plotnine"],
    extras_require={
        "dev": ["pytest", "black", "isort", "flake8", "pre-commit"],
        "docs": [
            "sphinx",
            "sphinx-book-theme",
        ],
    },
)
