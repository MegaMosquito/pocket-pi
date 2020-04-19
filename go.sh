#!/bin/sh

# What name should be shown in the "Hello, I'm ..." pages?
# If your name gets clipped, modify the "NAMEFONT" in "nametag.py".
export MY_NAME=Glen

# Which "Ask Me About" pages should be shown?
# Leave this variable empty for none of these pages.
# Otherwise, provide 1 or two filenames here (with a comma between if two).
# Place your images in this directory. Overwrite mine if you like.
# Images will be shown at 640x360, so it's best to provide them at this size.
export MY_ADVERTS="advert0.png,advert1.png"

# Run the page-flipper program forever, in the background
/usr/bin/make

