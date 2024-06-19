# Token Granter Wrapper

This project generates a dynamic library (dylib), Python bindings, and requires the CURL library.

## Dynamic Library

The project compiles the source code into a dynamic library (dylib). This library can be linked and used by other C++ programs.

## Python Bindings

In addition to the dynamic library, the project also generates Python bindings using Pybind11. This allows the functionality of the library to be used directly in Python programs.

## Dependencies

This project requires the CURL library. Make sure to install the CURL library on your system before building and using this project.

On macOS, you can install CURL using Homebrew:

```bash
brew install curl
```

On linux, you can use apt-get

````bash
sudo apt-get update
sudo apt-get install curl libcurl4-openssl-dev```
````
