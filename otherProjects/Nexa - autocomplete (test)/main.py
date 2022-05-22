import sublime_plugin
import sublime
import sys

_is_ST3 = int(sublime.version()) >= 3114

if _is_ST3:
    # Clear module cache to force reloading all modules of this package.
    # See https://github.com/emmetio/sublime-text-plugin/issues/35
    prefix = __package__ + "."  # don't clear the base package
    for module_name in [
        module_name
        for module_name in sys.modules
        if (module_name.startswith(prefix) and module_name != __name__)
        or ("json" == module_name)
    ]:
        del sys.modules[module_name]
    prefix = None

from .lib.settings import is_native_auto_complete  # noqa E402

is_v2 = False
is_v3 = False

if int(sublime.version()) >= 4000:
    is_v3 = True
    from .completions.completions_v1 import *
else:
    raise "incompatibility detected"

class DisableViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set("nexa-disabled", True)

    def is_visible(self, *args):
        return is_v2 and not self.view.settings().get("nexa-disabled", False)


class EnableViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set("nexa-disabled", False)

    def is_visible(self, *args):
        return is_v2 and self.view.settings().get("nexa-disabled", False)


class EnableNativeAutoCompleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.load_settings("Nexa.sublime-settings").set(
            "native_auto_complete", True
        )
        sublime.save_settings("Nexa.sublime-settings")
        sublime_plugin.unload_plugin(__name__)
        sublime_plugin.reload_plugin(__name__)

    def is_visible(self, *args):
        return not is_v2 and not is_v3
