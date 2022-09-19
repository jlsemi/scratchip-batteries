try:
    from scratchip_batteries.version import version as __version__
except ImportError:
    __version__ = "unknown"

from scratchip_batteries import main

batteries = main.batteries
default = main.default
