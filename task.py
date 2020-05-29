from point import Point
class CustomTask:
    def __init__(self,task_name):
        self.name=task_name
        self.agent=None
        self.knowledge=[]
        self.create_knowledge()
    def create_knowledge(self):
        """
        特定领域知识，存放在这里
        :return:
        """
        knowledge=[]
        point= Point("采集资源",(0,0),(0,0,0))
        knowledge.append(point)
        self.knowledge=knowledge
    def set_agent(self,agent):
        """
        设置代理
        :param agent:
        :return:
        """
        self.agent=agent
        self.agent.knowledge=self.knowledge
    def go_collection(self):
        """
        具体采集
        :return:
        """
        self.agent.click_icon("采集资源",1)
        self.agent.click_icon("最大负重",1)
        self.agent.click_icon("编队3加载",1)
        self.agent.click_icon("选择武将",1)
        self.agent.click_icon("自动派遣",1)
        self.agent.click_icon("派遣完成",1)
        self.agent.click_icon("出征",1)
        self.agent.click_icon("继续出征",1)

    def buy_buttery(self):
        """
        购买电量
        :return:
        """
        self.agent.click_icon("购买电量加号",2)
        self.agent.click_icon("钻石购买电量",2)
        self.agent.click_icon("购买电量返回",1)
    def check_buttery(self):
        """
        检查是否需要购买点亮
        :return:
        """
        if self.agent.watch_screen("电量不足"):
            self.agent.logger.info("需要买电")
            self.buy_buttery()
        else:
            self.agent.logger.info("需要买电")
    def can_go_out(self,collection_team):
        """
        是否可以出征
        :param collection_team:
        :return:
        """
        if self.agent.watch_screen(collection_team):
            return False
        else:
            return True
    def init_agent(self):
        """
        初始化代理
        :return:
        """
        self.agent.initial_wait()

    def run_collection(self,collection_team,wait_sec):
        """
        执行采集
        :param collection_team: 需要采集的队伍数量
        :param wait_sec: 多少时间检查一次
        :return:
        """
        while self.can_go_out(collection_team):
            self.check_buttery()
            self.go_collection()
            self.agent.wait(wait_sec)
