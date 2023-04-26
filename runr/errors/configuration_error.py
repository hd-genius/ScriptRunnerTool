from runr.errors.application_error import ApplicationError


class ConfigurationError(ApplicationError):
    def __init__(self, message) -> None:
        super().__init__()
        self.message = message

    def print(self):
        print(self.message)
