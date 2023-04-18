from errors.application_error import ApplicationError


class ConflictingScriptNamesError(ApplicationError):
    def __init__(self, filename, conflicting_paths):
        super()
        self.filename = filename
        self.conflicting_paths = conflicting_paths

    def print(self):
        print(
            f'More than one script with the name "{self.filename}" was found:')
        for conflict in self.conflicting_paths:
            print(conflict)
