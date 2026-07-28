import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "DL-Chicken-Disease-Classification"
AUTHORE_USER_NAME = "vicky7350"
SRC_REPO = "cnnClassification"
AUTHOR_EMAIL ="vikashsingh7350@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHORE_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN application",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHORE_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHORE_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
