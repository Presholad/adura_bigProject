from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "adura"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    "streamlit","numpy"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for ML app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    author_email="gbemi12344@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)