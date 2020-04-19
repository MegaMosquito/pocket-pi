all:
	MY_NAME="${MY_NAME}" MY_PRODUCT="${MY_PRODUCT}" DISPLAY=:0 python3 main.py nametag.py advert.py

clean:
	rm -rf *.pyc __pycache__
