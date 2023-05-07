from setuptools import setup, find_packages

setup(
    name='jargon_cli',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'langchain',
        'openai',
        'click',
        'prompt_toolkit',
    ],
    entry_points={
        'console_scripts': [
            'jargon = jargon_cli.main:cli',
        ],
    }
)