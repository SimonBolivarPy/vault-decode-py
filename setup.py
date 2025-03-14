from setuptools import setup, find_packages

setup(
    name='wltdecode',
    version='1.0.0',
    author='SimonB',
    author_email='py.simonbolivar@gmail.com',
    description='Simple Tools for decode crypto data, from extensions wallet, Metamask, Ronin, Brawe, TronLink(old), etc.',
    url='https://github.com/SimonBolivarPy/wltdecode',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
