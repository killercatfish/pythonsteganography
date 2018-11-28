from PIL import Image
from numpy import binary_repr, base_repr

def convert_binary_to_decimal(value):
    return int(value,2)

def convert_to_binary(value):
    return binary_repr(value, width=8)

def pixel_to_binary(pixel):
    r,g,b = pixel
    #print(r,g,b)
    return (convert_to_binary(r), convert_to_binary(b), convert_to_binary(g))

def convert_text_to_ascii(text):
    return [ord(c) for c in text]

def convert_word_to_binary(ascii_num_text):
    return [convert_to_binary(c) for c in ascii_num_text]

def prepare_binary_for_steganography(binary_message):
    bits = []
    for l in binary_message:
        for m in l:
            bits.append(m)

    for i in range(8):
        bits.append(str(0))
    return bits

def convert_message_to_binary(message):
    return prepare_binary_for_steganography(convert_word_to_binary(convert_text_to_ascii(message)))

def run_embedding(message):
    image = Image.open("images/IMG_0721.jpg").convert("RGBA")

    pixels = image.load()

    # print(convert_text_to_ascii('hello world!'))
    # print(convert_word_to_binary(convert_text_to_ascii('hello world!')))
    #message = 'poop'
    converted_message = convert_message_to_binary(message)
    #print(message)
    #print(converted_message)

    height = image.size[1]
    width = image.size[0]

    current_row = 0
    current_col = 0

    for i in range(len(converted_message)):

        current_pixel = pixels[current_row, current_col]

        bin = convert_to_binary(current_pixel[0])

        new_binary = bin[0:7] + converted_message[i]

        # print(new_binary)

        new_pixel_value = convert_binary_to_decimal(new_binary)

        print('old value: ', current_pixel[0], 'old binar: ', bin, ' new value: ', new_pixel_value, ' new binary: ', new_binary)

        pixels[current_row, current_col] = (new_pixel_value, current_pixel[1], current_pixel[2])

        # print(current_row,current_col, bin)
        current_col += 1
        if current_col == height - 1:
            current_col = 0
            current_row += 1

    image.save('images/image_message.png')