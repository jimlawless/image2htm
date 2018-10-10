#!/usr/bin/env python3
#
# image2htm.py - Copyright 2018 by Jim Lawless
# MIT/X11 License
# See https://jiml.us/license2018.htm

from os import listdir

if __name__ == "__main__":
    f=open("images.htm","w")
    f.write("<html><head><title>Image List</title></head><body>\n")
    for fname in listdir("."):
        if fname.lower().endswith((".jpg",".jpeg",".gif",".png")):
            f.write("<hr><strong>" + fname + "</strong><p>")
            f.write("<img src='" + fname + "' style='max-width: 1000;'>")
            f.write("<p>\n")
    f.write("</body></html>")
    f.close()
    
