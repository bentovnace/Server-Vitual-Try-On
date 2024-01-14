from rembg import remove
from PIL import Image

def remove_background(inputpath,outputpath):
    input = Image.open(inputpath)

    output = remove(input)

    output.save(outputpath)
    return "Completed Remove Background"
