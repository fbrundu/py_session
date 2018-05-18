==============
Python Session
==============


.. image:: https://img.shields.io/pypi/v/py_session.svg
        :target: https://pypi.python.org/pypi/py_session


Print session information


* Free software: MIT license


Features
--------

Installation:

.. code-block:: shell

    pip install py_session

Displays modules imported together with version:

.. code-block:: python

    >>> from py_session import py_session

    >>> py_session()

    re             	2.2.1         ipykernel      	4.8.2         json           	2.0.9
    IPython        	6.4.0         logging        	0.5.1.2       zlib           	1.0
    traitlets      	4.3.2         six            	1.11.0        ipython_genutils	0.2.0
    platform       	1.0.8         decorator      	4.3.0         argparse       	1.1
    pygments       	2.2.0         pexpect        	4.5.0         ptyprocess     	0.5.2
    ...


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
