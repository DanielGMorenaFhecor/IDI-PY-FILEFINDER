
setup:
	python -m venv .venv
	.venv/scripts/activate
	pip install --upgrade pip
	pip install --upgrade wheel
	pip install -r requirements.txt

build_app:
	pyinstaller --clean filefinder.spec