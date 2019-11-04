import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os, glob, time

orb = cv2.ORB_create()


def read_img(name1, name2):
    img1 = cv2.imread(name1, 1)
    img2 = cv2.imread(name2)
    h, w = min(img1.shape[0], img2.shape[0]), min(img1.shape[1], img2.shape[1])
    img1 = img1[:h, :w]
    img2 = img2[:h, :w]
    img1 = cv2.resize(img1, (800, 800 * img1.shape[0] // img1.shape[1]))
    img2 = cv2.resize(img2, (800, 800 * img2.shape[0] // img2.shape[1]))
    return img1, img2


def color_enhance(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    mask_green = cv2.inRange(hsv, lowerb=lower_green, upperb=upper_green)
    lower_white = np.array([0, 0, 245])
    upper_white = np.array([180, 30, 255])
    mask_white = cv2.inRange(hsv, lowerb=lower_white, upperb=upper_white)

    dst_w = cv2.bitwise_and(img, img, mask=mask_white)
    dst_g = cv2.bitwise_and(img, img, mask=mask_green)
    dst = dst_w + dst_g
    return dst


def count_box(img, show=False):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    H, W = img.shape[:2]
    count = 0
    for contour in contours:
        if cv2.contourArea(contour) < H * W / 500 or H > W * 1.1:
            continue
        count += 1
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if show:
        cv2.imshow('img', img)
        cv2.imshow('gray', gray)
        cv2.imshow('thresh', thresh)
        cv2.waitKey(0)
    return count


def orb_match(img1, img2):
    kp1, des1 = orb.detectAndCompute(img1, None)  # des是描述子
    kp2, des2 = orb.detectAndCompute(img2, None)
    return kp1, des1, kp2, des2


def draw_keypoints(img, keypoints, color=(0, 255, 255)):
    for kp in keypoints:
        x, y = kp.pt
        cv2.circle(img, (int(x), int(y)), 2, color)
    return img


def match_imgs(des1, des2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.8 * n.distance:
            good.append([m])
    return good


def compute_slope(src, dst):
    # slope = (y - y') / (x' - x + 800)
    return (src[1] - dst[1]) / (dst[0] - src[0] + 800)


def judge(img1, img2, show=False):
    img3, img4 = color_enhance(img1), color_enhance(img2)
    n1 = count_box(img3)
    n2 = count_box(img4)
    if n1 != n2:
        print('n1, n2: ', n1, n2)
        return False
    kp1, des1, kp2, des2 = orb_match(img3, img4)
    good = match_imgs(des1, des2)
    src_pts = np.float32([kp1[m[0].queryIdx].pt for m in good]).reshape(-1, 2)
    dst_pts = np.float32([kp2[m[0].trainIdx].pt for m in good]).reshape(-1, 2)
    all_slopes = []
    for i in range(len(src_pts)):
        all_slopes.append(compute_slope(src_pts[i], dst_pts[i]))
    all_slopes.sort()
    len_s = len(all_slopes) // 5
    filtered_slopes = all_slopes[len_s:-len_s]
    slopes = filtered_slopes if filtered_slopes else all_slopes

    if show:
        slopes = pd.Series(slopes)
        # print(slopes.describe())
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.hist(slopes, bins=20, color='blue', alpha=0.8)
        plt.show()

        img5 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        thresh_merge = np.hstack((img3, img4))
        cv2.imshow("thresh_merge", thresh_merge)

        visual_1 = draw_keypoints(img1, kp1, color=(255, 0, 255))
        visual_2 = draw_keypoints(img2, kp2, color=(255, 0, 255))
        hmerge = np.hstack((visual_1, visual_2))
        cv2.imshow("point", hmerge)
        cv2.imshow("ORB", img5)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    slopes_mean = sum(slopes) / len(slopes)
    print('abs slope mean: ', abs(slopes_mean))
    if abs(slopes_mean) < 0.01:
        return True
    else:
        return False


if __name__ == '__main__':
    name1, name2 = './xingyun/src.jpg', './xingyun/cha.jpg'
    img1, img2 = read_img(name1, name2)
    if judge(img1, img2, show=True):
        print('Same screenshots.')
    else:
        print('Different screenshots.')