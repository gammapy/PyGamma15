# Python web apps with Flask

- [Flask](http://flask.pocoo.org/) - web development, one drop at a time.
- Demo the "hello world" example
- Add a second route with a variable as shown [here](http://flask.pocoo.org/docs/quickstart/#variable-rules)
- Render a template as shown [here](http://flask.pocoo.org/docs/quickstart/#rendering-templates)
- The template engine is [Jinja](http://jinja.pocoo.org/).
When people say "Jinja", they mean "Jinja 2".
You should always `pip install jinja2` and `import jinja2`
- Demo the [debug mode](http://flask.pocoo.org/docs/quickstart/#debug-mode),
put an error in the view function and template
- Form handling
- Make Matplotlib image
- A few weeks ago I've started to use Flask in gammapy:
  - `gammapy-catalog-browse` to browse catalogs / make plots (3FGL and HGPS for now, 2FHL, SNRCat, .... soon).
  - `gammapy-data-browse` to browse HESS event lists and IRFs (broken at the moment due to changes in DataStore)
  - I just started learning Flask / web development,
    only a small part of these apps is implemented and the existing things are partly broken / not nice.
  - Any help would be very appreciated, there could also be
    an app to configure and launch analyses or to browse analysis
    results (e.g. change energy range and make a new image, or go through run-per-run IRFs to check that the run quality is OK)
- If you'd like to get started, I can recommend this:
read the first ~ 40 pages of the [Flask book from O'Reilly](http://flaskbook.com/) or read the first few posts from the [Flask mega tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg. All the code is available at https://github.com/miguelgrinberg/flasky ... you can checkout the git tags (`2a`, `2b`, `3a`, ...) and play with the examples to learn!
