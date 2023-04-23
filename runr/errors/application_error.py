class ApplicationError(Exception):
    def print(self):
        print("An unexpected error was encountered")
