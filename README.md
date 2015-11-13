
## Starting up

Starting up is easy. Just clone the repository, install dependencies, and run `manage.py`.

###Prerequisites
The following are required:

* `npm`
* `bower`
* `pip`
* `brew`, `apt-get`, or `yum`

### Installation

* Clone the repository:

```
$ git clone git@github.com:jamiecounsell/procurement.git
$ cd procurement/
```

* Install dependencies:

```
$ npm install
$ bower install
$ pip install -r requirements.txt
```
* Configure the [.env file](#env)  

* Migrate the server and create a superuser:

```
$ ./app/manage.py syncdb
```

* Build directories if missing:
```
$ mkdir app/dist
$ mkdir app/build
```

* Run the server:

```
$ ./app/manage.py gruntserver
```

## .env

A .env file is required to configure system-wide settings. The format of the file is below. For strings containing spaces, use quotations. Avoid spaces between the key and the value.

```
SECRET_KEY=
DEBUG=

# Databases
default_ENGINE='django.db.backends.sqlite3'
default_NAME=
```
