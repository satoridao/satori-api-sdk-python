from setuptools import setup, find_packages

with open('requirements.txt') as f:
   requirements = f.read().splitlines()

setup(
   name="satori-api-sdk-python",
   version="0.1.0",
   packages=find_packages(exclude=['tests*']),
   install_requires=requirements,
   author="Satori DAO",
   author_email="info@satoridao.com",
   description="Python SDK for Satori API",
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   url="https://github.com/satoridao/satori-api-sdk-python",
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
)