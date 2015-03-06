# Server
Notes on working with the server.

## Requirements
Using Python 2 for now.

Install the requirements using pip and `requirements.txt`

```sh
$ pip install -r requirements.txt
```

## Usage
You can run the server using `manage.py`. Invoked without any arguments will list the available options

```sh
$ python manage.py
```

### Running Flask shell

Optional requirements:
- [http://ipython.org/](http://ipython.org/) for a nice interactive shell experience

You can install optional requirements by using pip and `server/optional_requirements.txt`

```sh
$ pip install -r optional_requirements.txt
```

### Setting up the database
In order to apply all the necessary migrations run.

```sh
$ python manage.py db upgrade
```
