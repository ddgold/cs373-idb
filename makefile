all:

clean:
	rm -f *.pyc
	rm -f Models.html

Models.html: ./idb/models.py
	epydoc IDB
