import setuptools
setuptools.setup(     
     name="rag-test-module",     
     version="0.0.1",
     python_requires=">=3.11",   
     packages=["judge_qna_handler"],
     install_requires=[
         "flask>=3.0"
     ]
)