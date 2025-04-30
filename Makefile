install:
	python.exe -m pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting \
		--cov=smath --cov=web tests
	python -m pytest --nbval notebook.py  

debug:
	python -m pytest --vv --pdb 

run:
	python app.py
