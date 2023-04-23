from .script_handler import ScriptHandler

script_handlers: list[ScriptHandler] = []


def register_handler(handler_class):
    """A decorator that registers a class as a script handler."""
    handler_instance = handler_class()
    script_handlers.append(handler_instance)
    return handler_class
