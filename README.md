# haystack-test

This repository contains some basic, initial workings on haystack.

Haystack-test-2 contains a more in depth example with multiple types of records and different types of searching.

Haystack-moles-test contains a lot of moles style records and go more in depth about indexing.

# Haystack oddities

`Haystack` does not officially support `ElasticSearch` above 2.x I found this stated in the `Haystack` documentation here: http://django-haystack.readthedocs.io/en/master/installing_search_engines.html
under the `ElasticSearch` section.

I have found an unofficial fork of the `Haystack` repository that does support `ElasticSearch 5.x`
https://github.com/CraveFood/django-haystack-elasticsearch getting this to work properly requires the regular `Haystack` installation as well as this.

The documentation for `Haystack` recommends using an `include` in our `urls.py`
This saves us the trouble of setting up particular `views` for the search related elements, however it does mean that `Haystack` defaults to searching for templates in the `virtualenv` that we are currently using rather than the `Django` app we have created. Which is why I have included my environment titled `venv` in the repository.

While `Haystack` does this for the templating it still relies on the standard `Django` method of migrating models and storing it's `searchIndexes` in the app directory of the project.

All required components are specified in `requirements.txt` and can be installed with a single command `pip install "elasticsearch>=5.0.0,<6.0.0" django-haystack-elasticsearch`
