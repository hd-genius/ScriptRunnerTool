from .script_handler import ScriptHandler

script_handlers: list[ScriptHandler] = []

"""A decorator for registering a script handler"""
def register_handler(handler_class):
    handler_instance = handler_class()
    script_handlers.append(handler_instance)
    return handler_class
