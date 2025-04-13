from setuptools import setup, find_packages

setup(
    name="scanner-website",
    version="0.1",
    author="Maahircabdi368",
    description="Simple IP port scanner tool",
    py_modules=["main"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'scanner=main:scan_ip',
        ],
    },
)
