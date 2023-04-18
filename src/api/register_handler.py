from .script_handler import ScriptHandler

script_handlers: list[ScriptHandler] = []

def register_handler(handler_class):
    script_handlers.append(handler_class)
