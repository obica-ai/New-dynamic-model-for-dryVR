Installation
============

Following installation instructions has been tested with Python 2.7.12 on
Ubuntu 16.04.

.. code-block:: bash

    $ sudo apt install python-pip python-cairo python-tk python-pygraphviz \
        libglpk-dev
    $ pip2 install --user --upgrade pip
    $ pip2 install --user glpk networkx python-igraph matplotlib numpy scipy \
        sympy z3-solver


If you wish to install DryVR on other operation systems,
please make sure the following packages are correctly installed.

- Python 2.7

  * Including `Python Tkinter <https://docs.python.org/2.7/library/tk.html>`_

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
