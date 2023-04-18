from src.errors.application_error import ApplicationError


class InvalidScriptNameError(ApplicationError):
    def __init__(self, filename):
        super()
        self.filename = filename
