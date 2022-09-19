# coding:utf-8

from setuptools import setup

setup(
    name="scratchip-batteries",
    url='https://github.com/jlsemi',
    packages=["scratchip_batteries"],
    package_data={
        "scratchip_batteries": [
            "assets/chisel3-v3.5.4/cache.tar.gz",
            "assets/chisel3-v3.5.4/mill.tar.gz",
            "assets/chisel3-v3.5.4/Top.scala",
            "assets/chisel3-v3.5.4/build.sc",
            "assets/chisel3-jlsemi-v3.5.4/chisel3-jlsemi-v3.5.4.jar",
            "assets/chisel3-jlsemi-v3.5.4/Top.scala",
            "assets/chisel3-jlsemi-v3.5.4/build.sc",
        ],
    },
    use_scm_version={
        "relative_to": __file__,
        "write_to": "scratchip_batteries/version.py",
    },
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
    setup_requires=["setuptools_scm"],
    install_requires=[
    ],
    # Supported Python versions: 3.6+
    python_requires=">=3.6",
)
