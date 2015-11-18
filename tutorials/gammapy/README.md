# Tutorial - Getting started with Gammapy

* Presenter: [Johannes King](https://github.com/kingj90)
* Duration: 90 min
* Time: Wednesday, 16:00 - 17:30
* Location: Central seminar room

## Abstract

This is a tutorial on how to get started with Gammapy. It will follow mostly the [Gammapy documentation](https://gammapy.readthedocs.org/en/latest/).

You will take some simulated H.E.S.S. event lists and IRFs and run
a "classical" IACT source analysis, as described in [this](https://github.com/gammapy/2015-MPIK-Workshop/blob/gh-pages/talks/analysis-classical/README.md) talk on Monday.
:

1. Produce an image in a broad energy band, do detection and morphology analysis
2. Select an on and off region, produce a spectrum and fit a spectral model

If time allows, we'll take some Fermi-LAT high-energy data and make
a Galactic plane survey TS image, run a source detection method and
compare the result to the official 2FHL catalog.

Another possibility is to have a look in the code together and discuss how
contributions to Gammapy can be most efficiently.

## How to prepare

Install Gammapy 0.5 and Sherpa 4.7 in a fresh Python 2.7 anaconda environment with the following commands:

```
conda create -n gammapy python=2.7
source activate gammapy
conda config --add channels sherpa
conda install sherpa pyfits
conda install naima scipy matplotlib ipython-notebook cython click pyyaml wcsaxes
```

In order to
install the development version of Gammapy just clone [this git
repository](https://github.com/gammapy/gammapy) and install it by typing ``python
setup.py install``.

You can also clone the [gammapy-extra](https://github.com/gammapy/gammapy-extra) repository. It contains the example dataset that will be used in the tutorial.

## Agenda

- Make sure everyone has Gammapy installed ([docs](https://gammapy.readthedocs.org/en/latest/install.html))
- Basic examples showing functions and class in Gammapy ([docs](https://gammapy.readthedocs.org/en/latest/getting-started.html))
- Spectrum analysis using a command line tools ([docs](https://gammapy.readthedocs.org/en/latest/spectrum/index.html))
- Creating an image using a Gammapy example notebook

## Going further

If you'd like to learn more about Gammapy, head over to the official
[documentation](https://gammapy.readthedocs.org/en/latest/index.html),
which includes a link to the ICRC 2015 proceeding on the "About Gammapy"
page, as well as links to the code on Github, the mailing list,
and extensive documentation of what's already available.

Note that Gammapy is a very young project and there's many areas
where the features, implementation and documentation is work in progress.
So please have some patience and let us know where we should put our
priorities, or help out yourself and become a Gammapy co-developer.
