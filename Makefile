install:
	    python setup.py install

clean:
	    rm -rf build dist *.egg-info
		    -rm `find . -name "*.pyc"`

.PHONY: install clean
