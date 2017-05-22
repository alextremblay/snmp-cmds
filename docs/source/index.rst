.. our "home page" will be the entire contents of the README from the project root, plus the TOC and other Sphinx directives

.. include:: README.rst

.. during the "make" process, we stripped the .. _Doc: reference from our
.. README.rst file so we can add it in here:

For more information on the commands see :doc:`Commands <commands>`.
For more information on the API see :doc:`API <API>`.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   API
   commands
   exceptions
   helpers



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
