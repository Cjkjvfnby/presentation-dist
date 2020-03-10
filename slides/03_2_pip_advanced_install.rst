Working with packages
*********************

Specify version to be installed
===============================

- Exact version:  **==**
- Lower bound: **>, >=**
- Upper bound: **<, <=**

Get list of installed packages with their version
=================================================

.. code-block:: text

    > pip freeze
    flake8==2.6.2
    flake8-putty==0.4.0
    mccabe==0.5.3
    packaging==20.1
    plumbum==1.6.8
    pycodestyle==2.0.0
    pyflakes==1.2.3
    pyparsing==2.4.6
    six==1.14.0

Install many packages with one command
======================================

Requirements file for **flake8**
--------------------------------

.. literalinclude:: flake8.pip
   :language: text
   :caption: requirements.pip


Installation
------------

.. code-block::

    > pip install -r slides/requirements.pip
    Collecting pyflakes<2.2.0,>=2.1.0 (from -r slides/requirements.pip (line 1))
    Collecting pycodestyle<2.6.0,>=2.5.0 (from -r slides/requirements.pip (line 2))
    Collecting mccabe<0.7.0,>=0.6.0 (from -r slides/requirements.pip (line 3))
    Installing collected packages: pyflakes, pycodestyle, mccabe
    Successfully installed mccabe-0.6.1 pycodestyle-2.5.0 pyflakes-2.1.1

..
  Расмотрим некоторые дополнительные возможности пип.
  Он позволяет указывать версию пакета который вам необходим. Это можно сделать как явно, так и указывая интервал. Этот подход дает воспроизводимый результат.
  Для просмотра версий установленных пакетов можно использовать команду pip freeze
  Используя список установленных пакетов и их версий можно создать свой набор зависимостей. , это рекомендованный шаг для каждого проекта.
  Использование неограниченных зависимостей может выстрелить в любой момент. Вечерний релиз, который шел лишние два часа меня этому научил.
  Можно устанавливать сразу несколько пакетов за один шаг, это будет быстрее если у пакетов есть общие зависимости.
  Можно записать список зависимостей в файл и установить все одним шагом. Такой файл удобно хранить в репозитории, им могут пользоваться как люди так и скрипты автоматизации.
  Для указания файла с требованиями используется аргумент -r.  В самом файле с помощью префикса -r можно использовать другие файлы,
  это может понадобиться когда есть несколько разных места для установки и не хочется дублировать зависимости.
  В девелопмент среде все зависимости ставятся на машину разработчика, а в продакшене на разные машины.

  Вот поговорили как пользоваться пакетами перейдем к созданию.
