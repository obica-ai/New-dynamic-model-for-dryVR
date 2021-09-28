Installation
============

Following installation instructions has been tested with Python 3.5 on Ubuntu 16.04 as well as Python 3.8 on Ubuntu 20.04.

.. code-block:: bash

    $ sudo apt-get install python3-pip python3-cairo python3-tk python3-pygraphviz libglpk-dev
    $ pip3 install --user --upgrade pip  # Upgrade pip first
    $ pip3 install --user -r requirements.txt


If you wish to install DryVR on other operation systems,
please make sure the following packages are correctly installed.

- Python 3.5 or above

  * Including `Python Tkinter <https://docs.python.org/3/library/tkinter.html>`_

- `Six <https://six.readthedocs.io/>`_
- `NumPy <https://numpy.org/>`_
- `SciPy <https://www.scipy.org/>`_
- `matplotlib <https://matplotlib.org/>`_
- `SymPy <https://www.sympy.org/en/index.html>`_
- `Python igraph <https://igraph.org/python/>`_
- `NetworkX <https://networkx.github.io/>`_
- `Z3 Python binding <https://pypi.org/project/z3-solver/>`_
- `pyglpk (now glpk) <https://pypi.org/project/glpk/>`_

  * May require installation of gmp and glpk

- `Pycairo <https://pycairo.readthedocs.io/en/latest/>`_
- `pygraphviz <https://pypi.org/project/pygraphviz/>`_

  * May require installation of graphviz
