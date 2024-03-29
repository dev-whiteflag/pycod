import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycod",
    version="0.3.3",
    author="SE2Dev, dtzxporter, Scobalula, imwhiteflag",
    description="A Python library for reading/writing Call of Duty's *_EXPORT files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"pycod": "pycod"},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)