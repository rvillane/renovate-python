import setuptools
import unittest


def test_suite_loc():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')
    return test_suite


setuptools.setup(
    name="group-creator",
    version="0.1.0",
    description="Script to manage AD groups",
    author="L.L.Bean, Inc",
    url="https://github.com/rvillane/renovate-python",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests",
        ],
    test_suite='setup.test_suite_loc',
    zip_safe=True,
)
