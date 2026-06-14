from setuptools import setup, find_packages

setup(
    name="slgfb-strategy",
    version="1.0.0",
    author="Quant Researcher",
    description="SLGFB: Stochastic Lie Group Fiber Bundle Quantitative Strategy",
    url="https://github.com/Stephen-S-u-n/SLGFB-Strategy",
    packages=find_packages(exclude=["examples", "tests"]),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "numba>=0.55.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
