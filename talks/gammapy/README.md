# Talk - Astropy, Sherpa, Gammapy

* Presenter: [Axel Donath](https://github.com/adonath/)
* Duration: 20 + 5 min

## Abstract

The [Astropy project](http://www.astropy.org/) is a community effort to develop
a single core package for Astronomy in Python and foster interoperability
between Python astronomy packages.

[Sherpa](http://cxc.harvard.edu/sherpa/) is a Python modeling and fitting package.
It enables the user to construct complex models from simple definitions and fit
those models to data, using a variety of statistics and optimization methods.

[Gammapy](https://gammapy.readthedocs.org/en/latest/index.html) is a
community-developed, open-source Python package for gamma-ray astronomy. It is
an in-development affiliated package of Astropy that builds on the core
scientific Python stack as well as Astropy and Sherpa to provide tools to
simulate and analyse the gamma-ray sky for telescopes such as CTA, H.E.S.S.,
VERITAS, MAGIC, HAWC and Fermi-LAT.

This presentation will give an overview of Astropy, Sherpa and Gammapy and
discuss the status (the recent Gammapy 0.5 release) and plans for Gammapy.
A hands-on tutorial "Getting started with Gammapy" will be given later in the week.

## Outline

* Overview Astropy core packages (fits, table, wcs, time, coordinates, modeling).
* Overview of some relevant Astropy affiliated packages
* Overview Sherpa
* Gammapy overview, status, scope
* Gammapy next steps and goals:
  * improve Gammapy quality (code, tests, docs), Sherpa and Naima integration
  * cube and multi-mission analysis (e.g. Fermi-LAT and IACT)
  * 1.0 release, paper
* What can we work on  / achieve this week?

## References

### Astropy

* Astropy [website](http://www.astropy.org/), [code](https://github.com/astropy/astropy), [docs](http://astropy.readthedocs.org/en/latest/)

### Sherpa

* [Scipy 2009 proceeding: "Sherpa: 1D/2D modeling and fitting in Python"](http://conference.scipy.org/proceedings/scipy2009/paper_8/full_text.pdf)
* [Scipy 2011 proceeding: "Fitting and Estimating Parameter Confidence Limits with Sherpa"](http://conference.scipy.org/proceedings/scipy2011/pdfs/brefsdal.pdf)
* [Python for astronomers tutorial section on fitting uses Sherpa](http://python4astronomers.github.io/fitting/fitting.html)
* [Sherpa Quick Start IPython notebook](https://github.com/sherpa/sherpa/blob/master/docs/SherpaQuickStart.ipynb)
and [Doug Burke's notebooks](https://github.com/DougBurke/sherpa-standalone-notebooks)
* There's a lot of [Sherpa analysis threads](http://cxc.harvard.edu/sherpa/threads/index.html).
  They mostly use Chandra X-ray data, but are still very useful for gamma-ray astronomers,
  because gamma-ray data analysis is similar.
* [Sherpa code on Github](https://github.com/sherpa/sherpa)

### Gammapy

* [Gammapy code on Github](https://github.com/gammapy/gammapy) and [Gammapy docs](https://gammapy.readthedocs.org/en/latest/)
* [Gammapy ICRC 2015 proceeding](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015arXiv150907408D/)


## See also

* [Tutorial - Getting started with Gammapy](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/gammapy)
