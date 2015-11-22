# Python web apps with Flask

- There's many web frameworks. In Python probably the most-used is [Django](https://www.djangoproject.com/) (everything included), the opposite is something like [bottle](http://bottlepy.org/docs/dev/index.html) (single file `bottle.py`). 
- [Flask](http://flask.pocoo.org/) - web development, one drop at a time.
Like bottle, Flask is a "micro framework", i.e. minimalistic core and lots of extensions (separate Python modules you can install, e.g. `pip install flask-wtf` for form handling, [flask-wtf](https://flask-wtf.readthedocs.org/en/latest/))
- The template engine of flask is [Jinja](http://jinja.pocoo.org/).
When people say "Jinja", they mean "Jinja 2".
You should always `pip install jinja2` and `import jinja2`
- If you'd like to get started, I can recommend this:
read the first ~ 40 pages of the [Flask book from O'Reilly](http://flaskbook.com/) or read the first few posts from the [Flask mega tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg. All the code is available at https://github.com/miguelgrinberg/flasky ... you can checkout the git tags (`2a`, `2b`, `3a`, ...) and play with the examples to learn!
- Demo the "hello world" example `2a`
- Demo example `3a`: add a second route with a [variable rule](http://flask.pocoo.org/docs/quickstart/#variable-rules) and [render a template](http://flask.pocoo.org/docs/quickstart/#rendering-templates)
- Demo the [debug mode](http://flask.pocoo.org/docs/quickstart/#debug-mode),
put an error in the view function and template
- A few weeks ago I've started to use Flask in gammapy:
  - `gammapy-catalog-browse` to browse catalogs / make plots (3FGL and HGPS for now, 2FHL, SNRCat, .... soon).
  - `gammapy-data-browse` to browse HESS event lists and IRFs (broken at the moment due to changes in DataStore)
  - I just started learning Flask / web development,
    only a small part of these apps is implemented and the existing things are partly broken / not nice.
  - Any help would be very appreciated, there could also be
    an app to configure and launch analyses or to browse analysis
    results (e.g. change energy range and make a new image, or go through run-per-run IRFs to check that the run quality is OK)
