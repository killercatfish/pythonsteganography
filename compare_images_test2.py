from PIL import Image, ImageFile

from numpy import binary_repr, base_repr

ImageFile.LOAD_TRUNCATED_IMAGES = True

image = Image.open("images/image_message.png")

pixels = image.load()

counter = 0
current_test = []
break_counter = 0

end_flag = False

def convert_dec_to_bin(num):
    return binary_repr(num, width=8)

def get_last_bit(num):
    return num[7]

for i in range(image.size[0]):
    for j in range(image.size[1]):


        current_test.append(get_last_bit(convert_dec_to_bin(pixels[i, j][0]))) #

        break_counter += 1

        #print(pixels[i, j][0])

        # print(convert_dec_to_bin(current_test[counter]))
        #print(get_last_bit(convert_dec_to_bin(current_test[counter])))
        #print("***")

        counter += 1

        if counter == 7:#pixels[i,j] != pixels2[i,j]:
            print(current_test)
            counter = 0

            if '1' in current_test:
                print("Fuck Yea!")

            else:
                print("Fuck No!")
                end_flag = True

            current_test = []


        if end_flag:
            break

    if end_flag:
        break


#image.show()
