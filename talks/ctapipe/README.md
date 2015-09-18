# Talk - Exploring large-scale data processing in Python with CTA

* Presenter: [Karl Kosack](https://github.com/kosack)
* Duration: 12 + 3 min

## Abstract

The upcoming CTA (Cherenkov Telescope Array) observarory faces the
challenge of processing a large amount of binary data, similar in
scale to that produced by the LHC at CERN. CTA's predecessors have all
used data processing pipelines heavily based on CERN's ROOT framework
and a mixture of compiled and scripted C++. Pittfalls related to this
approach along with a desire to leverage code developent from a wider
scientific and industial community have led us to explore using modern
Python (with packages like numpy, scikit-learn, astropy, etc) for at
least the high-level parts of the CTA pipeline, and likely extending
to the low-level algorithms. In this presentation I will present the
challenges we face and what solutions we are currently exploring for
interoperability and code optimization.

https://github.com/cta-observatory/ctapipe

## Outline

* Data processing challenges
* CTA pipeline overview
* Python for I/O critical data processing
* Python for speed-critical data processing
* What is needed for a data processing framework?
* What can we work on this week?
* [ctapipe](https://github.com/cta-observatory/ctapipe) high-level overview

## References

* http://www.cta-observatory.org
* https://github.com/cta-observatory/ctapipe
* See `ctapipe` tutorial
