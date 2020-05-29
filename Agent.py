import random
import time
import pyautogui
import logging
class Agent:
    def __init__(self):
        self.name="艾达"
        self.knowledge=[]
        logging.basicConfig(filename="log.txt",filemode="w", level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
    def set_knowledge(self,knowledge):
        """
        设置知识库
        :param knowledge:
        :return:
        """
        self.knowledge=knowledge
    def wait(self,sleep_sec=-1):
        """
        停止时间
        :return:
        """
        if sleep_sec==-1:
            sleep_sec=random.randint(1,3)
        time.sleep(sleep_sec)
    def find_location(self,location_name):
        """
        找到特定位置
        :param location_name:
        :return:
        """
        for point in self.knowledge:
            if point.name==location_name:
                return point.location
        return (0,0)
    def find_color(self,goal_name):
        """
        找到特定位置的颜色
        :param goal_name:
        :return:
        """
        for point in self.knowledge:
            if point.name==goal_name:
                return point.color
        return (0,0,0)
    def click_icon(self,icon_name,wait=0):
        """
        点击按钮
        :param icon_name:
        :param wait:
        :return:
        """
        (x, y) = self.find_location(icon_name)
        self.logger.info("点击了按钮"+str(icon_name)+":"+str(x)+","+str(y))
        pyautogui.click(x, y)
        time.sleep(wait)
    def scroll_mouse(self,step=10):
        """
        滑动鼠标滚轮
        :param step: 大于0会显示更多的上部分的屏幕
        :return:
        """
        pyautogui.scroll(step)
    def watch_screen(self,icon_name):
        """
        观察屏幕的点是否符合目标值
        :param icon_name:
        :return:
        """
        img = pyautogui.screenshot()
        location=self.find_location(icon_name)
        color = img.getpixel(location)
        goal_color=self.find_color(icon_name)
        if color==goal_color:
            return True
        else:
            return False
    def initial_wait(self,sleep_sec=15):
        """
        初始化等待
        :param sleep_sec:
        :return:
        """
        print("智能机器人"+self.name+"开始启动...")
        time.sleep(sleep_sec)
        print("一切准备就绪，开始执行任务。")