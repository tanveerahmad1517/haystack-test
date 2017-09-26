# Haystack-Test

This repository contains some basic, initial workings on haystack.

Haystack-test-2 contains a more in depth example with multiple types of records and different types of searching: https://github.com/cedadev/haystack-test-2

Haystack-moles-test contains a lot of moles style records and go more in depth about indexing: https://github.com/cedadev/haystack-moles-test

## Haystack oddities

`Haystack` does not officially support `ElasticSearch` above 2.x I found this stated in the `Haystack` documentation (here: http://django-haystack.readthedocs.io/en/master/installing_search_engines.html) under the `ElasticSearch` section.

The unofficial fork of the `Haystack` repository that does support `ElasticSearch 5.x` (see: https://github.com/CraveFood/django-haystack-elasticsearch).
Getting this to work properly requires the regular `Haystack` installation as well.

The documentation for `Haystack` recommends using an `include` in our `urls.py`.  This saves us the trouble of setting up particular `views` for the search related elements, however it does mean that `Haystack` defaults to searching for templates in the `virtualenv` that we are currently using rather than the `Django` app we have created.  While `Haystack` does this for the templating it still relies on the standard `Django` method of migrating models and storing the `searchIndexes` in the app directory of the project.

All required components are specified in `requirements.txt` and can be installed with a single command `pip install` command (see below).

## Getting started

Set up the virtualenv: 

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create the `settings_local.py` file:

```
cd testsite/
cp testsite/settings_local.py.tmpl testsite/settings_local.py
```

And edit the file to give the:

 1. Details of the ElasticSearch service and index.
 2. Location of the Sqlite database. This must be a file on the local (not shared) file system.

Now create the database:

```
export DJANGO_SETTINGS_MODULE=testsite.settings
python manage.py migrate
```

Now populate the database:

```
python create_records.py
```

Now index the records in ElasticSearch:

```
python manage.py rebuild_index
```

And run the server:

```
python manage.py runserver
```

Now the UI is viewable at:

 http://localhost:8000/search/

