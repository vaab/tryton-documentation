Installation Procedure
=======================
You can directly install Tryton using pip command-line tool in your
virtualev.

.. code-block:: python

    $ pip install trytond
    $ pip install tryton
    $ pip install tryton_module_name

    Replace module_name with the name of the module you want to install

Preparing Application Servers
-----------------------------

TODO

Basic Database Configuraion
---------------------------

Postgres is the recommended database engine for tryton
Install Posgres database. Steps for installing Postgres can be
found from `Postgres Installation <http://wiki.postgresql.org/wiki/Detailed_installation_guides/>`_
Install the database and give a new password to the postgres database
user.

Installing from PyPI
--------------------
For installing tryton form Python Package Index, you can download from
`Trton PyPI Package <https://pypi.python.org/pypi/tryton/3.0.0/>`_
Download the tar.gz file of tryton and run the setup.py file to install
from PyPI.

Creating a Virtualenv
`````````````````````

Refer to `Virtualenv Docs <https://pypi.python.org/pypi/virtualenv/>`_
for getting started with virtualenv.

Create the virtualenv and activate the virtualenv you created.

.. code-block:: python

    $ sudo easy_install virtualenv  # to install virtualenv
    $ virtualenv foobar             # to create a virtualenv
    $ source foobar/bin/activate    # to activate the virtualenv
    $ deactivate                    # to deactivate the virtualenv

Now you can install tryton and trytond in your virtualenv by using pip
commands.
