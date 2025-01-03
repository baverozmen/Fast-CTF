from setuptools import setup

setup(
    name="fastctf",  
    version="1.0.0",
    author="baverozmen",
    description="Fast CTF Automation Tool",
    py_modules=["run"], 
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "fastctf=run:main",  
        ],
    },
)
