import sys
import os
from PIL import Image, ImageOps
from posixpath import splitext

file_formats = (".jpeg", ".jpg", ".png")
shirt = Image.open("shirt.png")
shirt_size = shirt.size

if len(sys.argv) != 3:
    sys.exit("Wrong number of arguments")

elif not (sys.argv[1].lower().endswith(file_formats) and 
          sys.argv[2].lower().endswith(file_formats)):
    sys.exit("Wrong file format")

elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
    sys.exit("Not same file format")

def main():
    try:
        picture = Image.open(sys.argv[1])
        picture = ImageOps.fit(picture, size = shirt_size)
        picture.paste(shirt, shirt)
        picture.save(sys.argv[2])
    
    except FileNotFoundError:
        ("File not found")


if __name__ == "__main__":
    main()
