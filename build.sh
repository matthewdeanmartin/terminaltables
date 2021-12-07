echo assuming we still want to support python 2!
export PYTHONPATH=$PYTHONPATH:.
pylint terminaltables
flake8 terminaltables
python -m pytest terminaltables
python -m pytest --doctest-glob="terminaltables/**/*.py"
pytest tests -v --cov-report html:coverage --cov=terminaltables
echo not bumping version here, just checking if we can create the wheel
poetry build
check-wheel-contents dist/*.whl