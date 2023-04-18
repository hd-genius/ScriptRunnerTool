from errors.application_error import ApplicationError


class InvalidScriptNameError(ApplicationError):
    def __init__(self, filename):
        super()
        self.filename = filename

    def print(self):
        print("The script was not found")
