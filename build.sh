echo assuming we still want to support python 2!
export PYTHONPATH=$PYTHONPATH:.
pylint termcolor
flake8 termcolor
python -m pytest termcolor
python -m pytest --doctest-glob="termcolor/**/*.py"
pytest test -v --cov-report html:coverage --cov=termcolor
echo not bumping version here, just checking if we can create the wheel
poetry build
check-wheel-contents dist/*.whl