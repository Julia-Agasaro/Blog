import os

class Config:

    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:Agasaro1@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:Agasaro1@localhost/watchlist_test'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:Agasaro1@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
