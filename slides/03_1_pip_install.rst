Install via pip
***************

**pip** is the package installer for Python.
You can use **pip** to install packages with dependencies from the Python Package Index and other indexes.

- Python Package Index (PyPI)

.. code-block:: sh

    pip install sphinx

- Local directory

.. code-block:: sh

    pip install .

- GitHub from (branch, release, tag, commit)

.. code-block:: sh

    pip install git+git://github.com/author/repository.git@master

- From the private packages

**pip** is just python script, when you run it with python you will do work for that python.
If you run script without explicit python executable, you will use latest installed pip.

.. code-block:: text

    > pip.exe -V
    pip 19.2.3 from h:\python27\lib\site-packages\pip (python 2.7)


You can run pip with explicit Python version

.. code-block:: text

    > c:\Python38\python.exe -m pip -V
    c:\Python38\lib\site-packages\pip (python 3.8)

..
  pip это инструмент для установки зависимостей, с помощь него можно устанавливать библиотеки из разных мест.
  Из централизованного хранилища артефактов (поведение по умолчанию)
  Указывая путь до папки с setup.py (замена python setup.py)
  Из любой точки гитхаба: ветка, тэг, коммит, релиз
  Из прочих мест. Ссылка на архив с библиотекой, приватные аналоги PyPI

  Пип это простой скрипт на питоне, оне не знает, куда нужно устанавливать. Все знания приходят из интерпретаторе питона.
  Если у вас установленно несколько питонов, то пакет поставится для того питона через который был вызван пип.
  Это является частым источником проблем, если вы установили библиотеку для оного питона и пытаетесь использовать её из другого.
