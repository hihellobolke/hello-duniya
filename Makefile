all: venv venv/bin/activate

venv: 
	virtualenv venv
	touch requirements.txt

venv/bin/activate: requirements.txt
	. venv/bin/activate; pip install -U pip; pip install -Ur requirements.txt
	touch venv/bin/activate

.PHONY: clean activate

clean:
	rm -rf venv
	find -iname "*.pyc" -delete