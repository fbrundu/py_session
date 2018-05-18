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

Displays modules imported sorted, together with version:

.. code-block:: python

    >>> from py_session import py_session

    >>> py_session()

    69 modules found
    IPython             	6.4.0                   idna                	2.6                     prompt_toolkit      	1.0.15
    anndata             	0.6.1                   ipaddress           	1.0                     ptyprocess          	0.5.2
    appdirs             	1.4.3                   ipykernel           	4.8.2                   py_session          	0.1.1
    argparse            	1.1                     ipython_genutils    	0.2.0                   pygments            	2.2.0
    backcall            	0.1.0                   ipywidgets          	7.2.1                   pyparsing           	2.2.0
    bioservices         	1.5.2                   jedi                	0.12.0                  pytz                	2018.4
    bs4                 	4.6.0                   joblib              	0.11                    re                  	2.2.1
    ...


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
