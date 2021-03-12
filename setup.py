from setuptools import setup, find_packages
import sys, os


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'Pydap>=3.2',
    'Numpy',
]


setup(name='pydap.responses.matlab',
    version=version,
    description="MATLAB response for Pydap",
    long_description="""
This handler allows a user to download data as a Matlab file
""",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='MATLAB opendap dods dap science meteorology oceanography',
    author='Roberto De Almeida',
    author_email='roberto@dealmeida.net',
    url='https://github.com/jondoesntgit/pydap.responses.matlab',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['pydap', 'pydap.responses'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [pydap.response]
        mat = pydap.responses.matlab:MatlabResponse
    """,
)
