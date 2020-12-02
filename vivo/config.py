from prettyconf import config


class Settings:

    LOG_LEVEL = config('LOG_LEVEL', default='INFO')


settings = Settings()
