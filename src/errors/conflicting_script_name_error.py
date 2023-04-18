from errors.application_error import ApplicationError


class ConflictingScriptNamesError(ApplicationError):
    def __init__(self, filename, conflicting_paths):
        super()
        self.filename = filename
        self.conflicting_paths = conflicting_paths

    def print():
        pass
