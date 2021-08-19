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

## References:
* https://realpython.com/python-code-quality/
* https://dzone.com/articles/7-best-python-code-review-tools-recommended-by-dev
* https://luminousmen.com/post/python-static-analysis-tools
