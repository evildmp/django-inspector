django-inspector
================

Inspects and reports on Django sites

https://github.com/evildmp/django-inspector.git

Quick start
===========

Install
-------

Install with pip, from GitHub::

    pip install -e git+git://github.com/evildmp/django-inspector.git#egg=django-inspector

Add::

    'inspector',

to ``INSTALLED_APPS``.

Django Inspector uses BeautifulSoup.

Use
---

Run ``syncdb``.

To run an inspection, in your project::

    python manage.py follow_all_links
    
Starting at the URL ``/``, Django inspector will visit the pages in the project.

For each published page (``models.Path``), it will collect:

* information about the page:
    * its path
    * the response code from the server
    * the resource's ``content-type``
    * any Django errors raised when the page was served
    * the page that linked to it
* all the links to other pages from it that:
    * begin with ``/`` (i.e. are internal ones)
    * haven't yet been collected

Reports
-------

Django Inspector reports in three ways:

In the terminal
^^^^^^^^^^^^^^^

In the terminal::

    / 200 36 found and 35 remaining
    /about-us/ 200 37 found and 35 remaining
    /medical-education/ 200 58 found and 55 remaining
    /research/ 200 74 found and 70 remaining
    [time passes...]
    /forthcoming-events/help-study/ 200 6445 found and 3 remaining
    /event/department-meeting/ 200 6445 found and 2 remaining
    /event/department-meeting/ 200 6445 found and 1 remaining
    /person/dr-frances-jane-rice/ 200 6445 found and 0 remaining

In the database
^^^^^^^^^^^^^^^

Each ``Inspection`` and all of its ``Paths`` will be recorded for inspection.

In future versions these will be available for inspection through the Django
application.

Via email
^^^^^^^^^

If you have set your ``ADMINS`` setting in ``settings.py``, Django will email
you when it encounters an error.

Running Django Inspector will get Django to try to serve all the pages it can
find, thus triggering any errors the page might raise; Django will email the
traceback to you. It's more effective than sitting back and waiting for
someone, or a web crawler, to visit your obscure pages to raise the error.