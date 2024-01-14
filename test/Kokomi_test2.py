import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from Kokomi.main import Kokomi, OceanHuedClam,Jellyfish

from main import Kokomi
from main import OceanHuedClam
from main import Jellyfish

# 测试1：测试方法链
'''
limit1 = OceanHuedClam("nwr")
limit3 = limit1
limit2 = limit1.key_value("name", "v-reg", "foo").key_value("amd", "=", "yes")
if limit1 == limit2:
    print("A")
if limit3 == limit1:
    print("B")
print(limit1.get_full_text())
print(limit2.get_full_text())
print(limit3.get_full_text())
'''
# 测试2
'''
limit1 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁")  # 限制语句1：nwr["name"~"郁"]
set1 = Jellyfish("a", limit1)  # 将限制1作为集合a的条件
limit2 = OceanHuedClam("node", 0).import_jellyfish(set1).in_jellyfish("a").key_value("railway", "exist")
# 引用集合set1，并设定为在set1中检索限制语句2：nwr["railway"]
set2 = Jellyfish("b", limit2)
limit3 = OceanHuedClam("nwr").import_jellyfish(set2).in_jellyfish("b").key_value("public_transport", "exist")\
    .key_value("train", "=", "yes").timeout("100")
query_text = limit3.get_full_text()  # 得到最终语句

print("最终语句为" + limit3.get_full_text())

print(limit1.get_this_text())
print(set1.get_this_text())
print(limit2.get_this_text())
print(limit2.get_semi_full_text())
print(limit2.get_full_text())
print(limit3.get_semi_full_text())
print(limit3.jellyfish_dict["b"].OceanHuedClam.jellyfish_dict)

waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(query_text)

print(waifu.directive_text_temp)
'''
# 测试3
'''
limit1 = OceanHuedClam("nwr").key_value("name:en", "v-Aa_no_care", "Shimo-Kitazawa").timeout("25")
waifu.Watatsumi_set("OSMde")
waifu.query(limit1.get_full_text())
print(waifu.directive_text_temp)

limit1 = OceanHuedClam("nwr").id("114514").timeout("25")
waifu.query(limit1.get_full_text())
print(waifu.directive_text_temp)
'''
# 测试4
waifu = Kokomi()
waifu.Watatsumi_set("OSMde")
limit1 = OceanHuedClam("node").in_bbox("106.614", "106.613", "30.176", "30.177").recurse("", "up")
set1 = Jellyfish("set1", limit1)
limit2 = OceanHuedClam("nwr").import_jellyfish(set1).in_jellyfish("set1").key_value("name", "exist").recurse("_", "up")

print(limit1.get_full_text())
waifu.query(limit1.get_full_text())
# print(waifu.directive_text_temp)

for node in waifu.directive_dict.get("node"):
    print(node, waifu.directive_dict.get("node")[node])

print(limit2.get_full_text())
waifu.query(limit2.get_full_text())
print(waifu.directive_text_temp)
