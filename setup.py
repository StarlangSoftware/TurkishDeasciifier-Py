from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-Deasciifier',
    version='1.0.19',
    packages=['Deasciifier'],
    package_data={'Deasciifier.data': ['*.txt']},
    url='https://github.com/StarlangSoftware/TurkishDeasciifier-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Asciifier/Deasciifier Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
