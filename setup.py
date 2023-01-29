# coding:utf-8

from setuptools import setup

setup(
    name="scratchip-batteries",
    url='https://github.com/jlsemi',
    packages=["scratchip_batteries"],
    package_data={
        "scratchip_batteries": [
            "assets/chisel3-jlsemi-v3.6.0/chisel3-jlsemi-v3.6.0.jar",
            "assets/chisel3-jlsemi-v3.6.0/plugin-v3.6.0.jar",

            "assets/chisel3-v3.5.5/cache.tar.gz",
            "assets/chisel3-v3.5.5/mill.tar.gz",
            "assets/chisel3-v3.5.5/Top.scala",
            "assets/chisel3-v3.5.5/build.sc",
            "assets/chisel3-v3.5.5/Makefile",
            "assets/chisel3-v3.5.5/chisel3-v3.5.5.jar",
            "assets/chisel3-v3.5.5/plugin.jar",

            "assets/chisel3-jlsemi-v3.5.5/chisel3-jlsemi-v3.5.5.jar",

            "assets/chisel3-jlsemi-v3.2/cache.tar.gz",
            "assets/chisel3-jlsemi-v3.2/mill.tar.gz",
            "assets/chisel3-jlsemi-v3.2/Top.scala",
            "assets/chisel3-jlsemi-v3.2/build.sc",
            "assets/chisel3-jlsemi-v3.2/chisel3-jlsemi-v3.2.jar",
            "assets/chisel3-jlsemi-v3.2/Makefile",

            "assets/knitkit/build.sc",
            "assets/knitkit/knitkit.jar",
            "assets/knitkit/Top.scala",
            "assets/knitkit/Makefile",
        ],
    },
    version="0.2.7",
    author="Leway Colin@JLSemi",
    author_email="colinlin@jlsemi.com",
    description=(
        "Scratchip Batteries is a fat JAR with all of its dependencies."
    ),
    license="Apache-2.0 License",
    keywords=[
        "scratchip",
    ],
    entry_points={
        "console_scripts":
            ["scratchip_batteries = scratchip_batteries.main:main"],
    },
    install_requires=[
    ],
    # Supported Python versions: 3.6+
    python_requires=">=3.6",
)
