from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="alshidata",               # Package name
    version="0.1.1",                   # Initial version
    packages=find_packages(),          # Automatically find packages in your directory
    install_requires=requirements,      # List dependencies here (if any)
    author="Samuel Cavazos",
    author_email="samuel@alshival.com",
    description="A bunch of data tools by Alshival\'s Data Service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alshivals-Data-Service/alshidata",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
