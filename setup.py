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
            "token_granter_wrapper",
            os.path.join(os.path.dirname(os.path.realpath(__file__))),
            # "token_granter_wrapper", os.path.dirname(os.path.realpath(__file__))
        )
    ],
    package_data={
        "": ["*.so", "*.pyi"],
    },
    include_package_data=True,
    cmdclass=dict(build_ext=CMakeBuild),
)
# import os
# import pathlib

# from setuptools import setup, Extension, find_packages
# from setuptools.command.build_ext import build_ext as build_ext_orig


# class CMakeExtension(Extension):

#     def __init__(self, name):
#         # don't invoke the original build_ext for this special extension
#         super().__init__(name, sources=[])


# class build_ext(build_ext_orig):

#     def run(self):
#         for ext in self.extensions:
#             self.build_cmake(ext)
#         super().run()

#     def build_cmake(self, ext):
#         cwd = pathlib.Path().absolute()

#         # these dirs will be created in build_py, so if you don't have
#         # any python sources to bundle, the dirs will be missing
#         build_temp = pathlib.Path(self.build_temp)
#         build_temp.mkdir(parents=True, exist_ok=True)
#         extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
#         extdir.mkdir(parents=True, exist_ok=True)

#         # example of cmake args
#         config = "Debug" if self.debug else "Release"
#         cmake_args = [
#             "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(extdir.parent.absolute()),
#             "-DCMAKE_BUILD_TYPE=" + config,
#         ]

#         # example of build args
#         build_args = ["--config", config, "--", "-j4"]

#         os.chdir(str(build_temp))
#         self.spawn(["cmake", str(cwd)] + cmake_args)
#         if not self.dry_run:
#             self.spawn(["cmake", "--build", "."] + build_args)
#         # Troubleshooting: if fail on line above then delete all possible
#         # temporary CMake files including "CMakeCache.txt" in top level dir.
#         os.chdir(str(cwd))


# setup(
#     name="token-granter-wrapper",
#     version="0.1",
#     packages=find_packages(),
#     ext_modules=[CMakeExtension("src/token_granter_bindings.cpp")],
#     package_data={
#         "": ["*.so", "*.pyi"],
#     },
#     include_package_data=True,
#     cmdclass={
#         "build_ext": build_ext,
#     },
# )
