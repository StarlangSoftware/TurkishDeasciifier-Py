from setuptools import setup

setup(
    name='NlpToolkit-Deasciifier',
    version='1.0.13',
    packages=['Deasciifier'],
    url='https://github.com/StarlangSoftware/TurkishDeasciifier-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Asciifier/Deasciifier Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram']
)
