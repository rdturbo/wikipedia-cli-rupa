The Wikipedia Command Line Interface Python Project
===================================================

The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the Wikipedia CLI Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install wikipedia-cli-rupa


Usage
-----

Wikipedia CLI's usage looks like:

.. code-block:: console

   $ wikipedia-cli-rupa [OPTIONS]

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
