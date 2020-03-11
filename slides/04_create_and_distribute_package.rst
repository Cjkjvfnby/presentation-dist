Create and distribute packages
##############################

Create package
--------------

To create package you need to make a **setup.py** file.

Process is described in the `Documentation <https://docs.python.org/3/distutils/setupscript.html>`_.

You can specify
- package meta info like: name, description, version
- which python is supported by your package
- specify required dependencies
- script that will be installed to system (like pip)


Release on PyPI
---------------

To release you package on pip you will need to create some additional files
**README.md** and **LICENCE** and follow `instructions <https://packaging.python.org/tutorials/packaging-projects/>`_.


Wheel vs Egg
------------

Wheel is currently considered the standard for built and binary packaging for Python. `Case closed <https://packaging.python.org/discussions/wheel-vs-egg/>`_

Unofficial Windows Binaries for Python Extension Packages are distributed with wheels. Pip compiles C++ extension on user machine,
it required installed software, otherwise you can download already compiled code from the `internet <https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_


..
  Любой может сделать собственный пакет и зарелизить его на PyPI. Но не всем это нужно.
  Обычно такие требования появляются когда есть пользователи библиотеки в других структурах.

  На соответствующих ресурсах есть необходимая документация и с её помощью это можно легко сделать.
  Для создания пакета необходимо создать файл setup.py и прописать в нем информацию о вашей библиотеке.

  Расскажу об некоторых возможностях:
  В файле setup.py можно указать все необходимые зависимости, в том числе отдельно для каждой версии питона.
  При установке через пип, все зависимости и их зависимости будут установлены. Возможны конфликты зависимостей.
  Можно добавить скрипты которые будет установленны в систему. Пример такого скрипта это pip.
  Во время инсталляции pip создаёт обертку подходящую для операционной системы и кладет ей в папку со скриптами.

  Публичную библиотеку можно опубликовать на PyPI. Это упростит её установку для сторонних разработчиков.
  Для публикации на ПуПи требуется более полное заполнение данных и наличие аккаунта. Он бесплатный.
  Подробнее рассматривать инструкции не имеет смысла, это достаточно редкий процесс. Самая сложная в нем часть, это сделать хорошее описание библиотеки.

  Стоит упомянуть про форматы в которых хранятся пакеты это более новый Wheel и устаревший Egg.
  Пип поддерживает оба формата, я на практике не сталкивался с ситуацией когда мне бы пришлось узнавать о формате более подробно.

  Если у вас не установлен компилятор, то установить через пип некоторые библиотеке зависящие от сишного кода не получится,
  ведь они компилируются у вас на машине, но можно скачать уже собранные пакеты.
  Если раньше они распространялись в виде exe файлов, то теперь в формате wheel.
