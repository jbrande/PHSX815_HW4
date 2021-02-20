# PHSX815 Spring 2021 Week 2

## Random Sampling I, Sorting, and Confidence Intervals

This repository contains severeal types of programs:

- `CoinToss.x` [C++] and `python/CoinToss.py` [Python]
- `CoinAnalysis.x` [C++] and `python/CoinAnalysis.py` [Python]
- `CookieTimer.x` [C++] and `python/CookieTimer.py` [Python]
- `CookieAnalysis.x` [C++] and `python/CookieAnalysis.py` [Python]

### Requirements

The Python code requires the `numpy` and `matplotlib` packages to be
installed (see [matplotlib](https://matplotlib.org/) documentation).

In order to compile (by typing `make`) and run the C++ examples, two
different external packages are required:
- [matplotlib](https://matplotlib-cpp.readthedocs.io/en/latest/
) (C++)
- [ROOT](https://root.cern/) (C++)
If you are missing either of these packages you must remove the
dependencies (and any executables that need them) from your `Makefile`
- `CoinAnalysis.x` requires [matplotlib](https://matplotlib-cpp.readthedocs.io/en/latest/
)
- `CookieAnalysis.x` requires [ROOT](https://root.cern/)

### Usage

All of the executables (and Python programs) can be called from the
command line with the `-h` or `--help` flag, which will print the options
