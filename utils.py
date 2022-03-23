"""
存储所需要用到的函数
"""
import feedparser
from bs4 import BeautifulSoup


def yun_pan_pan(text: str):
    # YunPanPan搜索转换
    base_url = "https://rss.ermaotie.workers.dev/telegram/channel/YunPanPan/searchQuery="
    url = base_url + ypp_cvt(text)
    d = feedparser.parse(url)
    result_list = []
    i = 1
    for each in d.entries[0:3]:
        soup = BeautifulSoup(each.description, features="html.parser")
        each_res = soup \
            .get_text('\n') \
            .replace("\n\n", "\n") \
            .replace("\n ", " ") \
            .replace(" \n#", " #") \
            .partition("via")[0] \
            .partition("频道投稿")[0]
        result_list.append(each_res)
        if i < 3:
            i += 1
        else:
            break

    if len(result_list) == 0:
        result = "暂无找到相关资源，请确认关键词正确！"
    else:
        index_text = "共找到{}条资源，因消息限制，仅显示优先级较高的几条\n\n".format(len(d.entries))
        result = index_text + "\n========\n\n".join(result_list)
    return result


def ypp_cvt(text: str):
    if text[0] == "#":
        text.replace("#", "%23", 0)
    return text


def test():
    print(yun_pan_pan("蜘蛛侠"))


if __name__ == "__main__":
    test()
