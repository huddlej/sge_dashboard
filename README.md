sge_dashboard
=============

A simple dashboard for grid engine

Getting started
---------------

Install dependencies (inside virtualenv, preferably).

    pip install -r requirements.txt

Create your database.

    ./manage.py syncdb

Dump job data from your grid engine's ``qacct``.

    qacct -j > jobs.txt

Load job data into the database.

    python parse_qacct.py jobs.txt

Start a Django server.

    ./manage.py runserver

Inspect your job data at /admin/.
