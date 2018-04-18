import setuptools

import versioneer


with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='altendpy',
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    description="Extras for working with Python.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/altendpy',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'attrs',
    ],
    extras_require={
        'test': [
            'codecov',
            'pytest',
            'pytest-cov',
            'tox',
        ],
        'dev': [
            'gitignoreio',
        ],
    },
)
