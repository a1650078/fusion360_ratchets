# A command which is able to reload another command's code
# This command intercepts calls to on_create, triggering
# a reload of the underlying addin module

# from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase

import importlib
import sys

def create_reloading_command(class):

    class ReloadingCommand:
        def on_create(self, *args, **kwargs):
            module = sys.modules[class.__module__]
            importlib.reload(module)
            the_new_class = getattr(module, class_name, None)

            # dynamically set the modules base class
            ReloadingCommand.__bases__ = (the_new_class,)

            # now run the originally requested code
            super().on_create(*args, **kwargs)

    return ReloadingCommand
