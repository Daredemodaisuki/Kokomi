from main import Kokomi
from main import OceanHuedClam
from main import Jellyfish
limit1 = OceanHuedClam("nwr")
limit3 = limit1
limit2 = limit1.key_value("name", "v-reg", "郁").key_value("A", "v-reg", "郁")
if limit1 == limit2:
    print("A")
if limit3 == limit1:
    print("B")
print(limit1.get_full_text())
print(limit3.get_full_text())

limit1 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁")  # 限制语句1：nwr["name"~"郁"]
set1 = Jellyfish("a", limit1)  # 将限制1作为集合a的条件
limit2 = OceanHuedClam("node", 0).import_jellyfish(set1).in_jellyfish("a").key_value("railway", "exist")
# 引用集合set1，并设定为在set1中检索限制语句2：nwr["railway"]
set2 = Jellyfish("b", limit2)
limit3 = OceanHuedClam("nwr").import_jellyfish(set2).in_jellyfish("b").key_value("public_transport", "exist")\
    .key_value("train", "=", "yes").timeout("100")
query_text = limit3.get_full_text()  # 得到最终语句

print("最终语句为" + limit3.get_full_text())
'''
print(limit1.get_this_text())
print(set1.get_this_text())
print(limit2.get_this_text())
print(limit2.get_semi_full_text())
print(limit2.get_full_text())
print(limit3.get_semi_full_text())
print(limit3.jellyfish_dict["b"].OceanHuedClam.jellyfish_dict)
'''


waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(query_text)

print(waifu.directive_text_temp)
'''
limit1 = OceanHuedClam("nwr").key_value("name:en", "v-Aa_no_care", "Shimo-Kitazawa").timeout("25")
waifu.Watatsumi_set("OSMde")
waifu.query(limit1.get_full_text())
print(waifu.directive_text_temp)
'''
limit1 = OceanHuedClam("nwr").id("114514").timeout("25")
waifu.query(limit1.get_full_text())
print(waifu.directive_text_temp)


'''
# 测试：说明无法产生集合的子集，Overpass应该也没有这个做法
limit1 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁州")  # 限制语句1：nwr["name"~"郁州"]
set1 = Jellyfish("a", limit1)  # 将限制1作为集合a的条件
print(limit1.jellyfish_dict)
limit3 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁州")  # 限制语句1：nwr["name"~"郁州"]
set2 = Jellyfish("b", limit3.subset("a", set1))
print(limit3.jellyfish_dict)
print(set2.get_this_text())
limit2 = OceanHuedClam("nwr").timeout("100").subset("b", set2).key_value("railway", "exist")
print(limit2.jellyfish_dict)
print(limit2.get_full_text("b"))

输出：
D:\Environment\Scripts\python.exe D:\地图和其它\kokomi\main.py 
{}
{'a': <__main__.Jellyfish object at 0x0000022A6C8B11D0>}
(nwr["name"~"郁州"];)->.b;
{'b': <__main__.Jellyfish object at 0x0000022A6A57E690>}
data=[out:xml][timeout:100];(nwr["name"~"郁州"];)->.b;nwr.b["railway"];out body;

Process finished with exit code 0
'''