import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    JWT_AUTH_URL_RULE = '/api/auth/'

    @staticmethod
    def static_files_endpoint(app):
        index = lambda: app.send_static_file('index.html')
        app.add_url_rule('/', 'index', index)

        static_files = lambda path: app.send_static_file('{0}'.format(path))
        app.add_url_rule('/<path:path>', 'static_files', static_files)

    @staticmethod
    def init_app(app):
        if os.environ.get('CLIENT_DIST_FOLDER'):
            app.static_folder = os.environ.get('CLIENT_DIST_FOLDER')
            app.static_url_path = ''
            DevelopmentConfig.static_files_endpoint(app)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}