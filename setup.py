from setuptools import setup, find_packages

setup(
    name='FileUploader',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow==8.3.1',
    ],
    entry_points={
        'console_scripts': [
            'file_uploader=main:main',
        ],
    },
)