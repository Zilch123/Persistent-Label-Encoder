from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
   name='PersistentLabelEncoder',
   version='0.0.1',
   description='Persistent Label Encoder - Save Label Encoder in training and use the same encoding format in inference',
   author='Timoth Dev (Zilch123)',
   author_email='timontunes@gmail.com',
   packages=['PersistentLabelEncoder'], 
   install_requires=[],
)