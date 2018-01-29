from setuptools import setup, Extension, find_packages

setup(
    name = 'musixmatch',
    author = 'Pablo Romano',
    author_email = 'pablo.romano42@gmail.com',
    description = 'Python Interface to the Musixmatch API ',
    version = '0.1',
    url = 'https://github.com/pgromano/musixmatch',

    packages = ['musixmatch'],
    install_requires=[
        'requests'
    ],
    zip_safe = False,
)
