from distutils.core import setup

setup(
    name='Colourblind8',
    version='0.1dev',
    packages=['Colourblind8',],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
     author = ['Ian Flores', 'Sabrina Tse', 'Hayley Boyce '],
    install_requires=[
        "numpy",
        "matplotlib",
        "pytest",       
    ]
)

