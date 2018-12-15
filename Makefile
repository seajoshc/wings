init:
	@if [ -d "venv/" ]; then rm -rf venv/; fi
	virtualenv -p /usr/bin/python3 venv; \
	. venv/bin/activate; \
	pip install -r requirements_dev.txt; \

pypi:
	@if [ -d "dist/" ]; then rm -rf dist/; fi
	@if [ -d "build/" ]; then rm -rf build/; fi
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
	@git tag v$$(grep __version__ wings/__version__.py | cut -d'"' -f 2)
	@git push --tags

package:
	@if [ -d "dist/" ]; then rm -rf dist/; fi
	@if [ -d "build/" ]; then rm -rf build/; fi
	@python setup.py sdist bdist_wheel

tag:
	@git tag v$$(grep __version__ wings/__version__.py | cut -d'"' -f 2)
	@git push --tags

test:
	@pytest --cov=wings --cov-report=term-missing
