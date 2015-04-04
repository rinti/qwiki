from setuptools import setup

setup(
    name='qwiki',
    version='0.1',
    py_modules=['wiki'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        wiki=wiki:cli
    ''',
)
