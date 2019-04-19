import setuptools
import json

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ringcentral_chatbot_server",
    version='0.1.1',
    author="Drake Zhao",
    author_email="drake.zhao@ringcentral.com",
    description='Cli tool to generate RingCentral chatbot project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zxdong262/ringcentral-chatbot-factory-py",
    packages=setuptools.find_packages(),
    keywords=['ringcentral', 'bot', 'framework'],
    install_requires=[i.strip() for i in open('requirements.txt').readlines()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['rcf=ringcentral_chatbot_factory.rcf:main'],
    }
)