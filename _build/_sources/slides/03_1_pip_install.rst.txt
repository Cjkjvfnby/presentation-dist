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
  Посмотрим, откуда пип может устанавливать библиотеки.

  Во первых тз централизованного хранилища артефактов пупи Питонпакадж Индекс
  Из папки с setup.py
  Из любой точки гитхаба будь то ветка, тэг, коммит или один из релизов
  Из urls ссылок, и закрытых хранилищ построенных по типу пупи.

  Пип это просто скрипт на питоне, оне не знает, куда нужно устанавливать. Знания о папках скриптов и библиотек ему приносит интерпретатор который его запускает.
  Если у вас установленно несколько питонов, то пакет поставится для того питона через который был вызван пип.
  Это является частым источником проблем, если вы установили библиотеку для одного питона и пытаетесь использовать её из другого.
  Например популярные пакетный менеджер на макоси home brew, добавляет новые алиасы к пипу.  pip2 pip3, чтобы было понятно куда ставить.
  Но всегда можно воспользоваться старым добрым python -m
