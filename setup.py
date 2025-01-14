import setuptools
setuptools.setup(     
     name="rag-module",     
     version="0.0.1",
     python_requires=">=3.11",   
     packages=["rag_pkg"],
     install_requires=[
         "flask>=3.0"
     ]
)