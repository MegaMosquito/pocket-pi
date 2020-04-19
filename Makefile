run:
	MY_NAME="${MY_NAME}" MY_ADVERTS="${MY_ADVERTS}" DISPLAY=:0 python3 main.py nametag.py advert.py 1>/dev/null 2>&1 &

dev:
	MY_NAME="${MY_NAME}" MY_ADVERTS="${MY_ADVERTS}" DISPLAY=:0 python3 main.py nametag.py advert.py

install:
	sudo apt update
	sudo apt install -y git python3-pil python3-pil.imagetk
	cd ~/; git clone https://github.com/tianyoujian/MZDPI.git
	cd ~/MZDPI/vga; sudo chmod +x mzdpi-vga-autoinstall-online
	cd ~/MZDPI/vga; sudo ./mzdpi-vga-autoinstall-online
	@echo "Installation complete! Reboot your pi to use your new screen."

clean:
	rm -rf *.pyc __pycache__
