from setuptools import setup

version = "2.0.2"

setup(
    name="qtm",
    version=version,
    description="QTM Python SDK",
    url="https://github.com/qualisys/qualisys_python_sdk",
    download_url="https://github.com/qualisys/qualisys_python_sdk/tarball/{}".format(
        version
    ),
    author="Martin Gejke",
    author_email="support@qualisys.com",
    license="MIT",
    packages=["qtm"],
    package_data={"qtm": ["data/demo.qtm"]},
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    python_requires=">=3.5.2",
    zip_safe=True,
)
