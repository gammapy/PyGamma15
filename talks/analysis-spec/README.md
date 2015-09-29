# Talk - 1D spectrum analysis in regions (like XSPEC)

* Presenter: [Regis Terrier](https://github.com/registerrier)
* Duration: 15 + 5 min

## Abstract

The issues and methods of spectral analysis are very similar in different domains of high energy astrophysics.   In particular, analyses of X-ray and VHE gamma-rays spectra share many characteristics: forward-folding methods,  Poisson signal and background etc. Extensive software packages have been developped for X-rays astrophysics (e.g. XPSEC, sherpa)  which can provide effective tools for spectral analysis of VHE  data. We will discuss how  this can be practically done. We will review the specificities of VHE spectral analysis (signal to noise level,  multiple observations, background estimation, profile likelihood methods  etc)  and show how this can be  implmented.

## Outline
* region-based analysis (sky vs. pixel regions, reflected regions)
* Likelihood (cash statistic) and  profile likelihood (wstat)
* OGIP file formats: PHA, ARF and RMF
* methods to handle multiple observations:
  * stacking observations (IRF aand background veraging)
  * joint modeling of observations (add likelihoods)
* Status and plans of tools: suggestions what to work on this week

## References
[OGIP format description](https://heasarc.gsfc.nasa.gov/docs/heasarc/ofwg/docs/spectra/ogip_92_007/node5.html)
[XSPEC documentation](https://heasarc.gsfc.nasa.gov/xanadu/xspec/)
[Fitting spectra with sherpa](http://cxc.harvard.edu/sherpa/threads/pha_intro/)
[Profile likelihood applied to gamma-ray  spectral analysis](http://cdsads.u-strasbg.fr/abs/2001A%26A...374..895P)
