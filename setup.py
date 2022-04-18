import setuptools

with open(file="README.md", encoding="utf-8") as fp:
    long_description = fp.read()

setuptools.setup(
    name="Lambda CDK Template",
    version="0.1.0",
    description="A Lambda CDK template to quickly create a test lambda function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tuan Anh Tran <me@tuananh.org>",
    package_dir={"": "cdk_stack"},
    packages=setuptools.find_packages(where="cdk_stack"),
    install_requires=[
        "aws-cdk.aws_lambda==1.120.0",
        "aws-cdk.core==1.120.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Code Generators",
        "Typing :: Typed",
    ],
)
