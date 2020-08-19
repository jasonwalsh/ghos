from setuptools import find_packages, setup

setup(
    entry_points={"console_scripts": ["ghos = ghos.cli:run"]},
    name="ghos",
    install_requires=["pynacl", "requests"],
    packages=find_packages(),
)
