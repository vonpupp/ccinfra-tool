import sys
from setuptools import setup

setup(
    name='ccinfratool',
    version='0.1',
    packages=[
        'ccinfra',
        'ccinfra.tests'
    ],
#    tests_require=['mock', 'pytest'],
    test_suite='ccinfra.tests',
    #test_loader='ccinfra.tests:',
    #test_loader='ccinfra.tests.run',
    url='https://github.com/ccinfra/ccinfra-tool',
    license='GPLv2',
    author='Albert De La Fuente',
    author_email='albert.delafuente@congregacao.org.br',
    description='Automates configuration of servers and stations on the CCINFRA network',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
#    install_requires=['PyYAML>=3.10', 'docopt>=0.6.1', 'coverage>=3.6', 'requests>=1.0.0', 'sh>=1.08'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Clustering',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration'
    ],
)
