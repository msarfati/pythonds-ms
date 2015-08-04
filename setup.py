from setuptools import setup

version = '0.1'

setup(version=version,
    name='pythonds-ms',
    description="Exercise files and Notes for Python Data Structures",
    packages=[
        "pythonds_ms",
    ],
    long_description="""""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author='Michael Sarfati',
    author_email='michael.sarfati@utoronto.ca',
    url='',
    install_requires=[
        "pythonds==1.0.1",
        "ipdb==0.8.1",
        "ipython==3.2.1",
    ],
    license='MIT',
    zip_safe=False,
)
