import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="windowsapps",
    version="0.0.7",
    author="Tushar Goyal",
    author_email="StealtherThreat@outlook.com",
    description="Windows Apps for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StealtherThreat/windowsapps",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)