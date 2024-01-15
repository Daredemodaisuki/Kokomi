import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import *

# 测试bbox

Q1 = OceanHuedClam("node").set_bbox(7.3, 50.6, 7.0, 50.8).extend("<", "_").key_value("name", "exist")

waifu = Kokomi()
waifu.Watatsumi_set("OSMde")
waifu.query(Q1)

for node in waifu.directive_dict["node"]:
    print(node, waifu.directive_dict.get["node"][node]["tag_dict"])
