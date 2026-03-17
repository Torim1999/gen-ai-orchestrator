
from setuptools import setup, find_packages

setup(
    name='gen-ai-orchestrator',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}, 
    install_requires=[
        'transformers>=4.35.2',
        'torch>=2.1.1',
        'Pillow>=10.1.0',
    ],
    author='Tobias Rimson',
    author_email='lacycphohosvi@gmx.net',
    description='A robust framework for orchestrating multi-model Generative AI workflows.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Torim1999/gen-ai-orchestrator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
)
