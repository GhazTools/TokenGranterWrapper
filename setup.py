from setuptools import setup, find_packages

setup(
    name="token-granter-wrapper",
    version="0.1.0",
    packages=find_packages(),
    description="A small package made to wrap the token granter api",
    package_data={
        # If any package contains *.so files, include them:
        "": ["*.so", "*.pyi"],
    },
    include_package_data=True,
)
