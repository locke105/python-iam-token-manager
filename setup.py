from setuptools import setup

from os import path
curr_dir = path.abspath(path.dirname(__file__))
with open(path.join(curr_dir, 'README.md')) as readme:
    readme_content = readme.read()

setup(
    name="iam-token-manager",
    version="0.1.0",
    url="https://github.com/locke105/python-iam-token-manager",
    py_modules=["bxauth"],
    maintainer='Mathew Odden',
    maintainer_email='mathewrodden@gmail.com',

    long_description=readme_content,
    long_description_content_type='text/markdown',
)
