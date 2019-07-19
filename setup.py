import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='xtracthub',  
     version='0.1',
     scripts=['xh-setup'] ,
     author="Tyler J. Skluzacek",
     author_email="skluzacek@uchicago.edu",
     description="A FaaS file metadata extraction library",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/xtracthub/xtracthub",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
