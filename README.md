# Haystack-Test

This repository contains some basic, initial workings on haystack.

Haystack-test-2 contains a more in depth example with multiple types of records and different types of searching: https://github.com/cedadev/haystack-test-2

Haystack-moles-test contains a lot of moles style records and go more in depth about indexing: https://github.com/cedadev/haystack-moles-test

# Haystack oddities

`Haystack` does not officially support `ElasticSearch` above 2.x I found this stated in the `Haystack` documentation here: http://django-haystack.readthedocs.io/en/master/installing_search_engines.html
under the `ElasticSearch` section.

I have found an unofficial fork of the `Haystack` repository that does support `ElasticSearch 5.x`
https://github.com/CraveFood/django-haystack-elasticsearch getting this to work properly requires the regular `Haystack` installation as well as this.

The documentation for `Haystack` recommends using an `include` in our `urls.py`
This saves us the trouble of setting up particular `views` for the search related elements, however it does mean that `Haystack` defaults to searching for templates in the `virtualenv` that we are currently using rather than the `Django` app we have created. Which is why I have included my environment titled `venv` in the repository.

While `Haystack` does this for the templating it still relies on the standard `Django` method of migrating models and storing it's `searchIndexes` in the app directory of the project.

All required components are specified in `requirements.txt` and can be installed with a single command `pip install "elasticsearch>=5.0.0,<6.0.0" django-haystack-elasticsearch`

# Getting this example running

I had no issue with pulling down the repo and using this command to use the Django server:
`````
source venv/bin/activate
`````
If you find that the virtual environment does not work for you, you will need to set up your own. These commands should do the job: 
`````
virtualenv <name>
source <name/bin/activate>
sudo pip install "elasticsearch>=5.0.0,<6.0.0" django-haystack-elasticsearch
`````
This should install everything you need for the virtual environment to support the Django server.

# Adding data/ Creating the index.

I have provided some Python scripts and some example text files for adding data to the database. To do this follow these commands:
`````
export DJANGO_SETTINGS_MODULE=testsite.settings # You may need to be in the testsite directory for this
python test.py
python manage.py rebuild-index
`````
If you receive an error concerning Models not existing you will need to enter `python manage.py migrate`. As is standard in Django everytime you alter a model you will need to re-migrate and rebuild your database. You can easily clear your database of entries with `python manage.py flush`. For a list of commands to be used with `manage.py` just enter `python manage.py` into the command line.

This will populate your database and build the ElasticSearch Index. Feel free to edit things in filetest.py to use whatever text file you like to take data from.
