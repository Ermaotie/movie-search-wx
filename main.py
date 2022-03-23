import werobot
from utils import *

robot = werobot.WeRoBot(token='tokenhere')


@robot.text
def hello(message):
    return yun_pan_pan(message.content)


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8080
robot.run()
