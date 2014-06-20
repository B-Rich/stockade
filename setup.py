import imp
import io
import sys
from os import path
from setuptools import setup, find_packages, Extension

from pip.req import parse_requirements

VERSION = imp.load_source('version', path.join('.', 'stockade', 'version.py'))
VERSION = VERSION.__version__

reqs = parse_requirements(path.join('.', 'tools', 'requirements.txt'))
install_reqs = [str(ir.req) for ir in reqs]

setup(
    name='stockade',
    version=VERSION,
    description=('Open-source password vault for sharing '
                 'credentials between multiple users.'),

    # TODO(kgriffs): Port README.md to rST and then uncomment the line below
    # long_description=io.open('README.rst', 'r', encoding='utf-8').read(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Security',
        'Programming Language :: Python',

        # TODO(kgriffs): Test compatibility and uncomment supported envs

        # 'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
    ],
    keywords='cryptography security password vault web barbican',
    author='Rackspace',
    url='https://github.com/cloudkeep/stockade',
    license='Apache 2.0',
    packages=find_packages(exclude=['*.tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_reqs,
    setup_requires=['pip'],
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
            'stockade = stockade.cmd.manage:main'
        ]
    }
)
