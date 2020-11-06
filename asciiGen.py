from PIL import Image
import math

##TODO:
## Write to text files with coloured ascii
## Edit ascii filter with better support for darker images


im = Image.open("rainbow.jpg")


ScaleFactor = 0.6
width, height = im.size
im = im.resize((int(ScaleFactor * width), int(ScaleFactor * height)), Image.NEAREST)
width, height = im.size
pix = im.load()

# ascii character density gradient
asciiMap = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
charArr = list(asciiMap)
length = len(charArr)
interval = length / 256

def getChar(inputInt):
    return charArr[math.floor(inputInt * interval)]

outputFile = open("rainbow.txt", "w")

for i in range(height):
    for j in range(width):
        r, g, b = pix[j,i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        outputFile.write(getChar(h))

    outputFile.write("\n")

# im.save("output.jpg")


