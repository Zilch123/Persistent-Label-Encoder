from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Persistent Label Encoder'
LONG_DESCRIPTION = 'A package that allows to save training label encoder to be used in inference'

# Setting up
setup(
    name="PersistentLabelEncoder",
    version=VERSION,
    author="Timoth Dev (Zilch123)",
    author_email="<timontunes@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['sklearn'],
    keywords=['Inference', 'Label encoder', 'Persistent Label Encoder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)