# PHSX815 Spring 2021 Week 2

## Yoni edits for HW 4
Editing CookieAnalysis.py to plot quantiles over histograms of analyzed cookie eating data.
CookieAnalysis.py now takes three new arguments:

-f (required) specifies the input filename

-n (optional) specifies the number of quantiles (default 1)

-scale (optional) if this is "log", the plot y-axis will be log scaled. if it is not present, or not "log", the plot y-axis will be scaled normally.

The program saves the plot in the main directory as "analysis.jpg".


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
