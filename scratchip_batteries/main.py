# See LICENSE for license details.

import pkg_resources


def get_resource_name(dest_name):
    return pkg_resources.resource_filename(__name__, dest_name)


def get_resource_string(dest_name):
    return pkg_resources.resource_string(__name__, dest_name)


default = "chisel3-v3.2"

batteries = {
    'chisel3-v3.6.0': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.5/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.5/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-v3.6.0/chisel3-jlsemi-v3.6.0.jar"),
            ],
            ".scratchip/plugin": [
                get_resource_name("assets/chisel3-v3.6.0/plugin.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-v3.5.5/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.5/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/chisel3-v3.5.5/Makefile"),
            ],
        }
    },
    'chisel3-jlsemi-v3.6.0': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.5/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.5/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-jlsemi-v3.6.0/chisel3-jlsemi-v3.6.0.jar"),
            ],
            ".scratchip/plugin": [
                get_resource_name("assets/chisel3-jlsemi-v3.6.0/plugin.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-v3.5.5/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.5/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/chisel3-v3.5.5/Makefile"),
            ],
        }
    },
    'chisel3-v3.5.5': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.5/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.5/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-v3.5.5/chisel3-v3.5.5.jar"),
            ],
            ".scratchip/plugin": [
                get_resource_name("assets/chisel3-v3.5.5/plugin.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-v3.5.5/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.5/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/chisel3-v3.5.5/Makefile"),
            ],
        }
    },
    'chisel3-jlsemi-v3.5.5': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.5/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.5/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-jlsemi-v3.5.5/chisel3-jlsemi-v3.5.5.jar"),
            ],
            ".scratchip/plugin": [
                get_resource_name("assets/chisel3-v3.5.5/plugin.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-v3.5.5/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.5/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/chisel3-v3.5.5/Makefile"),
            ],
        }
    },
    'knitkit': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.5/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.5/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/knitkit/knitkit.jar"),
            ],
        },
        "create": {
            "hw/knitkit/": [
                get_resource_name("assets/knitkit/build.sc"),
            ],
            "hw/knitkit/src": [
                get_resource_name("assets/knitkit/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/knitkit/Makefile"),
            ],
        },
    },
    'chisel3-v3.2': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-jlsemi-v3.2/cache.tar.gz"),
                get_resource_name("assets/chisel3-jlsemi-v3.2/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-jlsemi-v3.2/chisel3-jlsemi-v3.2.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-jlsemi-v3.2/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-jlsemi-v3.2/Top.scala"),
            ],
            ".": [
                get_resource_name("assets/chisel3-jlsemi-v3.2/Makefile"),
            ],
        }
    },
}
