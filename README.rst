Flake8-For-Pycharm
==================

This is a plugin for Flake8 that will emulate pylint json output.

Installation
------------

.. code-block:: bash

    pip install flake8-for-pycharm

flake8 will be automaitcally installed in the same enviroment.
To validate installation run `flake8_pycharm.py --help-msg=E1101`.
Output should look like that:

.. code-block::

    :no-member (E1101): *%s %r has no %r member%s*
    Used when a variable is accessed for an unexistent member. This message
    belongs to the typecheck checker.

pylint will also be installed because pycharm plugin refuses to work if it's not installed.

Usage
-----
1. Locate the file `flake8_pycharm.py` in your python environment (in linux use command `which flake8_pycharm.py`)
2. In Pycharm go to File -> Settings -> Pylint (If you can't find it, go to Settings -> Plugins and install pylint plugin)
3. In "Path to Pylint executable", provide path to "flake8_pycharm.py" script
4. [ *Optional* ] In path to pylintrc, provide path to your flake8 configuration file
5. Do not put anything in the "Arguments" field or script won't work.
6. This is it, youa re basically done.

How does it work?
-----------------

Initially Pycharm call pylint with the following arguments

.. code-block:: bash

    pylint --help-msg=E1101

Once this command has succeeded, it assumes that pylint is installed and starts using it with command like that.

.. code-block:: bash

    pylint --rcfile=pylintrc -f json my_file.py

The `flake8_pycharm.py` script understand those pylint arguments,
query flake8 accordingly and return result in same format that pylint produces.

Troubleshooting
---------------

If you did everything correctly but pycharm kept complaining about pylint being not installed, you might have to install it anyway.
It's a bug reported by a colleague but I wasn't able to reproduce it locallay.

If you received errors from pycharm, you can try to run the command manually to see if it's producing errors.

.. code-block:: bash

    flake8_pycharm.py --rcfile=<your flake8 configuration> -f json my_file.py
