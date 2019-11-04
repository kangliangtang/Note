import cv2
import numpy
from PIL import Image


def find_coordinate(scr_path, locator_path):
    img = cv2.imread(locator_path)
    height = img.shape[0]
    width = img.shape[1]

    scr = Image.open(scr_path)
    scr = numpy.asarray(scr, dtype=numpy.float32).astype(numpy.uint8)
    # 将图像从BGR为RGB格式;
    scr = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)

    # 模块匹配
    img_match = cv2.minMaxLoc(
        cv2.matchTemplate(cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY),
                          cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                          cv2.TM_CCOEFF_NORMED))

    x = img_match[3][0]
    y = img_match[3][1]

    print('---阀值---', round(img_match[1], 2))
    # 标识
    location_img = cv2.rectangle(scr, (x, y),(x + width, y + height),(0, 0, 255), 2)
    cv2.imwrite('./location.png', location_img)          # 保存
    cv2.imshow('result', cv2.imread('./location.png'))   # 展示
    cv2.waitKey(0)


if __name__ == '__main__':
    scr_path = '../image/121.png'
    locator_path = '../image/122.png'
    find_coordinate(scr_path, locator_path)








