from source_radar_client.plugins.base import BasePlugin
from source_radar_client.ruff import RuffLint

_BUILTIN_PLUGINS = {
    'ruff': RuffLint
}


class PluginRegistry:
    def __init__(self):
        self.plugins = _BUILTIN_PLUGINS.copy()

    def register(self, plugin_class):
        self.plugins[plugin_class.id] = plugin_class

    def get_plugin(self, plugin_id: str) -> type[BasePlugin]:
        return self.plugins[plugin_id]
