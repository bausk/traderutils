import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="traderutils",
    version="0.0.1",
    author="Oleksander Bausk",
    author_email="bauskas@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bausk/traderutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)