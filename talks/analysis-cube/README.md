# Talk - 3D cube analysis for Cherenkov telescopes

* Presenter: [Peter Eger](https://github.com/peger089)
* Duration: 15 + 5 min

## Abstract

The classical Cherenkov telescope data analysis method consists of detection
and morphology characterisation on 2D images, followed by spectral analysis
using a 1D counts vector as a function of energy in a given sky region
(see talk by Regis Terrier).

A potentially better way to analyse the data is to use 3D cubes
(with longitude, latitude and energy axis) and simultaneous morphology and
spectral modeling as is common already for Fermi-LAT data.

This talk will explain 3D analysis for Cherenkov telescopes and summarise
the status and plan to implement this method in open-source analysis codes.

## Outline

* Advantages over established analysis methods (1D + 2D) for IACTs
* Differences and similarities to the Fermi-LAT analysis scheme
* Background modeling
* Spatially and energy-dependent instrument response
* Binned vs. unbinned analysis
* Already implemented in [GammaLib](http://cta.irap.omp.eu/gammalib-devel/) and [ctools](http://cta.irap.omp.eu/ctools-devel/)
* Plan to implement this in [Gammapy](https://gammapy.readthedocs.org/en/latest/) using [Sherpa](http://cxc.harvard.edu/sherpa/)

## References

These tutorials are examples what's involved in doing a 3D cube binned
likelihood analysis:

* http://fermi.gsfc.nasa.gov/ssc/data/analysis/scitools/binned_likelihood_tutorial.html
* http://cta.irap.omp.eu/ctools/user_manual/
