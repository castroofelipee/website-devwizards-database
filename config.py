import os

class Config:
   
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USERNAME = os.getenv("DB_USERNAME", "seu_usuario_mysql")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "sua_senha_mysql")
    DB_NAME = os.getenv("DB_NAME", "nome_do_banco")

    
    DEBUG = os.getenv("DEBUG", True)
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta")

    
    SSL_CA_PATH = os.getenv("SSL_CA_PATH", "/etc/ssl/cert.pem")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
