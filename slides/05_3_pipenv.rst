pipenv
======

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

You no longer need to use pip and virtualenv separately. They work together.

This tools provide more simple way to create virtual env and manage dependencies.

File with requirements are maintened automatically. When you install/delete new version it si updated.
It also stores library hashes, if someone will update packge without version you will be warned.


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