import io
import os

import torch
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


def get_requirements():
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    with io.open(req_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def get_long_description():
    readme_file = os.path.join(os.path.dirname(__file__), "README.md")
    with io.open(readme_file, "r", encoding="utf-8") as f:
        return f.read()


if not torch.cuda.is_available():
    raise Exception("CPU version is not implemented")


requirements = get_requirements()
long_description = get_long_description()

setup(
    name="gather",
    version="0.2.0",
    description="PyTorch bindings for CUDA Gather",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxwellzh/torch-gather",
    author="Huahuan Zheng",
    author_email="maxwellzh@outlook.com",
    license="MIT",
    packages=find_packages(),
    ext_modules=[
        CUDAExtension(
            name="gather._C",
            sources=["core.cu", "binding.cpp"]
        )
    ],
    cmdclass={"build_ext": BuildExtension},
    setup_requires=requirements,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
