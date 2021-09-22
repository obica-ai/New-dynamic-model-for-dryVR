DryVR 2.0 is a software tool for verifying cyber-physical and autonomoous systems. A key feature of DryVR is that it supports reachability analysis of _gray-box_ systems, that is, systems that are described in part as a white box transition system or a program and in part as a black-box simulator as shown in the figure below.

<img src="https://gitlab.engr.illinois.edu/dryvrgroup/dryvrtool/-/blob/master/figures/dryvrmodel.png"
    style="float: left; margin-right: 10px;" />

Please note that there are three branches: master: it is based on Python 2.7 and supports hybrid models; symmetries: it is the modification of the master branch created to support symmetry-based acceleration for reachtube computations created for this ATVA 2019 paper: "Using symmetry transformations in equivariant dynamical systems for their safety verification" by Hussein Sibai, Navid Mokhlesi, and Sayan Mitra, however it does not support hybrid models; dryvr3: it is a Python 3.6 version of the master branch which support all features of DryVR 2.0.

Please find the documentation at 

http://dryvr-02.readthedocs.io/en/latest/


Installation
==================
Following installation instructions has been tested with Python 2.7.12 on
Ubuntu 16.04.

Install System dependencies:

```bash
$ sudo apt-get install python-pip python-cairo python-tk python-pygraphviz \
    libglpk-dev
```

Install PyPi dependencies using `pip`:
```bash
$ pip2 install --user --upgrade pip  # Upgrade pip first
$ pip2 install --user glpk networkx python-igraph matplotlib numpy scipy \
    sympy z3-solver six
```

For Python 3.5 or above on Ubuntu 16.04, try the following instructions.

```bash
$ sudo apt-get install python3-pip python3-cairo python3-tk python3-pygraphviz \
    libglpk-dev
$ pip3 install --user --upgrade pip  # Upgrade pip first
$ pip3 install --user -r requirements.txt
```

If using Python 3 `venv` virtual environment on Ubuntu 16.04, try the following instructions.
```bash
$ sudo apt-get install python3-pip libcairo2-dev libgraphviz-dev libglpk-dev
$ pip3 install --upgrade pip  # Upgrade pip first
$ pip3 install -r requirements.txt
```

Quick Start
==================
To run verification examples, please run 

```bash
python main.py input/[input_file]
```

for example:

```bash
python main.py input/daginput/input_thermo.json
```

The examples descriptions can be found in the documentation. Please note that as the verification algorithm uses probabilistic method, the verification result may vary for different runs.


To run controller synthesis, please run:
------------------------------------------------------------
python graphSearch.py input/[input_file]

for example:

python graphSearch.py input/rrtinput/mazefinder.json

