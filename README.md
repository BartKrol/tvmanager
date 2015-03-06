[![Build Status](https://travis-ci.org/BartKrol/tvmanager.svg?branch=master)](https://travis-ci.org/BartKrol/tvmanager)

# Server

## Requirements
Using Python 2 for now.

Install the requirements using pip and `server/requirements.txt`

```sh
$ pip install -r server/requirements.txt
```

## Usage

You can run the server using `server/manage.py`. Invoked without any arguments will list the available options

```sh
$ python server/manage.py
```

### Setting up the database
In order to apply all the necessary migrations run.

```sh
$ python server/manage.py db upgrade
```
