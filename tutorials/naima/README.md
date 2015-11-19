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

* Clone this repository (http://github.com/gammapy/PyGamma15) to your computer
  (or do a `git pull` if you already had it cloned), and open an ipython notebook
  server in the directory `tutorials/naima`.

## Agenda

* Overview of the radiative models available in naima and walkthrough of their
  use
* Prepare and execute an MCMC run.
* Analyse the results of the run.

## Contributing

If you find something in `naima` that you would like to be different, or some
desired feature missing, do not hesitate to report it in the [issue
tracker](http://github.com/zblz/naima/issues) or code it yourself and do a PR
(contact me if you want help getting started with how naima works internally).
