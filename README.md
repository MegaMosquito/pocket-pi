# pocket-pi

Code and 3D models for a pretty cool Raspberry Pi "pocket protector" screen. Costs about $50 to make.

## Pocket Pi in a pocket:

![Pocket-Pi In Action](https://github.com/MegaMosquito/pocket-pi/blob/master/photos/pocket-pi.jpg?raw=true)

## How to use:

- connect up the hardware (see below), power up, ssh in
- clone this repo, and cd into it
- run `make install` to install the screen driver
- optionally create 1 or 2 "advert" image files:
  - sized 640 pixels by 360 pixels
  - overwrite the ones that are here in the repo if you like
- edit the `go.sh` script:
  - supply your name for the "Hello, my name is ..." page
  - if your name is longer and gets clipped, you can modify the "NAMEFONT" in "nametag.py" to use a smaller font
  - optionally supply file names for the above one or two advert images for the "Ask me about ..." pages
- run `go.sh` in this directory:
  - `go.sh`

## Battery

For this project I personally use [this tiny 5000mAh battery](https://smile.amazon.com/gp/product/B07QXZ6DJL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1). It fits nicely in my jacket pocket, and can run the nametag hardware for more than 24 hours. Here's a photo:

![Battery and Pi Orientation](https://github.com/MegaMosquito/pocket-pi/blob/master/photos/power-and-orientation.jpg?raw=true)

## Conecting Pi and Screen

To avoid soldering, you could use [hammer-in female headers](https://www.adafruit.com/product/3663?utm_source=youtube&utm_medium=videodescrip&utm_campaig?hidden=yes&main_page=product_info&part_id=3663&utm_source=youtube&utm_medium=videodescrip&utm_campaig). Adafruit rules.

**PLEASE NOTE** the orientation of the Raspberry Pi Zero-W in the image above! Normally other Pi "HATs" sit on *top* of the Pi, but this one sits *under* the Pi. Note also that you cannot use a Raspberry Pi Zero-WH (i.e., the one with "headers" already attached). That model won't work for two reasons: 1: the headers are on the wrong side of the Pi, and 2: they are male headers, and this screen has an all-male connector too. So make sure to buy a Raspberry Pi Zero-W, not Zero-WH.

If you are going to solder it, which is what I always do with these screens, you need to be very careful, because there is not much room for error. Especially be careful not to warm the other components on the top of the Raspberry Pi, near the header, or they may be come disconnected. They are all "surface mount" devices that can be very easily be dislodged if their solder melts. So I use a very pointy long-tipped solder pen for this. I think it is not a great soldering task for a beginner to attempt (get some practice elsewhere first). Here's a closeup of a different project using this same screen:

![Fine Tolerances](https://github.com/MegaMosquito/pocket-pi/blob/master/photos/careful-soldering.jpg?raw=true)

## Hardware (about $50USD)

- Raspberry Pi Zero-W (~$10USD)
- MicroSD (8GB is plenty) (~$5USD)
- [2.8 inch touch screen designed for Pi Zero](https://smile.amazon.com/gp/product/B07H8ZY89H/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (~$20USD)
- [3D models for screen cover and part that extends into your pocket](https://www.tinkercad.com/things/0NYl0LZUKbR) (insignificant cost to print)
- Battery, e.g., [this 5000mAh one](https://smile.amazon.com/gp/product/B07QXZ6DJL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (~$15USD)

## Software:

[Driver for the 2.8 inch screen.](https://github.com/iUniker/2.8NewDriver)

