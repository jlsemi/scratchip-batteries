# See LICENSE for license details.

import pkg_resources


def get_resource_name(dest_name):
    return pkg_resources.resource_filename(__name__, dest_name)


def get_resource_string(dest_name):
    return pkg_resources.resource_string(__name__, dest_name)


default = "chisel3-v3.2"

batteries = {
    'chisel3-v3.5.4': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.4/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.4/mill.tar.gz"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-v3.5.4/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.4/Top.scala"),
            ],
        }
    },
    'chisel3-jlsemi-v3.5.4': {
        "init": {
            ".scratchip": [
                get_resource_name("assets/chisel3-v3.5.4/cache.tar.gz"),
                get_resource_name("assets/chisel3-v3.5.4/mill.tar.gz"),
            ],
            ".scratchip/jars": [
                get_resource_name("assets/chisel3-jlsemi-v3.5.4/chisel3-jlsemi-v3.5.4.jar"),
            ],
        },
        "create": {
            "hw/chisel/": [
                get_resource_name("assets/chisel3-jlsemi-v3.5.4/build.sc"),
            ],
            "hw/chisel/src": [
                get_resource_name("assets/chisel3-v3.5.4/Top.scala"),
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
        }
    },
}
