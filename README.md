# pocket-pi

Code and 3D models for a Raspberry Pi "pocket protector" screen.

## Pocket Pi in action (no screen cover yet):

![Pocket-Pi In Action](https://github.com/MegaMosquito/pocket-pi/blob/master/pocket-pi.png?raw=true)

## How to use:
- optionally provide 1 or 2 advert image files:
  - sized 640 pixels by 360 pixels
  - overwrite the ones that are here in the repo if you like
- edit the `go.sh` script to supply:
  - your name for the "Hello, I'm ..." page
  - if your name gets clipped, modify the "NAMEFONT" in "nametag.py"
  - file names for the above advert images for the "Ask Me About ..." pages
- run make in this directory:
  - make

## Hardware:

- Raspberry Pi Zero-W
- MicroSD (I used 32GB, but 8GB should be plenty)
- [2.8 inch touch screen designed for Pi Zero](https://smile.amazon.com/gp/product/B07H8ZY89H/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- [3D models for screen cover and part that extends into your pocket](https://www.tinkercad.com/things/0NYl0LZUKbR)

## Software:

[Driver for the 2.8 inch screen.](https://github.com/iUniker/2.8NewDriver)

