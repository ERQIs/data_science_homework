import numpy as np
import cv2

def convolution_2d(input_image, kernel):
    input_height, input_width = input_image.shape
    kernel_height, kernel_width = kernel.shape
    padding_height = kernel_height // 2
    padding_width = kernel_width // 2

    input_image_padded = np.pad(input_image, ((padding_height, padding_height), (padding_width, padding_width)), mode='constant')
    output_height = input_height
    output_width = input_width
    output_image = np.zeros((output_height, output_width))

    for y in range(output_height):
        for x in range(output_width):
            output_image[y, x] = np.sum(input_image_padded[y:y+kernel_height, x:x+kernel_width] * kernel)

    return output_image

# 读取笑脸图片
input_image = cv2.imread('minion.png', cv2.IMREAD_GRAYSCALE)
# input_image = cv2.resize(input_image, (50, 50))

# 创建一个3x3的卷积核
kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

# 进行卷积操作
output_image = convolution_2d(input_image, kernel)

# 显示结果图像
cv2.imshow('Output Image', output_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
