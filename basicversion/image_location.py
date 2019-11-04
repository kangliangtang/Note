import cv2
import numpy
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains


class ImageLocator(object):
    """图片定位 返回定位到的图片相对页面截图的坐标(x,y)"""
    def __init__(self, driver, img_path):
        self.locator = img_path
        # x, y position in pixels counting from left, top corner
        self.x = None
        self.y = None
        self.driver = driver
        self.img = None
        self.height = None
        self.width = None
        self.threshold = None

    @property
    def center_x(self):
        return self.x + int(self.width / 2) if self.x and self.width else None

    @property
    def center_y(self):
        return self.y + int(self.height / 2) if self.y and self.height else None

    def find_coordinate(self):
        try:
            self.img = cv2.imread(self.locator)
            self.height = self.img.shape[0]
            self.width = self.img.shape[1]

            # Clear last found coordinates 初始化坐标
            self.x = self.y = None
            # Get current screenshot of a web page  得到当前的网页截图
            scr = self.driver.get_screenshot_as_png()
            # Convert img to BytesIO  img转换为BytesIO
            scr = Image.open(BytesIO(scr))
            # Convert to format accepted by OpenCV  转换为格式接受OpenCV
            scr = numpy.asarray(scr, dtype=numpy.float32).astype(numpy.uint8)
            # Convert image from BGR to RGB format  将图像从BGR为RGB格式;
            scr = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)

            # Image matching works only on gray images  图像匹配只能在灰色图像;
            # (color conversion from RGB/BGR to GRAY scale) (从RGB颜色转换/ BGR灰度)
            img_match = cv2.minMaxLoc(
                cv2.matchTemplate(cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY),
                                  cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY),
                                  cv2.TM_CCOEFF_NORMED))

            # Calculate position of found element  计算发现元素的位置;
            self.x = img_match[3][0]
            self.y = img_match[3][1]

            # From full screenshot crop part that matches template image  完整的截图作物部分相匹配的模板映像
            scr_crop = scr[self.y:(self.y + self.height), self.x:(self.x + self.width)]

            # Calculate colors histogram of both template  计算颜色直方图的模板;
            # and matching images and compare them         和匹配图像和比较
            scr_hist = cv2.calcHist([scr_crop], [0, 1, 2], None,
                                    [8, 8, 8], [0, 256, 0, 256, 0, 256])
            img_hist = cv2.calcHist([self.img], [0, 1, 2], None,
                                    [8, 8, 8], [0, 256, 0, 256, 0, 256])
            comp_hist = cv2.compareHist(img_hist, scr_hist,
                                        cv2.HISTCMP_CORREL)
            # Save threshold matches of: graphical image and image histogram  节省阈值匹配:图形图像和图像直方图
            self.threshold = {'shape': round(img_match[1], 2),
                              'histogram': round(comp_hist, 2)}

            # image with blue rectangle around match   图像周围有蓝色矩形匹配;
            location_img = cv2.rectangle(scr, (self.x, self.y),
                                         (self.x + self.width, self.y + self.height),
                                         (0, 0, 255), 2)
            cv2.imwrite('./location.png', location_img)  # 保存标识出的图片

            # 发现差异标识 -> 获取准确位置（px）
            is_found = True if self.threshold['shape'] >= 0.8 and self.threshold['histogram'] >= 0.4 else False
            if is_found:
                return self.center_x, self.center_y
            else:
                return None, None
        except Exception:
            return None, None


if __name__ == '__main__':
    base_url = "http://api.devopsuat.crc.com.cn/oauth/login"
    # base_url = "http://www.baidu.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    img_paths = ['../image/user.png', '../image/pwd.png', '../image/login.png']
    # img_paths = ['../image/baidu.png']

    for path in img_paths:
        img_check = ImageLocator(driver, path)
        location_x, location_y = img_check.find_coordinate()
        print(location_x)
        print(location_y)
        action = ActionChains(driver)
        action.move_by_offset(location_x, location_y)
        action.click()
        action.send_keys('admin')
        action.perform()
        action.reset_actions()          # 将鼠标移动回原位，防止鼠标移动坐标叠加






