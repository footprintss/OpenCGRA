<pre>
==========================================

  ____                _____________  ___ 
 / __ \___  ___ ___  / ___/ ___/ _ \/ _ |
/ /_/ / _ \/ -_) _ \/ /__/ (_ / , _/ __ |
\____/ .__/\__/_//_/\___/\___/_/|_/_/ |_|
    /_/                                  

==========================================
</pre>
[![Build Status](https://travis-ci.com/pnnl/OpenCGRA.svg?token=yazoBFLC1ynpzdD4wAEP&branch=master)](https://travis-ci.com/github/pnnl/OpenCGRA)

OpenCGRA is a parameterizable and powerful CGRA (Coarse-Grained Reconfigurable Arrays) generator to generate synthesizable Verilog for different CGRAs based on user-specified configurations (e.g., CGRA size, type of the computing units in each tile, communication connection, etc.). OpenCGRA uses modular design and standardized interfaces between modules. The configurability and extensibility are maximized by its parametrization system to fit in various research and industrial needs.


Related publications
--------------------------------------------------------------------------

- Cheng Tan, et al. _“AURORA: Automated Refinement of Coarse-Grained Reconfigurable Accelerators.”_ The 2021 Design, Automation & Test in Europe Conference, Grenoble, France. (DATE-21) February 1-5, 2021.
- Cheng Tan, et al. _"ARENA: Asynchronous Reconfigurable Accelerator Ring to Enable Data-Centric Parallel Computing."_ IEEE Transactions on Parallel and Distributed Systems (TPDS-21).
- Cheng Tan, et al. _"OpenCGRA: An Open-Source Framework for Modeling, Testing, and Evaluating CGRAs."_ The 38th IEEE International Conference on Computer Design. (ICCD-20), Oct 2020.


License
--------------------------------------------------------------------------

OpenCGRA is offered under the terms of the Open Source Initiative BSD 3-Clause License. More information about this license can be found here:

  - http://choosealicense.com/licenses/bsd-3-clause
  - http://opensource.org/licenses/BSD-3-Clause


Installation
--------------------------------------------------------

OpenCGRA requires Python3.7 and has the following additional prerequisites:

 - graphviz, verilator
 - git, Python headers, and libffi
 - virtualenv
 - PyMTL3

The steps for installing these prerequisites and OpenCGRA on a fresh Ubuntu
distribution are shown below. They have been tested with Ubuntu Trusty
14.04.

### Install python3

```
 % sudo apt-get install python3.7
```

### Install graphviz

```
 % sudo apt-get install -y graphviz
```

### Install Verilator

[Verilator][4] is an open-source toolchain for compiling Verilog RTL
models into C++ simulators. OpenCGRA uses Verilator for Verilog import.

```
 $ sudo apt-get install git make autoconf g++ libfl-dev bison
 $ mkdir -p ${HOME}/src
 $ cd ${HOME}/src
 $ wget http://www.veripool.org/ftp/verilator-4.036.tgz
 $ tar -xzvf verilator-4.036.tgz
 $ cd verilator-4.036
 $ ./configure
 $ make
 $ sudo make install
```

 [4]: http://www.veripool.org/wiki/verilator

### Install git, Python headers, and libffi

We need to install the Python headers and libffi in order to be able to
install the cffi Python package. cffi provides an elegant way to call C
functions from Python, and PyMTL uses cffi to call C code generated by
Verilator. We will use git to grab the PyMTL source. The following
commands will install the appropriate packages:

```
 % sudo apt-get install git python-dev libffi-dev
```

### Create virtual environment

While not strictly necessary, we strongly recommend using [virtualenv][5]
to install PyMTL3 and the Python packages that PyMTL3 depends on.
virtualenv enables creating isolated Python environments. The following
commands will create and activate the virtual environment:

```
 % python3 -m venv ${HOME}/venv
 % source ${HOME}/venv/bin/activate
```

 [5]: https://virtualenv.pypa.io/en/latest/

### Install PyMTL3 and Python requirements

```
 % pip install git+https://github.com/tancheng/pymtl3.git
 % pip install --upgrade pip setuptools twine
 % pip install hypothesis
 % pip list
```

### Clone OpenCGRA repo

We can now use git to clone the OpenCGRA repo.

```
 % mkdir -p ${HOME}/cgra
 % cd ${HOME}/cgra
 % git clone https://github.com/pnnl/OpenCGRA.git
```

When you're done testing/developing, you can deactivate the virtualenv::

```
 % deactivate
```
