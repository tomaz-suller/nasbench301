import os
import sys
import setuptools
import subprocess
from importlib import import_module


def install_if_not_found(module: str, install_from: str, user: bool = False):
    try:
        import_module(module)
    except ModuleNotFoundError:
        print(f"Installing {module}")
        python_command = f"{sys.executable} -m pip install --upgrade".split()
        if user:
            python_command.append("--user")
        python_command.append(install_from)
        subprocess.run(python_command, check=False)


with open("README.md", "r") as f:
    long_description = f.read()

requirements = []
with open('requirements.txt', 'r') as f:
    for line in f:
        requirements.append(line.strip())

install_if_not_found(
    "ConfigSpace",
    "git+https://github.com/tomaz-suller/ConfigSpace.git@fix-naslib",
)

#optional_requirements = []
#with open('optional-requirements.txt', 'r') as f:
#    for line in f:
#        optional_requirements.append(line.strip())

setuptools.setup(
    name="nasbench301",
    version="0.3",
    author="AutoML Freiburg",
    author_email="zimmerl@informatik.uni-freiburg.de",
    description=("A surrogate benchmark for neural architecture search"),
    long_description=long_description,
    url="https://github.com/automl/nasbench301",
    long_description_content_type="text/markdown",
    license="3-clause BSD",
    keywords="machine learning"
             "optimization tuning neural architecture deep learning",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
    ],
	python_requires='>=3',
    platforms=['Linux'],
    install_requires=requirements,
    include_package_data=True
#    extras_require=optional_requirements
)
