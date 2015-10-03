# Talk - Statistics for gamma-ray astronomy

* Presenter: [Michael Schmelling]()
* Duration: 25 + 5 min

## Abstract

This talk will give an overview of statistics for in gamma-ray astronomy,
e.g. how parameters and parameter errors are estimated, or how signal
detections are quantified and reported.

Both theoretical concepts as well as computational methods will be covered, i.e.
you will learn both how statistics are defined as well as how you can compute
them efficiently.

There will be a hands-on tutorial with Python coding excercises later in the week.

## Outline

To be discussed ... this is just a first suggestion:

Given the limited time, the focus will be on the most common statistical
concepts and methods for gamma-ray astronomy.

* Poisson likelihood (cash statistic)
* Nuisance parameters, profile likelihood (wstat statistic)
* Relation of likelihood to Bayesian statistics (prior and posterior)
* Parameter estimation, confidence intervals, coverage
* Detection (TS, Wilk's theorem, Li & Ma significance)
* What's the relation between parameter errors, upper limits and sensitivity?
* Overview frequentist and Bayesian computational methods: optimisation, root finding, sampling

Maybe, if there's time:

* explain how MINUIT (MIGRAD, HESSE, MIGRAD) works in detail
* explain how emcee sampling works in detail
* how to handle systematic errors?
* model selection
* searches, trials

## References

Theory:

* [James (1980) "Interpretation of the shape of the likelihood function around its minimum"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1980CoPhC..20...29J/)
* [Li & Ma (1983) "Analysis methods for results in gamma-ray astronomy"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1983ApJ...272..317L/)
* [Cash (1979) "Parameter estimation in astronomy through application of the likelihood ratio"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1979ApJ...228..939C/)
* [Rolke et al. (2005) "Limits and confidence intervals in the presence of nuisance parameters"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2005NIMPA.551..493R/)
* [Cousins et al (2008) "Evaluation of three methods for calculating statistical significance when incorporating a systematic uncertainty into a test of the background-only hypothesis for a Poisson process"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2008NIMPA.595..480C/)
* [Spengler (2015) "Significance in gamma ray astronomy with systematic errors"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015APh....67...70S/)

Practical, with Python implementation:

* [Vanderplas (2014) "Frequentism and Bayesianism: A Python-driven Primer"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2014arXiv1411.5018V/)
* [Vanderplas (2014) Series of blog posts: "Frequentism and Bayesianism: A Practical Introduction"](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/)
* [iminuit code](http://iminuit.readthedocs.org/en/latest/)
* [Foreman-Mackey et al. (2013) "emcee: The MCMC Hammer"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2013PASP..125..306F/)
* [emcee code](http://dan.iel.fm/emcee/current/)

## See also

* [Tutorial - Statistics for gamma-ray astronomy](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/analysis-stats)
