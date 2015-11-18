# Tutorial - SED modeling with Naima

* Presenter: [Victor Zabalza](https://github.com/zblz)
* Duration: 90 min
* Time: Thursday, 11:00 - 12:30
* Location: Central seminar room

## Abstract

During this tutorial we will carry out the analysis of one or two non-thermal
sources and infer the particle distribution and environment parameters from
their spectra.

## How to prepare

* Go over the slides from the [SED modeling with Naima
  talk](https://github.com/gammapy/PyGamma15/tree/gh-pages/talks/naima) from
  Monday and the references given there.

* Install naima following the instructions [in the naima
  docs](http://naima.readthedocs.org/en/latest/installation.html).

To install in a conda enviroment (Python 2 or 3), do as follows (first line
might not be necessary if you did it yesterday):

```bash
conda config --add channels astropy
conda install naima ipywidgets
pip install triangle_plot corner
```


## Agenda

* Overview of the radiative models available in naima and walkthrough of their
  use
* Prepare and execute an MCMC run.
* Analyse the results of the run.
