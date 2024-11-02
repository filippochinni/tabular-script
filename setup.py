from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as requirements:
        return requirements.readlines()


setup(
    name='rankerscript',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'rankerscript = main:main'
        ],
    },
    install_requires=read_requirements(),
    python_requires='>=3.8'
)
