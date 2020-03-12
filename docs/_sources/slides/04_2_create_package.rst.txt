Create packages
###############

Package tools
-------------
It is possible to create package in different ways

setup.py
********
Classic way, you write everything in the **setup.py**.
Where is only one tool that can package it and it is **distutils**.
Recommendation for `packaging projects <https://packaging.python.org/tutorials/packaging-projects/>`_,
description of distutils `features <https://docs.python.org/3/distutils/setupscript.html>`_.

PEP-517/PEP-518
***************
New configuration file is added: **pyproject.toml**
Now, you can specify dependencies that required for installation.
They are used during installation and removed after (`PEP-518 <https://www.python.org/dev/peps/pep-0518/>`_).

You can specify witch tool should be used for installation (`PEP-517 <https://www.python.org/dev/peps/pep-0517/>`_).
You are not tied to distutils anymore. This opens a new era in python distribution.

Here is incomplete list of tools that can be used:

`distutils <https://docs.python.org/3/distutils/setupscript.html>`_
+++++++++
Default tool, still requires **setup.py** to create a package.

`poetry <https://python-poetry.org/docs/>`_
++++++++++++++++++++++++++++++++++++++++++++
All package data is located in **pyproject.toml**, no need to have **setup.py** anymore.
Besides from packaging this tool focuses on dependency management.

`flit <https://flit.readthedocs.io/en/latest/index.html>`_
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

All package data is located in **pyproject.toml**, no need to have **setup.py** anymore.
Cannot be used when need to compile C or bundle Javascript.
This tool has good support for publishing on PyPI.

Information required for packaging
**********************************
- package meta info: name, description, version etc.
  If you publish your library somewhere make sure that you fill this field with normal data.
  Use `semantic versioning <https://semver.org/>`_
- which python is supported by your package.
  Python 3.5 is a good start for public libraries, for limited number of users try to use as new version as you can.
  It will allow you to use all new shiny features
- required dependencies for your package.
  Don't forget to specify exact versions or at least ranges
- script that will be installed to system (like **pip**).
  You can have own script that will be copied to executable dir
  `distutils <https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-scripts-keyword-argument>`_
  or use python function that will be packed as script (Entry point)
  `distutils <https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point>`_
  `poetry <https://python-poetry.org/docs/pyproject/#scripts>`_

Starting
********

setup.py
++++++++
Create manually

poetry
++++++
Create template of the project with **poetry new project_name**

flit
++++
Wizard to create **pyproject.toml** and **LICENSE**

Project examples
****************
- `sampleproject by PyPA <https://github.com/pypa/sampleproject>`_
- `poetry <https://github.com/Cjkjvfnby/demo/>`_
- `flit <https://github.com/Cjkjvfnby/flit/>`_


..
  PEP-517 позволил отвязать создание пакетов от единственного инструмента который мог это делать и теперь каждый может сделать свой.
  Чем не применули воспользоваться разработчики.
