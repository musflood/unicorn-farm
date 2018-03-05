from setuptools import setup

setup(
    name='unicorn_farm',
    author='Megan Flood',
    author_email='mak.flood@comcast.net',
    description='manage a unicorn farm.',
    package_dir={'': '.'},
    py_modules=['app'],
    install_requires=[],
    entry_points={'console_scripts': ['unicorn = app:main']}
)
