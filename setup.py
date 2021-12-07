from setuptools import setup
from ptflutter import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ptflutter",
    version=__version__,
    author="Pham Xuan Tien",
    author_email="tienpx.x.x@gmail.com",
    description="A code generator for Flutter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tien-px/pt_flutter_tools",
    license="MIT",
    packages=[
        "ptflutter",
        "ptflutter/config",
        "ptflutter/core",
        "ptflutter/create",
        "ptflutter/figma",
        "ptflutter/generate",
        "ptflutter/rename",
        "ptflutter/template",
        "ptflutter/usecase",
        "ptflutter/utils",
        "ptflutter_templates",
    ],
    entry_points={"console_scripts": ["ptflutter = ptflutter.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    install_requires=[
        "clipboard>=0.0.4",
        "PyYAML>=6.0.0",
        "cssutils>=2.2.0",
        "Jinja2>=2.10",
        "arghandler>=1.2",
    ],
    include_package_data=True,
)
