class Config:
    SECRET_KEY = 'TuMaMaEnTaNgA'


class DevelopmentcConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456789'
    MYSQL_DB = 'flask_login'



config = {
    'developement' : DevelopmentcConfig
}