pipenv
======

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

You no longer need to use pip and virtualenv separately. They work together.

This tools provide more simple way to create virtual env and manage dependencies.

Creating env
************

.. code-block:: text

    > pipenv install bottle
    Creating a Pipfile for this project…
    Installing bottle…
    Adding bottle to Pipfile's [packages]…
    Installation Succeeded
    Pipfile.lock not found, creating…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Success!
    Updated Pipfile.lock (71876c)!
    Installing dependencies from Pipfile.lock (71876c)…
    ================================ 1/1 - 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

As result package lock is created. This file contains all installed libraries, their hashes and versions.

.. literalinclude:: Pipfile.lock
  :caption: Pipfile.lock
  :language: text
  :lines: 19-26

Package lock is updated each time install/uninstall command is called.
It also provides option to provide dev/test dependencies only, no need to have addition requirements file for development.

Command like pipenv install/uninstall are directory dependent unlike pip install.

To start virtual env use pipenv shell. This produces same result as activation of the virtual env.

Lets highlight similarity and differences

+------------------------------+-----------------------------+-----------------------------+
| Characteristic               | Pip and virtual env         | pipenv                      |
+==============================+=============================+=============================+
| installing libraries         | anywhere                    | in specific folder          |
+------------------------------+-----------------------------+-----------------------------+
| running venv                 | in specific folder          | in specific folder          |
+------------------------------+-----------------------------+-----------------------------+
| tracking versions            | yes                         | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| update requirements file     | no                          | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| sho dependency graph         | no                          | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| can install dev dependencies | no                          | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| tracking library hash        | no                          | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| use pip and venv under hood  | yes                         | yes                         |
+------------------------------+-----------------------------+-----------------------------+
| preferred way to manage deps | no                          | yes                         |
+------------------------------+-----------------------------+-----------------------------+


..
    Инструменты работы с зависимостями широко распространены в экосистемы джаваскрипт. Кто слышал про npm?
    В джавасрипте без них нет жизни, ведь даже такая простая функция как расширить слово до заданного размера,
    добавив слева недостающее количество указанных символов, поставляется отдельной библиотекой.
    В этот момент начинаешь ценить батарейки в комплекте. Кстати как называется аналог в питоне? (str.rjust)
    Также npm есть большие проблемы безопасности, кто угодно может добавить пакет,
    код которого потом будет выполнятся в браузере пользователя.
    Эта проблема воспроизводится и для Питона, но за счет того, что питон более консервативный и того,
    что большинство нужных библиотеки имеет долгую историю, не так актуальна.

    Пипенв заставляет вас работать только в виртуальном окружении.
    При установке/установке он автоматически добавляет/удаляет их в файл с зависимостях. Теперь вы никогда не забудете про новые зависимости.
    В целях повышения безопасности, он хранить хэш полученного пакета.
    Для npm существуют внешние инструменты, которые содержат базу зависимостей с уязвимостями. Хэш нужен чтобы проверять, что файл библиотеке соответствует заявленной версии.
    Они проверяют, что в в ваших зависимостях их нет. Одним из таких инструментов является Sonar Cube, который широко используется в Эпаму.
    Аналогов, которые проверяют по хэшу я не нашёл, есть только проверяющие по версиям пакетов.

    Посмотрим на пример работы с пипенв.
    Начинаем с выбора директории.   pipenv install находит утановленное окружение в текущей папке, если его нет то содает.
    После этого добавляет необходимый пакет в Pipfile.lock.
    Чтобы воспользоваться окружением мы должны либо его активировать либо, выполнять команды через его скрипты.

    Пойдемся по таблице сравнения подходов.

    Пипенв это новый инструмент и он не лишен недостатков. Про него существую как положительные так и отрицательные отзывы.
    Это и послужило причиной появления большого количества аналогов. Я с ним очень мало работал и для простых случаев он не вызывал проблем.



