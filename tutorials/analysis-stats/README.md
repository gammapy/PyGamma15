# Tutorial - Statistics for gamma-ray astronomy

* Presenter: [Michael Schmelling](michael-mpik)
* Duration: 90 min
* Time: Tuesday, 14:00 - 15:30
* Location: Central seminar room

## Abstract

This tutorial will extend the material presented at the [statistics
talk](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/talks/analysis-stats)
on Monday with a hands-on introduction and exercises.

Participants will be given some example data and implement their own
likelihood function as Python functions and perform statistical
analyses using [iminuit](http://iminuit.readthedocs.org/en/latest/).
and [emcee](http://dan.iel.fm/emcee/current/).

## How to prepare

To participate in this tutorial, you have to have a working scientific Python
installation (Python, IPython including notebook, iminuit, emcee and a few other
packages).

The full list of packages is given in the [setup-check.ipynb](https://github.com/gammapy/PyGamma15/blob/gh-pages/tutorials/analysis-stats/setup-check.ipynb)
IPython notebook and you can also use that to check that everything is working correctly:

    git clone https://github.com/gammapy/PyGamma15.git
    cd PyGamma15/tutorials/analysis-stats
    ipython notebook setup-check.ipynb

It doesn't matter if you use Python 2 or 3 for this tutorial,
everything will work the same.

## Tutorial

Open up the  [Tutorial.ipynb](https://github.com/gammapy/PyGamma15/blob/gh-pages/tutorials/analysis-stats/Tutorial.ipynb) IPython notebook and follow along with the instructions, coding exercises.

A full solution is given in [TutorialSolution.ipynb](https://github.com/gammapy/PyGamma15/blob/gh-pages/tutorials/analysis-stats/TutorialSolution.ipynb).
This was handed out after the tutorial.
If you're reviewing this at a later time, suggest you try implementing this yourself and not just look at the solution!

While preparing this tutorial we discussed several options what to use as an example.
We didn't flesh this out, but one idea was this [spectrum_chi2](https://github.com/gammapy/PyGamma15/blob/gh-pages/tutorials/analysis-stats/spectrum_chi2.ipynb)
example, which we keep here in case it's useful as extra material or for future tutorials.
