# Tutorial - Astrophysical modeling with Gamera

* Presenter: [Joachim Hahn](https://github.com/JoachimHahn)
* Duration: 75 min
* Time: Thursday, 9:15 - 10:30
* Location: Central seminar room

## Abstract

In this tutorial you will learn step-by-step to use gappa in order to
 * calculate an SED from a particle distribution
 * perform a particle evolution in the presence of energy losses
 * calculate some galactic gas densities
 * tinker with the galactic spiral arm structure
 * dice some random galactic pulsar positions

## How to prepare

Installation preparation:

**on Ubuntu**

using apt:

    $ sudo apt-get install libgsl0ldbl libgsl0-dev python-dev swig
    
**on MacOS**
using e.g. homebrew:

    $ brew install gsl swig
    
Installation of GAMERA and the gammapy Python interface:

    $ git clone https://github.com/JoachimHahn/GAMERA.git
    $ cd GAMERA
    $ make gappa

The GAMERA / gammapy build system doesn't have "install" implemented yet.
For now you should start Python from the `lib` directory and then you should be able to import `gappa`

    $ cd lib
    $ python -c 'import gappa'
  
To start the tutorial IPython notebook do this in the `lib` directory:

    $ wget https://github.com/gammapy/PyGamma15/raw/gh-pages/tutorials/gamera/gappa-tutorial.ipynb
    $ ipython notebook gappa-tutorial.ipynb

