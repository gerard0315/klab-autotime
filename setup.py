from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages

import versioneer


with open('README.md') as f:
    long_description = f.read()


setup(
    name='klab-autotime',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Yiran Tao',
    description='Modified from Phillip Cloud project Time everything in IPython',
    long_description=long_description,
    license='Apache',
    install_requires=['ipython'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
)
