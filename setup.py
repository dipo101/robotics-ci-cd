import os
import shutil
import subprocess
import sys

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


class BazelExtension(Extension):
    """A C/C++ extension that is defined as a Bazel target."""
    def __init__(self, name, bazel_target, **kwargs):
        self.bazel_target = bazel_target
        super().__init__(name, sources=[], **kwargs)


class BuildBazelExtension(build_ext):
    """A command that runs Bazel to build a C/C++ extension."""
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        if not isinstance(ext, BazelExtension):
            super().build_extension(ext)
            return

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(self.get_ext_fullpath(ext.name)), exist_ok=True)
        
        # Build the Bazel target
        bazel_cmd = [
            "bazel",
            "build",
            ext.bazel_target,
            "--compilation_mode=" + ("dbg" if self.debug else "opt"),
        ]
        subprocess.check_call(bazel_cmd)

        # Copy the built extension to the location expected by setuptools
        bazel_bin_path = "bazel-bin"
        target_name = ext.bazel_target.replace("//", "").replace(":", "/")
        
        # Determine the file extension based on the OS
        if sys.platform == "darwin":
            ext_name = ".so"
        elif sys.platform == "win32":
            ext_name = ".pyd"
        else:
            ext_name = ".so"
            
        built_lib_path = os.path.join(bazel_bin_path, target_name + ext_name)
        
        shutil.copy(built_lib_path, self.get_ext_fullpath(ext.name))


setup(
    name="my_robot_py",
    version="1.0.0",
    packages=find_packages(where="python/src"),
    package_dir={"": "python/src"},
    ext_modules=[
        BazelExtension(
            name="my_robot_py.my_robot_py",
            bazel_target="//python:my_robot_py",
        )
    ],
    cmdclass={"build_ext": BuildBazelExtension},
    zip_safe=False,
    install_requires=[],  # No external dependencies
)
