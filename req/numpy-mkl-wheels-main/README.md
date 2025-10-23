# Wheels for Python on Windows, linked to oneAPI MKL

This repository provides unofficial binary wheels for open-source extension packages for Python on Windows, linked to the [Intel(r) oneAPI Math Kernel Library](https://software.intel.com/en-us/intel-mkl/) (oneAPI MKL).

The files are unofficial (meaning: informal, unrecognized, personal, unsupported, no warranty, no liability, provided "as is") and made available for testing and evaluation purposes.

Source code changes, if any, have been submitted to the project maintainers or are included in the wheels.

The wheels can be downloaded from the [Releases](https://github.com/cgohlke/numpy-mkl-wheels/releases) page.

## Release 2025.9.14

Linked to oneAPI MKL 2025.2 (64-bit) and 2024.2 (32-bit).

Depends on the latest
[Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist)
and the
[mkl](https://pypi.org/project/mkl/),
[intel-openmp](https://pypi.org/project/intel-openmp/), and
[intel-fortran-rt](https://pypi.org/project/intel-fortran-rt/) packages.

- [numpy](https://github.com/numpy/numpy) 2.3.3
- [scipy](https://github.com/scipy/scipy) 1.16.2
- [numexpr](https://github.com/pydata/numexpr) 2.12.1
- [mkl_fft](https://github.com/IntelPython/mkl_fft) 2.0.0
- [mkl_random](https://github.com/IntelPython/mkl_random) 1.2.10
- [mkl_service](https://github.com/IntelPython/mkl-service) 2.5.2

## Build system

- Windows 11 Pro
- [Visual Studio](https://visualstudio.microsoft.com/vs/community/) 2022 Community 17.14
- [Intel oneAPI Base and HPC Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.miarqe) 2025.2 (64-bit) and 2024.2 (32-bit and ifort)
- [LLVM](https://github.com/llvm/llvm-project/releases) 20.1.8
- [CPython](https://www.python.org/downloads/windows/) 3.11, 3.12, 3.13, 3.14

## Alternatives

Binaries for Python packages linked to the oneAPI MKL are also available as part of the [Intel(r) Distribution for Python](https://www.intel.com/content/www/us/en/developer/tools/oneapi/distribution-for-python.html) and the [MKL-accelerated NumPy and SciPy wheels](https://github.com/urob/numpy-mkl) repository.
