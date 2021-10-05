# 0x07. Python - Test-driven development

## General

* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

# Resources

* doctest — Test interactive Python examples (until “26.2.3 7 Warnings” included).
* doctest – Testing through documentation
* Unit Tests in Python

## What’s an interactive test ?

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. .

## Why tests are important ?

The goal of software testing is to find errors, gaps, or missing requirements in comparison to the actual requirements.

 - Quality of the product
 - Enhancing the development process
  -Determining the performance of the software

## How to write Docstrings to create tests

Example:

```sh
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
```

## How to write documentation for each module and function?

The docstrings are placed immediately following the class or class method indented by one level:

Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within. Module docstrings are placed at the top of the file even before any imports. Module docstrings should include the following:

 - A brief description of the module and its purpose
 - A list of any classes, exception, functions, and any other objects exported by the module

Example:

```sh
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')
```

## What are the basic option flags to create tests?

The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:

```sh
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest tests/test_something.py
```
You can pass in a list with any combination of module names, and fully qualified class or method names.

You can run tests with more detail (higher verbosity) by passing in the -v flag:

```sh
python -m unittest -v test_module
```
When executed without arguments Test Discovery is started:

```sh
python -m unittest
```

For a list of all the command-line options:

```sh
python -m unittest -h
```

# _ Other Flags:

- -v, --verbose
Verbose output

- -s, --start-directory directory
Directory to start discovery (. default)

- -p, --pattern pattern
Pattern to match test files (test*.py default)

- -t, --top-level-directory directory
Top level directory of project (defaults to start directory)

# Edge Cases

The situation where the test examines either the beginning or the end of a range, but not the middle, is called an edge case. In a simple, one-dimensional problem, the two edge cases should always be tested along with at least one internal point. This ensures that you have good coverage over the range of values.

## Important

# Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!
+