"""
存储所需要用到的函数
"""
import feedparser
from bs4 import BeautifulSoup


def yun_pan_pan(text: str):
    # YunPanPan搜索转换
    base_url = "https://rsshub.uneasy.win/telegram/channel/shareAliyun/searchQuery="
    url = base_url + ypp_cvt(text)
    d = feedparser.parse(url)
    result_list = []
    for each in d.entries:
        soup = BeautifulSoup(each.description, features="html.parser")
        each_res = soup \
            .get_text('\n') \
            .replace("\n\n", "\n") \
            .replace("\n ", " ") \
            .replace(" \n#", " #") \
            .replace("=", "") \
            .partition("🏷")[0] \
            .partition("频道投稿")[0]
        result_list.append(each_res)

    if len(result_list) == 0:
        result = "暂无找到相关资源，请确认关键词正确！"
    else:
        text_length = 0
        last_index = 0
        limit_count = 900
        for each_res in result_list:
            if text_length + len(each_res) < limit_count:
                last_index += 1
                text_length += len(each_res)
            else:
                break
        if last_index == 0:
            result = result_list[0][0:limit_count-3] + "..."
        else:
            index_text = "共找到{}条资源，因消息字数限制，仅显示优先级较高的{}条\n\n".format(len(d.entries), last_index)
            result = index_text + "\n\n".join(result_list[0:last_index])
    return result


def ypp_cvt(text: str):
    if text[0] == "#":
        text.replace("#", "%23", 0)
    return text


def test():
    # print(yun_pan_pan("学而思"))
    # print(yun_pan_pan("老友记"))
    # print(yun_pan_pan("合集"))
    print(yun_pan_pan("极度深寒"))


if __name__ == "__main__":
    test()
