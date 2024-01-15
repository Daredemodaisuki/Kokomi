import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import *
from xpinyin import Pinyin

# 有哪些外国地名的英文拼写，恰好和它的普通话翻译的汉语拼音拼写一样？
# https://www.zhihu.com/question/627251900/answer/3319217680
# 一种可能实现的示例，考虑到OSM数据质量参差不齐、数据填写情况不一致，可能会混有不正确的数据且会有大量缺漏

waifu = Kokomi()
waifu.Watatsumi_set("OSMde")
waifu.query(OceanHuedClam("node")
            .key_value("place", "exist")
            .key_value("name", "exist")
            .key_value("name:en", "exist")
            .key_value("name:zh", "exist")
            , 5000)


p = Pinyin()

for node in waifu.directive_dict["node"]:
    name = waifu.directive_dict["node"][node]["tag_dict"]["name"]
    en_name = waifu.directive_dict["node"][node]["tag_dict"]["name:en"]
    zh_name = waifu.directive_dict["node"][node]["tag_dict"]["name:zh"]
    if en_name.lower() == p.get_pinyin(zh_name, "") and not (zh_name in name or name in zh_name):
        print(node, "|", name, "|", en_name, "|", zh_name)
