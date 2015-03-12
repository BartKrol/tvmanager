#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from app.app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    """Populate stuff in flask shell"""
    return dict(app=app, db=db)

@manager.command
def test(coverage=False):
    """Run unit tests."""
    import nose2

    script_path = os.path.realpath(__file__)
    server_path = os.path.dirname(script_path) #+ '/tests'

    # Remember that the first argument is always current file
    arguments = [script_path, '-s', server_path]
    plugins = ['nose2.plugins.layers']

    if coverage:
        arguments.append('--with-coverage')

    return nose2.discover(argv=arguments, plugins=plugins)


# Populate commands
manager.add_command('shell', Shell(make_context=make_shell_context, use_bpython=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

