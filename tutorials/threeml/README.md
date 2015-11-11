# Tutorial - How to analyze multi-mission data using 3ML

* Presenter: [Luigi Tibaldo](https://github.com/tibaldo)
* Duration: 90 min
* Time: Tuesday, 16:00 - 17:30
* Location: Central seminar room

## Abstract

This is a tutorial on how to get started with 3ML as a user to perform
joint analysis of data from multiple instruments.
The concept of 3ML will be covered in the
[previous talk](https://github.com/gammapy/PyGamma15/tree/gh-pages/talks/threeml/README.md)
on Monday.

## How to prepare

To run the tutorial you will need to install
* the [Fermi ScienceTools](http://fermi.gsfc.nasa.gov/ssc/data/analysis/)
* [3ML](https://github.com/giacomov/3ML)
* Jupyter notebook/ipython notebook

The installation of 3ML requires as prerequisites:
* numpy and scipy
* the [Boost libraries](http://www.boost.org/) with python bindings
* the [ROOT analysis framework](https://root.cern.ch/)
Once you have installed them download
[3ML](https://github.com/giacomov/3ML) and look at the setup.py help
to get started. If you have trouble with the installation contact
[Luigi Tibaldo](https://github.com/tibaldo) or
[Giacomo Vianello](https://github.com/giacomov).

TODO: add zipped folder with tutorial notebook; how to check if you
are ready for the tutorial.

## Agenda

We will analyze jointly Fermi LAT and Swift XRT observations of the
gamma-ray burst GRB090510. We will go through the following steps
* Data specification
* Definition of likelihhod model
* Fit using Minuit and inspection of results
* Definition of custom models
* Bayesian analysis

## Going further

Note also that 3ML is a very young project and there are many areas
where the features, implementation and documentation is work in progress.
So please have some patience and let us know where we should put our
priorities. We can also discuss possible contributions if you want to
become a co-developer.
