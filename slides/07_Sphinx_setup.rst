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
  Начальная установка включает в себя установку требуемых библиотек.
  Запуск скрипта первоначальной настройки, который спросить вас несколько вопросов и сгенерирует файлы конфигурации
  Настройка необходимых расширений, в нашем случае это автоматические генераторы из исходного кода
  Проект готов можно приступать к написанию документации. (показать исходный код слайда)
