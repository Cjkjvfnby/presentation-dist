Distribute packages
###################

Release on PyPI
---------------

PyPI has extra requirements for packages.
**README.md** and **LICENCE** are required as well as extra meta data fields.

Depending on the package way you can use `distutils <https://packaging.python.org/tutorials/packaging-projects/>`_
or `flit <https://flit.readthedocs.io/en/latest/index.html>`_.

You will also need an account on PyPI.

In both cases it is quite simple procedure that includes loading package to test server, where you can check how it will look like,
and after that load it to PyPI.

Wheel vs Egg
------------

Wheel is currently considered the standard for built and binary packaging for Python. `Case closed <https://packaging.python.org/discussions/wheel-vs-egg/>`_

Unofficial Windows Binaries for Python Extension Packages are distributed with wheels. Pip compiles C++ extension on user machine,
it required installed software, otherwise you can download already compiled code from the `internet <https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_


..
  Публичную библиотеку можно опубликовать на PyPI. Это упростит её установку для сторонних разработчиков.
  Для публикации на ПуПи требуется более полное заполнение данных и наличие аккаунта. Он бесплатный.
  Подробнее рассматривать инструкции не имеет смысла, это достаточно редкий процесс. Самая сложная в нем часть, это сделать хорошее описание библиотеки.

  Стоит упомянуть про форматы в которых хранятся пакеты это более новый Wheel и устаревший Egg.
  Пип поддерживает оба формата, я на практике не сталкивался с ситуацией когда мне бы пришлось узнавать о формате более подробно.

  Если у вас не установлен компилятор, то установить через пип некоторые библиотеке зависящие от сишного кода не получится,
  ведь они компилируются у вас на машине, но можно скачать уже собранные пакеты.
  Если раньше они распространялись в виде exe файлов, то теперь в формате wheel.
