import werobot
from utils import *

robot = werobot.WeRoBot(token='tokenhere')


@robot.text
def hello(message):
    return yun_pan_pan(message.content)


@robot.subscribe
def subscribe():
    return "感谢您的关注，发送关键词即可获取资源链接！"


# 让服务器监听在 0.0.0.0:8080
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8080
robot.run()
