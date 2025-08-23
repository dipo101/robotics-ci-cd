from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import subprocess
import sys


class BazelExtension(Extension):
    """Python extension that uses Bazel to build."""
    def __init__(self, name, bazel_target, **kwargs):
        super().__init__(name, sources=[], **kwargs)
        self.bazel_target = bazel_target


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
        built_lib_path = os.path.join(bazel_bin_path, target_name + ".so")
        shutil.copy(built_lib_path, self.get_ext_fullpath(ext.name))


setup(
    name="my_robot_py",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python bindings for MyRobotProject",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    ext_modules=[
        BazelExtension(
            name="my_robot_py",
            bazel_target="//python:my_robot_py",
        ),
    ],
    cmdclass={
        'build_ext': BuildBazelExtension,
    },
    zip_safe=False,
    python_requires=">=3.10",
)