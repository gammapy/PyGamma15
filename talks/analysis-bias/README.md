# Talk - Bias in spectral likelihood estimators and observation grouping

* Presenter: Lea Jouvin
* Duration: 10 + 5 min

## Abstract

Spectral extraction in data from ground-based gamma-ray observations is usually
performed using the on-off likelihood statistic which is based on the profile
likelihood technique. The latter is known to lead to inconsistent estimators in
some situations. We present here a systematic Monte Carlo study of the
distribution of fitted spectral parameters for typical observations with VHE
(very high energy; >100GeV) observatories and show that in some conditions
spectral extraction yields inconsistent estimators. We discuss some techniques
to alleviate this effect and the impact on the search for spectral cutoffs in
the very low statistic regime.

## Outline

* “forward folding method”:
  comparison of a spectral shape hypothesis assumed a priori convolved by
  the instrument response functions (IRFs) with the observations.
  * Spectral parameters then evaluated with a Maximum Likelihood (M.L.) method. 
  * Background: no realistic model so far: marginalize the background (“profile likelihood” ) [3]:
    - interest parameters: spectral model parameters
    - nuisance parameters: Background from ON region (region of interest) and OFF region (without sources)

* H.E.S.S. (High Energy Stereoscopic System): VHE gamma-ray atmospheric Cherenkov telescopes
   * Typical source observation covers wide range of observational parameters (e.g. time, zenith, offset).
   * Strong IRFs dependence with the observational parameters and energy and IRFs are calculated for each observation. 
   * In order to keep all the information related to the observation conditions, one of the official H.E.S.S. spectrum fitting packages, processes all the observations individually for the likelihood maximization
   * Maximization of the likelihood function background estimators in the ON and OFF regions.

Issues:

* Without observations grouping, due to the large number of nuisance parameters,
  the estimators can be significantly biased (up to dozen of percent)
* Where there is as many nuisance parameters as observations:
  estimators can be inconsistent (i.e. do not converge to the right value
  even for an infinite number of observations)
  -> we need an observation grouping to decrease the number of degree of freedom

In order to test the consistency of the estimators on the adjusted spectral
parameters MC tool that simulate ON & OFF spectra. We test also the impact of
observation grouping on the estimators bias as it is done in other spectrum
fitting package in H.E.S.S..


## References

This study described here: [Jouvin L. et al, ICRC 2015](https://indico.cern.ch/event/344485/session/142/contribution/1183)

Statistics reference:

* [Piron F. et al, 2001, A&A, 374](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2001A%26A...374..895P/)
* [Cash W., 1979, ApJ, 228](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/1979ApJ...228..939C/)
* Neyman J. and Scott E. L.,  1948, The Econometrica Society, 16
* [Spanos A., 2013, ArXiv e-prints](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2013arXiv1301.0118S/)
