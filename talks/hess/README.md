# Talk - H.E.S.S. data analysis with open source tools

* Presenter: [Christoph Deil](https://github.com/cdeil)
* Duration: 12 + 3 min

## Abstract

[H.E.S.S.](http://www.mpi-hd.mpg.de/hfm/HESS/) is an array of
Cherenkov telescopes in Namibia observing the sky at TeV energies since 2004.

I will report on the activities in H.E.S.S. to export event lists
and instrument response functions (IRFs) to FITS, and to analyse
them using open source science tools like [Gammapy](https://gammapy.readthedocs.org/en/latest/)
and [ctools](http://cta.irap.omp.eu/ctools-devel/).
 
## Outline

In this talk, I plan to cover:

* The H.E.S.S. telescopes
* H.E.S.S. internal data and analysis chains
* The "H.E.S.S. data analysis with open source tools (HOST)" task group
* FITS exporters, event list and IRF formats
* FITS data distribution within H.E.S.S.
* Analyses with Gammapy and ctools
* Cross-checks against results obtained with the H.E.S.S.-internal software packages (HAP and ParisAnalysis)
* Summarise status and discuss where we might go from here ...
* What can we achieve at this workshop for H.E.S.S.?
  (data formats, methods, codes)

## References

If you'd like to get a hands-on introduction to H.E.S.S. high-level
data analysis, come to the [Gammapy](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/gammapy)
and [Naima](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/naima) tutorials.
If you'd like to do some low-level H.E.S.S. data analysis (shower images),
join the [ctapipe](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/ctapipe)
tutorial.

There's no good quick overview of IACT data analysis that I'm aware of.
(I'm hoping the slides of this presentation will achieve that.)

A very comprehensive and good resource is [Mathieu de Naurois's habilitation thesis](http://inspirehep.net/record/1122589).

The [H.E.S.S. 2006 Crab paper](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2006A%26A...457..899A/)
is often cited as an overview of H.E.S.S. data analysis.
It doesn't describe the high-level analysis part though, i.e.
the morphology and spectral analysis techniques that are used for H.E.S.S.
publications these days.

[Berge (2007)](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2007A%26A...466.1219B/)
is a good reference on background modeling.
