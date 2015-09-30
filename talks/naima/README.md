# Talk - SED modeling with Naima

* Presenter: [Victor Zabalza](https://github.com/zblz/)
* Duration: 12 + 3 min

## Abstract

The ultimate goal when observing and analyzing the non-thermal spectra from
astrophysical sources is to understand the acceleration and cooling processes
that affect relativistic particle populations. To do so, we must bridge the gap
between the observed photon spectra and the parent particle population that
gave rise to it. In this talk I will give an overview of the general problems
faced when trying to infer the physical processes responsible for the observed
spectra, and will present [naima](https://github.com/zblz/naima), a Python
package that provides an open-source implementation of radiative models and
tools to fit them to nonthermal spectra.

## Outline

* Astrophysical motivation for radiative modelling of sources
* Particle distribution evolution (cooling, escape)
* Overview of high-energy radiation processes with comments on numerical
  implementation
  - Synchrotron
  - Inverse Compton
  - Nonthermal bremsstrahlung
  - Neutral pion decay
* Overview of Naima capabilities for radiative modelling
* Example of their use on a HESS source (preview of tutorial)

## References

* [Zabalza (2015), "naima: a Python package for inference of relativistic
  particle energy distributions from observed nonthermal
  spectra"](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015arXiv150903319Z/)
* [Naima documentation](http://naima.readthedocs.org), specially the [Radiative
  Models](http://naima.readthedocs.org/en/latest/radiative.html) and [MCMC
  intro](http://naima.readthedocs.org/en/latest/mcmc.html)
* The details of MCMC sampling with emcee have been covered in the [stats
  talk](https://github.com/gammapy/PyGamma15/tree/gh-pages/talks/analysis-stats)
  and
  [tutorial](https://github.com/gammapy/PyGamma15/tree/gh-pages/tutorials/analysis-stats)
  by Michal Schmelling.
* [Naima tutorial later in the
  week](https://github.com/gammapy/PyGamma15/tree/gh-pages/tutorials/naima)
