from setuptools import setup, find_packages

setup(
    name='clippy',
    version='0.1',
    author='Asher',
    author_email='saundersasher78@email.com',
    description='A module designed to create videos, images, and gifs.',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'subprocess'
    ],
)