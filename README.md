CDMATH
======

CDMATH is a geometrical and numerical toolbox designed for numerical analysts who work on the discretisation of partial differential equations on general shapes and meshes and who would rather focus on high-level scripting. The library originates from [CDMATH](http://cdmath.jimdo.com), a collaborative workgroup with the same name. It is based on the [MEDcoupling](https://docs.salome-platform.org/latest/dev/MEDCoupling/tutorial/index.html) C++/python library of the [SALOME](http://www.salome-platform.org/) project for the handling of meshes and fields, and on the C++ library [PETSC](https://www.mcs.anl.gov/petsc/) for the handling of matrices and linear solvers. The library currently developed for linux distributions and is maintained on Ubuntu 16.04 LTS and 18.04 LTS, as well as on Fedora 24, 25 and 26.

Examples of use
---------------
- [Examples of stable methods for the 1D linear transport equation](tests/doc/1DTransportEquation/RegularGrid/TransportEquation1D_RegularGrid.ipynb)
- [Example of unstable numerical methods for the 1D linear transport equation](tests/doc/1DTransportEquation/UnstableSchemes/TransportEquation1D_UnstableSchemes.ipynb)
- [Shock formation and numerical capture issues for the 1D Burgers' equations](tests/doc/1DBurgersEquation/BurgersEquation1D.ipynb)
- [Numerical convergence and maximum principle analysis for the linear finite element method applied to the 2D Poisson equation](tests/doc/2DPoissonEF/Convergence_Poisson_FE_SQUARE.ipynb)
- [Numerical convergence analysis for the finite volume method applied to the 2D Poisson equation](tests/doc/2DPoissonVF/Convergence_Poisson_FV5_SQUARE.ipynb)
- [Numerical convergence analysis for the finite volume method applied to a 2D anisotropic diffusion equation](tests/doc/2DDiffusionVF/Convergence_Diffusion_FV5_SQUARE.ipynb)
- [Influence of the mesh on the convergence and low Mach precision for the UPWIND finite volume method applied to the 2D wave system](tests/doc/2DWaveSystemVF_stationary/Convergence_WaveSystem_Upwind_SQUARE.ipynb)
- [Influence of the mesh on the convergence and low Mach precision  for the CENTERED finite volume method applied to the 2D wave system](tests/doc/2DWaveSystemVF_stationary/Convergence_WaveSystem_Centered_SQUARE.ipynb)
- [Influence of the mesh on the convergence and low Mach precision  for the STAGGERED finite volume method applied to the 2D wave system](tests/doc/2DWaveSystemVF_stationary/Convergence_WaveSystem_Staggered_SQUARE_squares.ipynb)
- [Influence of the mesh on the convergence and low Mach precision  for the PSEUDO-STAGGERED (colocated) finite volume method applied to the 2D wave system](tests/doc/2DWaveSystemVF_stationary/Convergence_WaveSystem_PStag_SQUARE.ipynb)

Download CDMATH sources to compile
----------------------------------

Create your source directory. For instance:
* `mkdir ~/workspace/cdmath`
* `cd ~/workspace/cdmath`

Download from GitHub. For instance:
* `wget https://github.com/ndjinga/CDMATH/archive/master.zip`

Then unzip the file to a directory cdmath-master
* `unzip master.zip`


Set environment for the compilation of CDMATH
---------------------------------------------
Dependencies. The following packages list is sufficient on Ubuntu 14.04, Ubuntu 16.04, Ubuntu 18.04 :

 - `cmake` (mandatory)
 - `g++` or another C++ compiler (mandatory)
 - `libhdf5-dev` (mandatory)
 - `python-dev`, `python-numpy` and `swig`, if you want to use CDMATH commands in yous Python scritps. Use the compilation option `-DCDMATH_WITH_PYTHON=ON`. (highly recommended)
 - `python-matplotlib` and `paraview` for postprocessing tools such as plotting curves (matplotlib) or generating 3D views (paraview). Use the compilation option `-DCDMATH_WITH_POSTPRO=ON` (recommended).
 - `petsc` if you want to solve large spase linear system. Typically required for implicit methods. Use the compilation option `-DCDMATH_WITH_DOCUMENTATION=ON` (recommended).
 - `jupyter`, in order to generate and visualise nice reports from test case simulations (optional)
 - `doxygen`, `graphviz` and `mscgen`, if you want to generate a nice source code documentation in `~/workspace/cdmath/cdmath_install/doc/`. Use the compilation option `-DCDMATH_WITH_PETSC=ON`. (optional)
 - `libcppunit-dev`, if you want to generate unit tests. Use the compilation option `-DCDMATH_WITH_TESTS=ON` (optional).
 - `libopenmpi-dev`, in particular if you need to use the compilation option `-DMEDFILE_USE_MPI=ON` (optional).
 - `rpm`, if you want to generate RPM installation packages. Use the compilation option `-DCDMATH_WITH_PACKAGE=ON` (optional).

Directories. Create the suggested build and installation folders:
* `cd ~/workspace/cdmath`
* `mkdir cdmath_build`
* `mkdir cdmath_install`
* `cd cdmath_build`


Compile and install CDMATH
--------------------------
Generate makefiles for a minimum version:
* `cmake ../cdmath-master/ -DCMAKE_INSTALL_PREFIX=../cdmath_install -DCMAKE_BUILD_TYPE=Release`

Or generate makefiles for an all-options version:
* `cmake ../cdmath-master -DCMAKE_INSTALL_PREFIX=../cdmath_install -DCMAKE_BUILD_TYPE=Release -G"Eclipse CDT4 - Unix Makefiles" -D_ECLIPSE_VERSION=4.3 -DMEDFILE_USE_MPI=ON -DCDMATH_WITH_PETSC=ON -DCDMATH_WITH_PYTHON=ON  -DCDMATH_WITH_POSTPRO=ON -DCDMATH_WITH_TESTS=ON -DCDMATH_WITH_DOCUMENTATION=ON -DCDMATH_WITH_PACKAGE=ON`

Compile and install:
* `make`
* `make install`

Run unit and example tests:
* make check

Run validation tests:
* make validation

Notes for compilation options:
* Eclipse: The Cmake options `-G"Eclipse CDT4 - Unix Makefiles" -D_ECLIPSE_VERSION=4.3` create project files if you want to develop CDMATH with Eclipse Kepler or higher.
* HDF5: On some systems (not Ubuntu 14.04 nor Ubuntu 16.04), you may have to use the compilation option `-DHDF5_ROOT_DIR=/path/to/hdf5/library` too.
* MPI: On some systems (not Ubuntu 14.04, nor Ubuntu 16.04), you may have to use the compilation option `-DMPI_ROOT_DIR=/path/to/mpi/library` too. You may also have to set the environment variable `export MPI_ROOT_DIR=/path/to/mpi/library`. Moreover, on some systems (not Ubuntu 14.04, nor Ubuntu 16.04), the compilation option `-DMEDFILE_USE_MPI=ON` may be mandatory and be set to `ON`.
* PETSc: If the library Petsc is already installed in your system (packages libpetsc-dev for ubuntu and petsc-devel for fedora 25 and 26), you may save time and disk space by using the installed library instead of installing a new one. In order to do so use the compilation options `-DPETSC_DIR=/path/to/petsc/installation/petsc -DPETSC_ARCH=arch-linux2-c-opt`. If you prefer to compile PETSc yourself from the sources you may follow the instructions given in [the official documentation](http://www.mcs.anl.gov/petsc/documentation/installation.html).

Use of CDMATH
-------------
We recommend using CDMATH in python scripts which avoids the hassle of having to edit Makefile files and compiling every C++ scripts.

To use CDMATH with your Python code, you can load the CDMATH environment in your terminal using the command
 * source `~/workspace/cdmath/cdmath_install/env_CDMATH.sh`
Then in your terminal simply type
- `python main.py `

If performance or parallelism is an issue for your simulations, you can use CDMATH librairies with your C++ code :
 * C++ libraries: `export LD_LIBRARY_PATH=~/workspace/cdmath/cdmath_install/lib`
 * To know how to include the right libraries for compilation, see the makefiles of the examples. They include the list `-linterpkernel -lmedC -lmedloader -lmedcoupling -lbase -lmesh -llinearsolver`.

The CDMATH environment variables consist in :
 * C++ libraries: `export LD_LIBRARY_PATH=~/workspace/cdmath/cdmath_install/lib`
 * Python libraries: `export PYTHONPATH=~/workspace/cdmath/cdmath_install/lib/cdmath:~/workspace/cdmath/cdmath_install/bin/cdmath`

Create Linux installation packages for CDMATH
---------------------------------------------
After popular request, here is how you can create packages for Debian and Red Hat-based Linux distributions:

1. Download CDMATH as explained hereabove.
2. Set the environment as explained hereabove (in particular, make sure you have `rpm` installed).
3. Generate a makefile with `cmake -DCMAKE_INSTALL_PREFIX=../cdmath_install -DCMAKE_BUILD_TYPE=Release -DCDMATH_WITH_PACKAGE=ON ../cdmath-master/` and eventually other options (documentation, tests, swig, etc).
4. Compile with `make package`.

You will then find a Debian package in the build directory; you may install it on Ubuntu 14.04 or Ubuntu 16.04. You will also find an RPM package, which you may install on Red Hat-based distributions. This way, the packages you generate may include all the compilation options you want.

Unfortunately, the Debian package may be said to be of “bad quality” for Debian standards as far as ownership is concerned. This is true and due to limitations in CMake/CPack. The package should still install nonetheless.
