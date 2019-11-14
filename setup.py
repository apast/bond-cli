from setuptools import setup, find_packages

with open("requirements.txt", "r") as _file:
    DEPS_MAIN = _file.readlines()

with open("requirements-test.txt", "r") as _file:
    DEPS_TEST = DEPS_MAIN + _file.readlines()

with open("VERSION", "r") as _file:
    VERSION = _file.readline().strip()

setup(
    name="bond-cli",
    version=VERSION,
    author="Olibra",
    packages=find_packages(),
    include_package_data=True,
    description="Bond Command Line Interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    setup_requires=["pytest-runner"],
    install_requires=DEPS_MAIN,
    tests_require=DEPS_TEST,
    extras_require={"test": DEPS_TEST},
)
