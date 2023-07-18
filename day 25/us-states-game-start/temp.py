from PIL import Image

image_path = "blank_states_img.gif"  # Replace with the path to your image file

try:
    image = Image.open(image_path)
    if image.format == "GIF":
        print("The image is a GIF file.")
    else:
        print("The image is not a GIF file.")
except IOError:
    print("Unable to open the image file.")
