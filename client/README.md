# Client

## Tools
Install required tools. You need to install node, 

```sh
$ npm install -g bower gulp karma-cli
```

## Setup
Install tools by running

```sh
$ npm install
$ bower install
```

## Running Client
In order to nicely separate layers we are running separate _server_ for client.
Unfortunately it requires configuring proxy redirect in ./gulp/proxy.js file. On
default it will listen to *localhost* on port *5000*.

```sh
$ gulp serve
```

**IMPORTANT** - Backend server must be running !
