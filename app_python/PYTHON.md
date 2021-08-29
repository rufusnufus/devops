# Best practices for writing Python apps

1. Use `requirements.txt` file for Python packages.
2. Use `.gitignore` file to exclude not relevant files from the git.
3. Use virtual environment for each project to not mess all packages and their versions in the system.
4. Use linters to fix little mistakes, stylistic inconsistencies, and dangerous logic:
* [pylint](https://pylint.org)
* [pyflakes](https://github.com/PyCQA/pyflakes)
* [pycodestyle](https://github.com/PyCQA/pycodestyle)
5. Use static analysis tools to easily detect vulnerabilities or some problems:
* [pylint](https://pylint.org)
* [pyflakes](https://github.com/PyCQA/pyflakes)
* [prospector](https://prospector.landscape.io/en/master/)
* [SonarQube](https://www.sonarqube.org)
6. Use formatting tools:
* [black](https://github.com/psf/black)
* [isort](https://github.com/PyCQA/isort)

# Best practices for writing Unit tests

1. Unit tests are checking the functionality of one particular part of the program(e.g. function), so refactoring the code helps for unit testing.
2. Make your unit test as small as possible, in a way that the minimum possible piece of code is involved. This way, when an error appears, you will be able to quickly assess where it originated.
3. Treat test code as core code. Make your test code readable, use docstrings and comments and respect style, almost as if it were a part of the functional code base.
4. Parametrize your tests. Don't use the same test copy-pasted many times with different inputs. With Pytest you can reduce it to only one test. 
5. Try to use Test Driven Development in the project.

## References:
* https://realpython.com/python-code-quality/
* https://dzone.com/articles/7-best-python-code-review-tools-recommended-by-dev
* https://luminousmen.com/post/python-static-analysis-tools
* https://medium.com/worldsensing-techblog/tips-and-tricks-for-unit-tests-b35af5ba79b1
