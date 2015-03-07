#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

from app import db, create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    """Populate stuff in flask shell"""
    return dict(app=app, db=db)

@manager.command
def test(coverage=False):
    """Run unit tests."""
    import nose

    server_dir = os.path.dirname(os.path.realpath(__file__))

    # Remember that the first argument is always cwd
    arguments = [os.getcwd(), server_dir]

    if coverage:
        arguments.append('--with-coverage')
        arguments.append('--cover-package=app')

    return nose.main(argv=arguments)


# Populate commands
manager.add_command('shell', Shell(make_context=make_shell_context, use_bpython=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

