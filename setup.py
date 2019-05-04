import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyosu",
    version="1.0",
    author="HellCatNya",
    author_email="blacktigermaxx@gmail.com",
    description="Python lib for OSU API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hell13Cat/PyOSU",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    packages=setuptools.find_packages(),
    install_requires = ["requests"]
)
