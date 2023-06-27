from main import Kokomi
from main import OceanHuedClam
from main import Jellyfish

limit1 = OceanHuedClam("nwr", 0).key_value("name", "v-reg", "郁州")  # 限制语句1：nwr["name"~"郁州"]
set1 = Jellyfish("a", limit1)  # 将限制1作为集合a的条件
limit2 = OceanHuedClam("nwr").timeout("100").subset("a", set1).key_value("railway", "exist")
# 限制语句2：nwr["railway"]，且设置a为这句话会使用的集合
query_text = limit2.get_full_text("a")  # 设定最终输出集a（nwr["railway"]变为nwr.a["railway"]），并得到最终语句
waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(query_text)

print(limit1.get_this_text())
print(set1.get_this_text())
print(limit2.get_this_text())
print(limit2.get_semi_full_text())
print(limit2.get_full_text("a"))
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