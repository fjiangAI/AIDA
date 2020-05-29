from task import CustomTask
from Agent import Agent
if __name__ == '__main__':
    goal_task=CustomTask("自定义任务")
    aida=Agent()
    goal_task.set_agent(aida)
    goal_task.init_agent()
    # 采集5个队伍，每次采集等待5秒
    goal_task.run_collection(collection_team=5,wait_sec=5)
