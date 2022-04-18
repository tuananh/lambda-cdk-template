class Config:
    def __init__(self) -> None:
        self._default_config = {}

    def base(self):
        __config = {"lambda_timeout": 180}
        return {**__config, **self._default_config}