# Talk - Why Python for gamma-ray astronomy?

* Presenter: [Christoph Deil](https://github.com/kosack/)
* Duration: 12 + 3 min

## Abstract

<!-- (e.g.
<a href="https://gammapy.readthedocs.org/en/latest/">Gammapy</a>,
<a href="http://naima.readthedocs.org/en/latest/">Naima</a>,
<a href="http://cta.irap.omp.eu/gammalib-devel/">Gammalib</a>,
<a href="http://cta.irap.omp.eu/ctools-devel/">ctools</a>,
<a href="https://threeml.stanford.edu/">3ML</a>,
<a href="https://github.com/fermiPy/fermipy">FermiPy</a>,
<a href="https://github.com/woodmd/gammatools">gammatools</a>,
<a href="https://github.com/kialio/VHEObserverTools">VHEObserverTools</a>,
<a href="https://github.com/cta-observatory/ctapipe">ctapipe</a>,
<a href="http://cxc.cfa.harvard.edu/sherpa/">Sherpa</a> ).-->


Explain why Python makes sense for gamma-ray astronomy.
Give an high-level overview of the language (Py 2 / 3),
Scipy packages (Numpy, Scipy, Matplotlib, Numba) and tools (IPython, pytest, ...)

## Outline

* Language
* Packages
* Tools

## References

* See tutorials on Tuesday

* Rethinking the Gammapy stack: thoughts on how to collaborate more with other packages (Astropy, Astropy affiliated packages, Sherpa, Naima, ctapipe, Gammalib, ctools, 3ML, FermiPy, ...) to avoid duplication of effort and enable multi-mission analyses and astrophysical modeling.

# Talk - Open-source Python project development on Github

* Presenter: looking for a speaker ... you?
* Duration: 12 + 3 min

## Abstract

This presentation will give an overview of how most open-source Python projects
are run these days, explaining the tools (git, pytest, Sphinx) and
free web services (Github, travis-ci, Read the docs) and
workflows involved.


## Outline

- Open source, reproducible and open science
- The [git](https://git-scm.com/) version control system
- Development workflow with [Github](https://github.com/)
- Issues, pull requests, code review
- Testing with [pytest](http://pytest.org/latest/) and [travis-ci](https://travis-ci.org/)
- Documentation with [Sphinx](http://sphinx-doc.org/) and [Read the docs](https://readthedocs.org/).
- TBD: cover releases and distribution via PyPI and anaconda.org as well?
- TBD: Thoughts / experiences on using these services for large astronomy projects (Astropy, LSST, Sherpa, CTA, ...) versus setting up equivalent services on collaboration servers to be independent.

## References

For a hands-on introduction to how this all works, join the
[Contributing to Python projects on Github tutorial](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/contributing).

The pytest testing framework and Sphinx documentation generator will also be
covered in the [Python developer tools tutorial](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/python-tools).

For an in-depth overview of Astropy and how Github is central to it's development,
see [Erik Tollerud's talk on "The Astropy project"](https://www.youtube.com/watch?v=osZg2cxuwwc).
