import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libjavaserialize",
    version="0.0.1",
    author="Frank",
    author_email="frankli0324@hotmail.com",
    description="A port of Java's [read/write]Object method, in pure python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankli0324/libjavaserialize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
    install_requires=[]
)
