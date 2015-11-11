# Tutorial - D3PO - Denosing, Deconcolving, and Decomposing Photon observations, an algorithm based on information field theory

* Presenter: [Daniel Pumpe](https://github.com/dpumpe)
* Duration: 90 min
* Time: Wednesday, 16:00 - 17:30
* Location: Central seminar room

## Abstract

In this tutorial I will briefly introduce D3PO, which addresses the inference
problem of denoising, deconvolving, and decomposing photon observations. Its
primary goal is thereby to simultaneously but individual reconstruct the diffuse
and point like photon flux given a photon count image.

D3PO is based on information field theory (IFT), which will be introduced as
well. IFT is a  Bayesian framework for signal processing and image
reconstruction. For practical calculations 'Numerical information field theory'-
NIFTy can be used. NIFTy is a versatile Python library to enable the development
of signal inference algorithms that operate regardless of the underlying spatial
grid and its resolution. 

Within a first practical hands on session we will guide the audience thru some
examples (Wiener filter etc.) and thereby demonstrate NIFTy principle
capabilities. Then the usage of D3PO will be demonstrated. 

## How to prepare

1. Install NIFTy by pip install ift_nifty
2. Install D3PO by pip install ift_d3po

Detailed instruction how to install [NIFTy](http://wwwmpa.mpa-garching.mpg.de/ift/nifty/install.html#download-label) 
and [D3PO](http://wwwmpa.mpa-garching.mpg.de/ift/d3po/install.html#download-label) 

First you should install all dependicies ([NUMPy](http://www.numpy.org), [SciPy](http://www.scipy.org), [matplotlib](http://matplotlib.org), [multiprocessing](https://docs.python.org/2/library/multiprocessing.html), [GFFT](https://github.com/mrbell/gfft), [healpy](https://github.com/healpy/healpy), [libsharpwrapper](https://github.com/mselig/libsharp-wrapper)) needed for NIFTy, followed by the NIFTy installtion itself. Last one may install D3PO as it deppends on NIFTy. 

Please note that NIFTy as well as D3PO only work with Python 2.7

## Agenda


- Introduction to Information field theory
- Numerical information field theory, what are its capabilities?
  Hands so session (Wiener filter etc.)
- Introduction to D3PO- Denoising, Deconvolving, and Decomposing photon observations
- Hands on session with D3PO

## Going further

If you'd like to learn more, here's some useful references:

* D3PO [code](https://github.com/information-field-theory/d3po),
  [docs](http://wwwmpa.mpa-garching.mpg.de/ift/d3po/)
* Nifty [code](https://github.com/information-field-theory/nifty),
  [docs](http://wwwmpa.mpa-garching.mpg.de/ift/nifty/)
* [D3PO algorithm paper](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015A%26A...574A..74S/)
* [D3PO application to Fermi-LAT data](http://labs.adsabs.harvard.edu/adsabsadsabs/abs/2015A%26A...581A.126S/)
* [Information Field Theory webpage](https://wwwmpa.mpa-garching.mpg.de/ift/)
