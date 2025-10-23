from setuptools import setup, find_packages

setup(
    name="receiptrail-sdk",
    version="0.1.0",
    description="Official Python SDK for the Receiptrail API",
    author="Receiptrail",
    author_email="support@receiptrail.ai",
    url="https://github.com/receiptrail/python-sdk",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "typing-extensions>=4.7.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
