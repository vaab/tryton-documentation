Installation Procedure
======================

Tryton is separated into independent parts:

- the server named ``trytond``
- the GTK client named ``tryton``
- and several modules to extends server capabilities (ie: account, bank, party, project...)

You can directly install all these independentely using pip command-line tool
on your system (or in a virtualenv, a recommended setup) as each of these are
available on the Python Package Index. Here's how to proceed:

- Installing the server

  .. code-block:: bash

      pip install trytond

- Installing the GTK client

  .. code-block:: bash

      pip install tryton

- Installing any module for server:

  .. code-block:: bash

      pip install trytond_MODULE_NAME    # Replace MODULE_NAME with the name of the module

  You might be interested by a `list of available modules
  <https://pypi.python.org/pypi?:action=browse&show=all&c=551>`_.


Preparing Application Servers
-----------------------------

TODO


Basic Database Configuration
----------------------------

Postgres is the recommended database engine for tryton
Install Postgres database. Steps for installing Postgres can be
found from `Postgres Installation <http://wiki.postgresql.org/wiki/Detailed_installation_guides/>`_
Install the database and give a new password to the postgres database
user.


Installing from PyPI
--------------------

For installing tryton form Python Package Index, you can download from
`Tryton PyPI Package <https://pypi.python.org/pypi/tryton/3.0.0/>`_
Download the ``tar.gz`` file of tryton and run the ``setup.py`` file to install
from PyPI.


Creating a Virtualenv
`````````````````````

Refer to `Virtualenv Docs <https://pypi.python.org/pypi/virtualenv/>`_
for getting started with virtualenv.

Create the virtualenv and activate the virtualenv you created.

.. code-block:: bash

    $ sudo easy_install virtualenv  # to install virtualenv
    $ virtualenv foobar             # to create a virtualenv
    $ source foobar/bin/activate    # to activate the virtualenv
    $ deactivate                    # to deactivate the virtualenv

Now you can install ``tryton`` and ``trytond`` in your virtualenv by using pip
commands.
