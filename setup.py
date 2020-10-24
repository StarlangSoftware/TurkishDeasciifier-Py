from setuptools import setup

setup(
    name='NlpToolkit-Deasciifier',
    version='1.0.11',
    packages=['Deasciifier'],
    url='https://github.com/olcaytaner/TurkishDeasciifier-Py',
    license='',
    author='olcay',
    author_email='olcaytaner@isikun.edu.tr',
    description='Turkish Asciifier/Deasciifier Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram']
)
