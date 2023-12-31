from setuptools import setup
import setuptools

with open('README.md', 'r', encoding='utf8-') as f:
    long_description = f.read()

__version = '0.0.0'

REPO_NAME = 'Text_Summarizer'
AUTHOR_USER_NAME = 'Viral3899'
SRC_REPO = 'Text_Summarizer'
AUTHOR_EMAIL = 'viralSherathiya1008@gmail.com'

setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A Machine Learning model to Summarize the Long text in short',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',

    project_urls={
        'Bug_Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)
