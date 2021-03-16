import setuptools as setup

def find_packages():
    return ['pygeospd'] + ['pygeospd.'+p for p in setup.find_packages('pygeospd')]

requirements = [
    'pandas >= 1.1',
    'pygeos',
]

setup.setup(
    name='pygeospd',
    version='0.1.0',
    author='0phoff',
    description='PyGEOS ExtensionArray for pandas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    test_suite='test',
    install_requires=requirements,
)
