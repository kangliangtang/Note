import cv2
from skimage.measure import compare_ssim


def imageCompare(src_path, modfiy_path, result_path):
    """
    :param src_path:     原图片 路径
    :param modfiy_path:  修改过的图片路径
    :param result_path:  对比结果图 需要保存的路径
    :return:
    """
    image1 = cv2.imread(src_path)
    image2 = cv2.imread(modfiy_path)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 两张图片的尺寸必须一致
    (score, diff) = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype('uint8')
    print('ssim:{}'.format(score))

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        (x, y, w, h) = cv2.boundingRect(cn)
        cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Result', image2)               # 展示对比标识图
    cv2.imwrite(result_path, image2)           # 对比标识图
    cv2.waitKey(0)


if __name__ == '__main__':
    src_path = '../xingyun/3.jpg'
    modfiy_path = '../xingyun/4.jpg'
    result_path = '../xingyun/3-4.jpg'
    # imageCompare(src_path, modfiy_path, result_path)

    image_path1 = '../xingyun/3-b.jpg'
    img1 = cv2.imread(src_path)
    rows1, cols1 = img1.shape[:2]

    image_path2 = '../xingyun/4-b.jpg'
    img2 = cv2.imread(modfiy_path)
    rows2, cols2 = img2.shape[:2]
    if (rows1 * cols1) > (rows2 * cols2):
        img1 = cv2.resize(img1, (rows2, cols2), )  # 为图片重新指定尺寸
        cv2.imwrite(image_path1, img1)
    elif (rows1 * cols1) < (rows2 * cols2):
        img2 = cv2.resize(img2, (rows1, cols1), )  # 为图片重新指定尺寸
        cv2.imwrite(image_path2, img2)
    else:
        pass











