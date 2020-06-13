import setuptools

setuptools.setup(
    name="autocli",
    version="1.0",
    author="Daniel Tan",
    author_email="dtch009@gmail.com",
    description="Generate ArgParse command-line arguments automatically"
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])