from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="indtools_pwa",
    version="0.0.1",
    description="INDTOOLS - Industrial Tools & Fasteners Ionic PWA",
    author="INDTOOLS",
    author_email="indtools1992@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
