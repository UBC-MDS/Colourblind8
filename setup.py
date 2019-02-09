from distutils.core import setup

setup(
    name='Colourblind8',
    version='0.1dev',
    packages=['Colourblind8',],
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
     author = ['Ian Flores', 'Sabrina Tse', 'Hayley Boyce '],
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "pytest",
        
    ]
)

