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
    for each in d.entries:
        soup = BeautifulSoup(each.description)
        each_res = soup \
            .get_text('\n') \
            .replace("\n\n", "\n") \
            .replace("\n ", " ") \
            .replace(" \n#", " #") \
            .partition("via")[0]
        result_list.append(each_res)
    if len(result_list)==0:
        result = "暂无找到相关资源，请确认关键词正确！"
    else:
        index_text = "共找到{}条资源\n\n".format(len(result_list))
        result = index_text + "\n========\n\n".join(result_list)
    return result


def ypp_cvt(text: str):
    if text[0] == "#":
        text.replace("#", "%23", 0)
    return text


def test():
    print(yun_pan_pan("keep"))


if __name__ == "__main__":
    test()
