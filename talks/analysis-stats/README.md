# Talk - Detection and parameter estimation in gamma-ray astronomy

* Presenter: [Michael Schmelling]()
* Duration: 15 + 5 min

## Abstract

Introduction to the most common frequentist and Bayesian methods for parameter
estimation and signal detection in gamma-ray astronomy.

A more in-depth and hands-on [statistics
tutorial](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/analysis-stats)
on the same subject will be given later in the week.


## Outline

TBD: ... this is just a first suggestion ...

* Likelihood
* The likelihood statistics used in gamma-ray astronomy (see [Sherpa statistics page](http://cxc.cfa.harvard.edu/sherpa/statistics/)): chi2 variants, cash, cstat.
The wstat on-off likelihood fit statistic from XSPEC is currently being added, for now see [here](https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/XSappendixStatistics.html) or [here](http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/wstat.ps)
* Is there a simple toy example where it can be shown why likelihood parameter estimators are sometimes biased?
  Low-stats power-law with Poisson statistics?
* Nuisance parameters, profile likelihood
* Confidence intervals, coverage
* Explain TS and Wilk's theorem, Li & Ma significance
* Explain how sensitivity and upper limits and parameter errors relate
* Frequentist and Bayesian likelihood analysis; optimisation vs. sampling; parameter estimation and detection
* Methods to handle systematic errors for detection and parameter estimation
* Model selection (Probably no time?)
* How to handle searches in multiple places, analysis configs, etc. "Trial factors", "Look elsewhere effect" (probably no time?)
* Suggestions what to work on this week?

## References

Theory:

* [Li & Ma (1983) "Analysis methods for results in gamma-ray astronomy"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1983ApJ...272..317L/)
* [Cash (1979) "Parameter estimation in astronomy through application of the likelihood ratio"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1979ApJ...228..939C/)
* [Rolke et al. (2005) "Limits and confidence intervals in the presence of nuisance parameters"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2005NIMPA.551..493R/)
* [Cousins et al (2008) "Evaluation of three methods for calculating statistical significance when incorporating a systematic uncertainty into a test of the background-only hypothesis for a Poisson process"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2008NIMPA.595..480C/)
* [Spengler (2015) "Significance in gamma ray astronomy with systematic errors"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015APh....67...70S/)

Practical, with Python implementation:

* [Vanderplas (2014) "Frequentism and Bayesianism: A Python-driven Primer"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2014arXiv1411.5018V/)
* [Vanderplas (2014) Series of blog posts: "Frequentism and Bayesianism: A Practical Introduction"](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/)
* [Foreman-Mackey et al. (2013) "emcee: The MCMC Hammer"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2013PASP..125..306F/)
* [James (1980) "Interpretation of the shape of the likelihood function around its minimum"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1980CoPhC..20...29J/)
