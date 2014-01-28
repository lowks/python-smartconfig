SmartConfig
===========

Easy way to create Python config files

* __Author__: [Ondrej Sika](http://ondrejsika.com/c.html)
* __Python Package Index__: <http://pypi.python.org/pypi/smartconfig>
* __GitHub__: <https://github.com/ondrejsika/smartconfig>

Docs
----

### Install

``` python
pip install smartconfig
```

### Usage

#### Load config from file

file `settings.py`:

``` python
VARIABLE_STR = "string"
VARIABLE_INT = 111
```

console:

``` python
>>> import smartconfig
>>> conf = smartconfig.config_from_file("settings.py")
>>> conf.VARIABLE_STR
"string"
>>> conf.VARIABLE_INT
111
```

#### Load config relatively

Smart config can load config relatively from different locations for local, user, system config.

We have a same config file on different locations:

* ~/myapp/config
* ~/.myapp
* /etc/myapp

We load config from app root (~/myapp):

``` python
>>> conf = smartconfig.config(local="config", user=".myapp", system="myapp")
```

At first smart config try open local config, than user and than system. Local config is loaded from relative path, user from home and system from etc.
