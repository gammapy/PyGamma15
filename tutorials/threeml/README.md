# Tutorial - How to analyze multi-mission data using 3ML

* Presenter: [Luigi Tibaldo](https://github.com/tibaldo)
* Duration: 90 min
* Time: Wednesday, 11:00 - 12:30
* Location: Multimedia room

## Abstract

This is a tutorial on how to get started with 3ML as a user to perform
joint analysis of data from multiple instruments.
The concept of 3ML will be covered in the
[previous talk](https://github.com/gammapy/PyGamma15/tree/gh-pages/talks/threeml/README.md)
on Monday. At the end we can also discuss possibilities if you are
interested to contribute to code development.

## How to prepare

The installation of the software required for the tutorial may be time
consuming. If you want to be able to interactively
participate to the tutorial you are advised to start setting up your machine well in advance.

To run the tutorial you will need to install
* the [Fermi ScienceTools](http://fermi.gsfc.nasa.gov/ssc/data/analysis/)
* [3ML](https://github.com/giacomov/3ML)
* Jupyter notebook/ipython notebook

The installation of 3ML requires as prerequisites:
* numpy, scipy, and astropy
* the [Boost libraries](http://www.boost.org/) with python bindings
* <strike>the [ROOT analysis framework](https://root.cern.ch/), including
  Minuit2 (note that Minuit2 is not activated by default in all ROOT
  distributions).</strike> (the latest version of 3ML is ROOT free!)

Once you have installed the prerequisites, download the
[3ML](https://github.com/giacomov/3ML) software and look at the setup.py help
to get started. For compatibility we recommend to install 3ML for the
python distributed with the Fermi Science Tools. If you have trouble with the installation contact
<a href="mailto:luigi.tibaldo@mpi-hd.mpg.de">Luigi Tibaldo</a> or
<a href="mailto:giacomov@stanford.edu">Giacomo Vianello</a>.

Now, <a href="GRB090510.tar.gz" download>download</a> the
tarball that contains the ipython notebook and the data for the
tutorial. Open the notebook "joint\_xrt\_lat.ipynb". Run the first
code block. Do you get only a warning saying that HAWC
software is not available on your machine? Congratulations! You are
ready for the interactive tutorial.

If you don't have time or do not manage to install all the software,
you are still welcome to participate: a large part of the tutorial
will be a demo of a user case for 3ML.

Optional: in the tutorial you will deal with an instrument and data format that
are not going to be covered in detail, if at all, in the previous
days. We will go through some preliminary information at the beginning of the
session, but if you want to read some material in advance 
* get familiar with the [Swift mission](http://swift.gsfc.nasa.gov/)
and [XRT instrument](http://https://www.swift.psu.edu/xrt/)
* learn about the [OGIP spectral file format](https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/ogip_92_007.html), a data format shared by many X-ray telescopes. 

## Agenda

First we will go through a user case with 3ML. We will analyze jointly Fermi LAT and Swift XRT observations of the
gamma-ray burst GRB090510. We will go through the following steps
* Data specification
* Definition of likelihood model
* Fit using Minuit and inspection of results
* Definition of custom models
* Bayesian analysis

Later if there is interest we can walk through the
[3ML repository](https://github.com/giacomov/3ML), discuss details of
the code and areas that we need help to develop.

## Going further

Note that 3ML is a very young project and there are many areas
where the features, implementation and documentation is work in progress.
So please have some patience and let us know where we should put our
priorities. We can also discuss possible contributions if you want to
become a co-developer.
