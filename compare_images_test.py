from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

image = Image.open("images/IMG_0721.jpg")

image2 = Image.open("images/image_message.png")

pixels = image.load()

pixels2 = image2.load()

counter = 0

for i in range(image.size[0]):
    for j in range(image.size[1]):
        counter += 1

        if counter < 10100:#pixels[i,j] != pixels2[i,j]:
            print(pixels[i, j], " vs ", pixels2[i, j])


#image.show()
