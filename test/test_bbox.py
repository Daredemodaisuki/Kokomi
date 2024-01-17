import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import *

# 测试bbox

Q1 = OceanHuedClam("node").set_bbox(157.41, 11.58, 157.33, 11.67).extend("<", "_").key_value("name", "exist")

waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(Q1)
# waifu.query("node(bbox:50.6,7.0,50.66,7.1)->.TempInner1448;.TempInner1448<->.TempInter7946;node.TempInter7946[\"name\"];out body; ")

print(waifu.directive_text_temp)

for node in waifu.directive_dict["node"]:
    print(node, waifu.directive_dict.get["node"][node]["tag_dict"])
