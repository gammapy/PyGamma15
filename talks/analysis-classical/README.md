# Talk - Classical Cherenkov telescope data analysis

* Presenter: [Regis Terrier](https://github.com/registerrier)
* Duration: 20 + 5 min

## Abstract

Cherenkov telescope data consists of events with reconstructed sky position
(e.g. in equatorial coordinates RA / DEC) and event energy.

The classical Cherenkov telescope data analysis method (i.e. the one used for
almost all papers published so far) is a two-step procedure. First perform
source detection and position / morphology measurements on 2-dimensional images
using all events from a broad energy band. Then choose a sky region (e.g. a
circle centered on the best-fit source position) and analyse the 1-dimensional
event energy distribution to measure the source spectrum. This is similar to the
methods from X-ray astronomy and some of the tools (e.g. XSPEC, Sherpa) and file
formats (OGIP, FITS) have been adopted for VHE gamma-ray astronomy.

This talk will introduce the methods in detail and explain the specificities of
Cherenkov telescope data analysis (e.g. background estimation, multiple
observations, safe energy threshold).

A hands-on introduction to classical VHE gamma-ray analysis will be given
in the "Getting started with Gammapy" tutorial later in the week.

## Outline

* Classical analysis overview (event list, images, spectra)
* Image analysis:
  * Counts images. Sky and pixel coordinates (FITS WCS standard)
  * Exposure images
  * Background modeling
  * PSF convolution
  * Source modeling and likelihood fitting (cash statistic)
* Spectral analysis:
  * Region selection (on and off regions)
  * Counts spectra (PHA OGIP file format)
  * Effective area (ARF OGIP file format)
  * Energy resolution (RMF OGIP file format)
  * Safe energy threshold
  * Source modeling, forward folding, profile likelihood fitting (wstat statistic)
* Methods to handle multiple observations:
  * Stacking observations (IRF and background averaging)
  * Joint modeling of observations (add likelihoods)
* Status and plans of tools: suggestions what to work on this week

## References

* [OGIP format description](https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/node5.html)
* [XSPEC documentation](https://heasarc.gsfc.nasa.gov/xanadu/xspec/)
* [Fitting spectra with sherpa](http://cxc.harvard.edu/sherpa/threads/pha_intro/)
* [Piron (2001), Profile likelihood applied to gamma-ray spectral analysis](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2001A%26A...374..895P/)
* [Berge (2007) "Background modelling in VHE gamma-ray astronomy"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2007A%26A...466.1219B/)

## See also

* [Talk - Bias in spectral likelihood estimators and observation grouping](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/talks/analysis-bias)
* [Talk - 3D cube analysis for Cherenkov telescopes](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/talks/analysis-cube)
* [Tutorial: Getting started with Gammapy](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/gammapy)
