import os
from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version() -> str:
    """Get current version.
    
    :return: Current version.
    :rtype: str
    """
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()
    
def get_license_path() -> str:
    """Get path file with license text.

    :return: path
    :rtype: str
    """
    return os.path.join(BASE_DIR, "LICENSE")

def get_long_description() -> str:
    """Get README.md text.
    
    :return: README.md data.
    :rtype: str
    """
    path = os.path.join(BASE_DIR, "README.md")
    with open(path, "r") as readme_file:
        return readme_file.read().strip()

def get_requires() -> [str]:
    """Get requirements.

    :return: list with packages name.
    :rtype: [str]
    """
    path = os.path.join(BASE_DIR, "requirements.txt")
    with open(path, "r") as require_file:
        packages = [
            package.strip() for package in require_file.read().strip().split("\n")
        ]
    return packages


APP_PROPERTY = {
    "name": "Ted Talks Parser",
    "version": get_version(),
    "author": "m.shik",
    "author_email": "m.shik@protonmail.com",
    "url": "https://github.com/maximshik/ted-analysis",
    "packages": find_packages("src", exclude=["tests", "*test*"]),
    "package_dir": {"": "src"},
    "test_suite": "tests",
    "include_package_data": True,
    "license": get_license_path(),
    "description": "Ted Talks parser",
    "long_description": get_long_description(),
    "long_description_content_type": "text/markdown",
    "install_requires": get_requires(),
    "python_requires": ">=3.7.6",
    "zip_safe": False,
    "entry_points": {
        "console_scripts": [
            "tedtalks = tedtalks.app"
        ]
    },
    "classifiers": [
        "Development Status :: 5 Production/Stable"
    ],
}


setup(**APP_PROPERTY)