# @@ -1,21 +0,0 @@
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="contact_siphon_pkg",
    version="0.0.1",
    author="Stan King",
    author_email="stan@king-of-tx.com",
    description="An app to pull email contacts out of your IMAP mail account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stanking2/ContactSiphon",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
