from prettyconf import config


class Settings:

    LOG_LEVEL = config('LOG_LEVEL', default='INFO')

    DEBUG = config('DEBUG', cast=config.boolean)


settings = Settings()
