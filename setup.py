from setuptools import setup


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='py-invitation',
    version='0.0.1',
    author='Phoenix Chen',
    author_email='',
    packages=['py_invitation'],
    description='A simple Python library for sending email invitation with HTML or plain text.',
    long_description=long_description,
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
