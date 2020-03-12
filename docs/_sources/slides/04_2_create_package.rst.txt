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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
- `poetry <https://github.com/Cjkjvfnby/presentation-dist/tree/master/demo/poetry-demo>`_
- `flit <https://github.com/Cjkjvfnby/presentation-dist/tree/master/demo/flit-demo>`_


..
  PEP-517 позволил отвязать установку пакетов от единственного инструмента который мог это делать и теперь каждый может сделать свой инструмент.
  Чем не применули воспользоваться разработчики.  Информация о инструменте лежит в пайпроджект томл

  Если инструмент не указан или пайпрожект томл отсутствует то используется дистутил. Это работает начиная с пип 19.0

  Теперь указание инструмента это единственный требуемый параметр.  Остальные требования уже выдвигает инструмент.
  Для дистутилс это наличие сетпап пай. Поетри и флит требуют новых секций в пайпрожект томл.

  Какой бы вы инструмент не выбрали, все они требуют одних и тех же данных.
  Это метаданные пакета: название, описание, автор, версия.  Для версии рекомендовано использовать симвер. Кто знает что это такое?

  Версии питона которые поддерживаются. В каждом случае это определяется самостоятельно. Для публичных библиотек ниже 3.5 не стоит опускаться,
  большинство дистрибутивов уже прошли эту версию.
  Для внутренних проектов, выбирайте самой новую из возможных версий, чтобы иметь в рукаве побольше новых возможностей.

  Зависимости пакета. Не забываем указывать версии зависимостей, такие инструменты как поетри не дадут вам совершить ошибку.

  Скрипты. Вы можете написать просто системные скрипты которые скопируются в папку скриптов при установке.
  Есть такой подход точки входа (entry points). Вы указываете какая питоновская функция должна быть вызвана, а установщик пакета сам создаст для неё обёртку.

  Сделать пакет очень просто.
  Для дистутил надо написать setup.py. Большую часть работы по созданию берёт на себя CTRL-C/CTRL-V.
  Для поетри это делается одной командой. Для флит тоже, но там появляется визард который задаст пару несложных вопросов.
  Давайте посмотрим на примеры.
