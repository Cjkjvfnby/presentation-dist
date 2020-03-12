Setup Sphinx
############

Install Sphinx and style
========================

.. literalinclude:: ../requirements.pip
   :language: text
   :caption: requirements.pip

.. code-block:: text

    pip install -r requirements.pip

Run `sphinx-quickstart <https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html>`_ and answer all hist question to create a project base.

Configure required extensions
=============================

.. literalinclude:: ../conf_exts.py
   :language: python
   :caption: conf.py

Generate an HTML
================

.. code-block:: text

    make html

..
  Чтобы начать использовать Сфинкс надо сделать несколько простых действий.
  Сначала устанавливаем требуемые библиотеки. Сам сфинкс и тему к нему. В сфинксе есть встроенные темы, но мне нравится эта.
  Дальше запускаем скрипт первоначальной настройки quick-start который спросит вас несколько вопросов и сгенерирует файлы конфигурации
  Настроим расширения, нам достаточно тех, что идут из коробки.
  Проект готов можно приступать к написанию документации. (показать исходный код слайда)
