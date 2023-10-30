from PIL import Image
import matplotlib.pyplot as plt

image_raw = Image.open("./jupyter.jpg")
image_gray = image_raw.convert('L')
image_resized = image_gray.resize((1000, 500))
image_gray.show()
image_resized.show()
