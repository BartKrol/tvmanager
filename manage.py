import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import db, create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
def test(coverage=False):
    """Run unit tests."""
    import nose
    arguments = [os.getcwd()]

    if coverage:
        arguments.append('--with-coverage')
        arguments.append('--cover-package=app')

    nose.main(argv=arguments)


def make_shell_context():
    return dict(app=app, db=db)

if __name__ == '__main__':
    manager.add_command("shell", Shell(make_context=make_shell_context, use_bpython=True))
    manager.add_command('db', MigrateCommand)
    manager.run()

