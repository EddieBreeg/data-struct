import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="structLib-Eddie-Breeg",
    version="0.0.1",
    author="Eddie Breeg",
    author_email="eddiebreeg0@protonmail.com",
    description="A class to handle complex JSON-like data objects more easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EddieBreeg/structLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)