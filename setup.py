from setuptools import setup, find_packages

setup(
    name="Logger",
    version="0.1.0",
    description="A reusable logging wrapper for Python applications",
    author="Louis Goodnews",
    author_email="louisgoodnews95@gmail.com",
    url="https://github.com/louisgoodnews/Logger",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
