from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import os
import sys
import subprocess


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = "Debug" if self.debug else "Release"

        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + extdir,
            "-DPYTHON_EXECUTABLE=" + sys.executable,
            "-DCMAKE_BUILD_TYPE=" + cfg,
        ]

        build_args = ["--config", cfg]

        os.chdir(ext.sourcedir)
        self.spawn(["cmake", ext.sourcedir] + cmake_args)
        if not self.dry_run:
            self.spawn(["cmake", "--build", "."] + build_args)


setup(
    name="token-granter-wrapper",
    version="0.1",
    packages=find_packages(),
    ext_modules=[
        CMakeExtension(
            "token_granter_wrapper", os.path.dirname(os.path.realpath(__file__))
        )
    ],
    package_data={
        "": ["*.so"],
    },
    cmdclass=dict(build_ext=CMakeBuild),
)
