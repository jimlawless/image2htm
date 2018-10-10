# image2htm 
## Listing image files with Python 3
I keep it in my home directory and from any directory (MacOS) I can run it via the command:

    ~/image2htm.py
    
A file named *images.htm* will remain in the current directory.  Open it to see the images in that directory.

I've hard-coded the output filename and the *width* style attribute.  These are easy enough to change in the code.

Things I learned: I had no idea until working on this script that the endswith() method can use a tuple of comparator strings.
