Virtual environment
###################

Each application can get it own python.
Virtual environment allow to fast switch between projects by having copy of installed python modules for each project.
Tools for virtual environment creation is part of the Python 3 installation `installation <https://docs.python.org/3/tutorial/venv.html>`_.
It allows creating a copy of the "python" installed libraries in specified folder. You can install dependencies for each environment separately.

Virtual env creation example
============================

Creating virtual env, this command wil just create a folder with activation scripts and empty folder for libraries

.. code-block:: text

    > python -m venv myenv
    > dir myenv
    Include/
    Lib/
    Scripts/
    pyvenv.cfg

Lets check that we don't have bottle installed for python

.. code-block:: text

    > python -c "import bottle"
    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    ModuleNotFoundError: No module named 'bottle'

Activate virtual environment, install library, check that in can be imported

.. code-block:: text

    > myenv\Scripts\activate
    (myenv) pip install bottle
    Successfully installed bottle-0.12.18
    (myenv) python -c "import bottle"

Deactivate virtual environment, check that original python was not affected

.. code-block:: text

    (myenv) myenv\Scripts\deactivate
    > python -c "import bottle"
    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    ModuleNotFoundError: No module named 'bottle'

..
    Виртуальное окружение это способ лего переключаться между проектами. Для каждого проекта можно сделать свой питон с нужным набором библиотек.
    Когда это действительно надо?
    У вас есть проекты с несовместимыми зависимостями, например разные версии одной библиотеки.
    Вы хотите проверить, что для библиотеки достаточно тех зависимостей которые вы указали.

    Создание и работа с виртуальным окружением хорошо описана в документации.
    Когда вы включаете виртуальное окружение, то это работает только в текущей консоли.
    Открывая новую консоль нужно снова активировать окружение. Из полюсов такого подхода, то что вы можете работать одновременно в разных окружениях.

    Рассмотрим работу с виртуальным окружением.
    Первым делом мы создаем папку с ним. Там лежат почти пустые паки скриптов и библиотек, по умолчанию установлен только пип.
    Хотя при желании можно указать, чтобы у виртуального окружения был доступ к библиотекам основного питона.

   Дальше необходимо активировать виртуальное окружение. Это делается скриптом, который лежит в существующей папке.
   Строка приветствия при этом меняется, и все команды связаннае с питоном в данной консоле будут использовать питон из этого окружения.
   Остальные команды тоже будут работать.

   Такой подход позволяет работать с разными окружениями в разных консолях одновременно.

   После того как мы закончили работу, виртуальное окружение можно деактивировать.
