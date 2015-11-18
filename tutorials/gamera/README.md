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
    
Installation:

  $ git clone https://github.com/JoachimHahn/GAMERA.git
    
cd into directory, then run:

  $ make gappa
  
after that, cd in the lib/ directory:

  $ cd lib
  
now it gets a bit shitty  (Sorry!). You have to copy the ipython notebook to
your current directory (./lib/):
    
  $ cp /path/to/where/you/downloaded/it/gappa-tutorial.ipynb.

After that, run :

  & ipython notebook gappa-tutorial.ipynb

