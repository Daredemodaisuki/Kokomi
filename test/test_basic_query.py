import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import *

# 基本测试：是否跑得通，带多层集合的情况下
Q1 = OceanHuedClam("nwr")\
    .key_value("name", "v-reg", "郁")  # 限制语句1：nwr["name"~"郁"]
Q2 = OceanHuedClam("node").include_OceanHuedClam("a", Q1).set_from("a")\
    .key_value("railway", "exist")  # ↑将限制1作为集合a的条件：引用集合set1，并设定为在set1中检索限制语句2：nwr["railway"]
Q3 = OceanHuedClam("node").include_OceanHuedClam("b", Q2).set_from("b")\
    .key_value("public_transport", "exist").key_value("train", "=", "yes")  # 同理再次套用，得到最终语句

for x in Q3.convert():
    print("最终语句为" + x)

waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(Q3)

'''
【成功】
测试输出（数据截至2024-01-14）
————————————————————————————————————————
INFO: OceanHuedClam a is included.
信息：「海染砗磲」“a”已装备。

INFO: OceanHuedClam b is included.
信息：「海染砗磲」“b”已装备。

最终语句为nwr["name"~"郁"]->.a;node.a["railway"]->.b;node.b["public_transport"]["train"="yes"];
INFO: Kokomi is ready.
Kokomi就绪。

INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.
信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：
 OGF https://overpass.ogf.rent-a-planet.com/api/ 

INFO: Kokomi is finding in Sangonomiya(Overpass) ( 1 / 1 ):
信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 1 次/共 1 次）：
https://overpass.ogf.rent-a-planet.com/api/interpreter?data=[out:xml][timeout:500];nwr["name"~"郁"]->.a;node.a["railway"]->.b;node.b["public_transport"]["train"="yes"];out body; 

INFO: 3 node (s) have been found.
信息：Kokomi找到了 3 个 node 。

INFO: 0 way (s) have been found.
信息：Kokomi找到了 0 个 way 。

INFO: 0 relation (s) have been found.
信息：Kokomi找到了 0 个 relation 。
'''

'''
老版本文段存档（没有联网查询）
————————————————————————————————————————
limit1 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁")  # 限制语句1：nwr["name"~"郁"]
set1 = Jellyfish("a", limit1)  # 将限制1作为集合a的条件
limit2 = OceanHuedClam("node", 0).import_jellyfish(set1).in_jellyfish("a").key_value("railway", "exist")
# 引用集合set1，并设定为在set1中检索限制语句2：nwr["railway"]
set2 = Jellyfish("b", limit2)
limit3 = OceanHuedClam("nwr").import_jellyfish(set2).in_jellyfish("b").key_value("public_transport", "exist")\
    .key_value("train", "=", "yes").timeout("100")

print("最终语句为" + limit3.get_full_text())  # 得到最终语句
'''


