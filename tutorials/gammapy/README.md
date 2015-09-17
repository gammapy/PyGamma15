# Tutorial - Getting started with Gammapy

* Presenter: [Axel Donath](https://github.com/adonath) and [Johannes King](https://github.com/kingj90)
* Duration: 90 min
* Time: Tuesday, 11:00 - 12:30
* Location: Central seminar room

## Abstract

This is a tutorial on how to get started with Gammapy as a user.
How to contribute to Gammapy will be covered in [a different tutorial](https://github.com/gammapy/2015-MPIK-Workshop/blob/gh-pages/tutorials/contributing/README.md).

You will take some simulated H.E.S.S. event lists and IRFs and run
a "classical" IACT source analysis:

1. Produce an image in a broad energy band, do detection and morphology analysis
   (as described in [this](https://github.com/gammapy/2015-MPIK-Workshop/blob/gh-pages/talks/analysis-image/README.md) talk on Monday).
2. Select an on and off region, produce a spectrum and fit a spectral model
   (as described in [this](https://github.com/gammapy/2015-MPIK-Workshop/blob/gh-pages/talks/analysis-spec/README.md) talk on Monday).

If time allows, we'll take some Fermi-LAT high-energy data and make
a Galactic plane survey TS image, run a source detection method and
compare the result to the official 2FHL catalog.

## How to prepare

Install Gammapy 0.5 and Sherpa 4.7 (TODO: do we need the dev version?) using Python 2.7 as described [here](https://gammapy.readthedocs.org/en/latest/install.html#id1).

Download example data: TODO

Run the `tutorial-setup-check.py` script (TODO: implement) to check if you have everything you need for the tutorial.

## Agenda

TODO: Add the tutorials to the official Gammapy docs, then just
add links here.

- Get everyone set up and run one command-line tool and Python command.
- HESS image analysis
- HESS spectrum analysis
- Fermi-LAT make survey image, source list and compare to 2FHL

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
