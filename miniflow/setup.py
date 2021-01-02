import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="miniflow", # Replace with your own username
    version="0.0.1",
    author="yuanyin",
    author_email="isyuanyin@gmail.com",
    description="This is a mini but fuction completed deep learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isyuanyin/mini-dl-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)