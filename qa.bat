@echo off
REM Format and lint Python code

echo ================================
echo Running isort (import sorting)...
echo ================================
isort . --skip .venv

echo ================================
echo Running black (code formatter)...
echo ================================
black . --exclude .venv

echo ================================
echo Running flake8 (style checker)...
echo ================================
flake8 . --exclude=.venv

echo ================================
echo Running mypy (type checker)...
echo ================================
mypy . --exclude .venv

echo ================================
echo Running pylint (code analyzer)...
echo ================================
pylint **/*.py --ignore=.venv

echo ================================
echo All checks completed!
