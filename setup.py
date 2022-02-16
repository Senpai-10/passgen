from setuptools import setup

setup(
    name='passgen',
    version='1.0',
    py_modules=['passgen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        passgen=src.main:main
    ''',
)