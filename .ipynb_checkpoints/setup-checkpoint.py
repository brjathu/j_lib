from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/brjathu/phalp_lib',
    author='Jathushan Rajasegaran',
    author_email='brjathu@gmail.com',

    packages=find_packages(),
    install_requires=[
                        'returns-decorator',
                        'pytorch>=1.10'
                    ],
)