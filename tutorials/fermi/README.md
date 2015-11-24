# Tutorial - Fermi-LAT data analysis

* Presenter: Matthew Wood and Jeremy Perkins
* Duration: 75 min
* Time: Wednesday, 9:15 - 10:30
* Location: Central seminar room

## Abstract

This tutorial teaches you to run Fermi-LAT Pass 8 data analyses
via the [Fermi ScienceTools](http://fermi.gsfc.nasa.gov/ssc/data/analysis/)
and [FermiPy](https://github.com/fermiPy/fermipy).

## How to prepare

Install the Fermi STs as described [here](http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/).  It is recommended to use the binary STs distribution.  Here are the respective tarballs for OSX and Scientific Linux distributions of STs v10-00-05 (the currently recommended release for Pass 8 analysis):

*Scientific Linux*: [ScienceTools-v10r0p5-fssc-20150518-x86_64-unknown-linux-gnu-libc2.12A.tar.gz](http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/tar/ScienceTools-v10r0p5-fssc-20150518-x86_64-unknown-linux-gnu-libc2.12A.tar.gz)

*OSX*: [ScienceTools-v10r0p5-fssc-patch-20150518-x86_64-apple-darwin14.4.0-without-root.tar.gz](http://fermi.gsfc.nasa.gov/ssc/data/analysis/software/tar/ScienceTools-v10r0p5-fssc-patch-20150518-x86_64-apple-darwin14.4.0-without-root.tar.gz)

Then follow the fermipy installation instructions on this [page](http://fermipy.readthedocs.org/en/latest/install.html).  Note that fermipy and the Fermi STs can only be used with the python distribution that comes packaged with the STs and cannot be used with an existing python distribution (e.g. anaconda python).

As part of the installation process you will clone the fermipy git repository which contains the notebooks for this tutorial.  You can launch any of the notebooks by going to the notebooks directory and executing `ipython notebook` followed by the notebook name:

```bash
cd notebooks # From root directory of fermipy git repo
ipython notebook PG\ 1553+113.ipynb
```

It is recommended to begin first with the PG1553 notebook.

## Agenda

- Review some basic aspects of the fermipy package (configuration management, etc.).
- Run a basic analysis of PG1553.  
- Cover some more advanced analysis examples: spatial extension fitting and bin-by-bin likelihoods.

## Going further

Additional documentation on running LAT analysis is available in the
[FSSC pages](http://fermi.gsfc.nasa.gov/ssc/data/analysis/).


