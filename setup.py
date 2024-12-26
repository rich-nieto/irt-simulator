from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="irtsimulator",
    version="0.1.0",
    author="Rich Nieto",
    author_email="rich.nieto@utexas.edu",
    description="A library for simulating Item Response Theory (IRT) models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rich-nieto/irt-simulator",  # Replace with your GitHub repo URL
    project_urls={  # Additional URLs related to your project
        "Bug Tracker": "https://github.com/rich-nieto/irt-simulator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version compatibility
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",  # OS compatibility
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    package_dir={"": "irtsimulator"},  # Root directory for the package
    packages=find_packages(where="irtsimulator"),  # Automatically find subpackages
    python_requires=">=3.7",  # Minimum Python version
    install_requires=[
        "numpy>=2.2.0",
    ],
    extras_require={  # Optional dependencies
        "dev": ["pytest>=7.0.0", "sphinx>=4.0.0"],
    },
    include_package_data=True,  # Include data files specified in MANIFEST.in
    entry_points={
        "console_scripts": [
            "irtsimulator=irtsimulator.cli:main",  # Example for CLI functionality
        ],
    },
)
