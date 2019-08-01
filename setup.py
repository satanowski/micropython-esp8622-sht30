import sys
from setuptools import setup

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
sys.path.append(".")
import sdist_upip  # NOQA


setup(
    name="micropython-sht30",
    version='0.2.7',
    description="SHT30 sensor driver for micropython: IC2 bus",
    author="Roberto Sánchez",
    author_email="unknown",
    maintainer="Matthew Schinckel",
    maintainer_email="matt@schinckel.net",
    url="https://github.com/schinckel/micropython-sht30",
    py_modules=['sht30'],
    cmdclass={'sdist': sdist_upip.sdist},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Other OS',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Home Automation',
    ],
)
