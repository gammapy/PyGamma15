# Talk - Open source development and Python for gamma-ray astronomy

* Presenter: [Christoph Deil](https://github.com/cdeil/)
* Duration: 15 + 5 min

## Abstract

I will give a high-level overview to open-source software development and Python
for gamma-ray astronomy.

Disclaimer: Obviously every choice (language, tool, service, ) has pros and cons (git or svn? Github or self-hosted? Python, C or C++? pytest or nose? swig or Cython? pip or conda? ...). This talk will be somewhat biased and opinionated. Disagreement welcome!

## Outline

* Open source software development
  * The [git](https://git-scm.com/) version control system (compared to CSV, SVN).
  * Collaboration with [Github](https://github.com/) (compared to self-hosted solutions)
  * Licenses: free, libre, open-source, copy-left, copy-right .... oh my! Does it matter?
* Python
  * How the CPython interpreter works (compared to C / C++)
  * The dreadful Python 2 / 3 transition
  * How did Python become the most popular programming language in astronomy?
  * Testing with [pytest](http://pytest.org/latest/)
  * Documentation with [Sphinx](http://sphinx-doc.org/)
  * Packaging and distribution (pip, PyPI, conda)
  * C / C++ / Fortran extensions
  * Efficient multi-core and cluster computing with Python?
* Scientific Python (maybe I'll leave that part to the next presentation by Karl)
  * Interactive computing with IPython and the Jupyter notebook
  * Numpy and Scipy
  * Visualisation: Matplotlib, Bokeh, ...
  * Comparison with [ROOT](https://root.cern.ch/)
  * Python in industry and academia
* Python in astronomy
  * Astropy, affiliated packages, Sherpa, ..
  * Other big projects: LSST, JWST, ...
  * Many gamma-ray astro Python efforts (or C++ with Python wrapper) exists:
    [Gammapy](https://gammapy.readthedocs.org/en/latest/),
    [Naima](http://naima.readthedocs.org/en/latest/),
    [Gammalib](http://cta.irap.omp.eu/gammalib-devel/),
    [ctools](http://cta.irap.omp.eu/ctools-devel/),
    [3ML](https://threeml.stanford.edu/),
    [FermiPy](https://github.com/fermiPy/fermipy),
    [gammatools](https://github.com/woodmd/gammatools),
    [VHEObserverTools](https://github.com/kialio/VHEObserverTools),
    [ctapipe](https://github.com/cta-observatory/ctapipe), ... apologies if I've missed your project!
* The future
  * Is hard to predict, these are just some questions and opinions for discussion.
  * Is Python / Numpy / Scipy / Astropy a stable enough basis for gamma-ray astronomy? (compared to other languages / libraries)
  * Are there any game-changers in sight (e.g. the Julia language, the Pyston or PyPy Python interpreters, JITs like numba, or "numpy rewrites like dynd)?
  * When will the transition to Python 3 be complete?
  * Will / should CTA have a recommended open-source license?
* This workshop
  * Is it possible (technically and sociologically) or even desirable to
    try and merge some of the ongoing Python gamma-ray astronomy packages?
  * Alternatively, can we agree on common high-level data structures
    and file formats (e.g. for data, IRFs, observation lists, source models, fit statistics, analysis results, ...) for easy collaboration and data exchange?


## References

For a hands-on introduction to how this all works, join the
[Contributing to Python projects on Github tutorial](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/contributing).

The pytest testing framework and Sphinx documentation generator will also be
covered in the [Python developer tools tutorial](https://github.com/gammapy/2015-MPIK-Workshop/tree/gh-pages/tutorials/python-tools).

For an in-depth overview of Astropy and how Github is central to it's development,
see [Erik Tollerud's talk on "The Astropy project"](https://www.youtube.com/watch?v=osZg2cxuwwc).
