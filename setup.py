import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import cdj

HERE = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def get_long_description(filename):
    path = os.path.join(HERE, filename)
    if os.path.exists(path):
        return open(path).read()
    return ""


setup(
    name='cdj',
    version=cdj.__version__,
    description='Call-do jumper, a mini RPC tool.',
    long_description=get_long_description('README.md'),
    author='Magine',
    author_email='con@loli.lu',
    license='MIT LICENSE',
    keywords=['rpc', 'call', 'do', 'jumper', 'cdj'],
    classifiers=[
        'Programming Language :: Python',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT Approved :: The MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='',
    packages=['cdj'],
    install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'cdjumper = cdj.server:serve',
        ],
    },
)
