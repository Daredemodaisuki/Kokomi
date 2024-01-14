import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from Kokomi.main import Kokomi, OceanHuedClam

# 检索同时在上京站和人民广场周围1000m内的公交站
waifu = Kokomi()
waifu.Watatsumi_set("OGF")
Q3 = OceanHuedClam("node")\
    .include_OceanHuedClam("SJZstop", OceanHuedClam("node")\
                                     .include_OceanHuedClam("SJZ", OceanHuedClam("node")\
                                                                  .id(301074167))\
                                     .key_value("highway", "=", "bus_stop")
                                     .around("SJZ", 1000))\
    .include_OceanHuedClam("RMGCstop", OceanHuedClam("node")\
                                      .include_OceanHuedClam("RMGC", OceanHuedClam("way")\
                                                                    .id(28800254))\
                                      .key_value("highway", "=", "bus_stop")\
                                      .around("RMGC", 1000))\
    .set_from(["SJZstop", "RMGCstop"])

waifu.query("data=[out:xml][timeout:500];" + Q3.convert() + "out body;")
print(waifu.directive_text_temp)

'''
Q1 = OceanHuedClam("node") \
    .include_OceanHuedClam("SJZ", OceanHuedClam("node").id(301074167)) \
    .key_value("highway", "=", "bus_stop") \
    .around("SJZ", 1000)
Q2 = OceanHuedClam("node") \
    .include_OceanHuedClam("RMGC", OceanHuedClam("way").id(28800254)) \
    .key_value("highway", "=", "bus_stop") \
    .around("RMGC", 1000)
Q3 = OceanHuedClam("node") \
    .include_OceanHuedClam("SJZstop", Q1) \
    .include_OceanHuedClam("RMGCstop", Q2) \
    .set_from(["SJZstop", "RMGCstop"])
waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query("data=[out:xml][timeout:500];" + Q3.convert() + "out body;")
print(waifu.directive_text_temp)
'''
# print(Q3.convert())

# 检验id是否可以同kv一并使用 -> 不可以
'''Q4 = OceanHuedClam("node")\
    .id(301074167)\
    .key_value("highway", "exist")

waifu1 = Kokomi()
waifu1.Watatsumi_set("OGF")
waifu1.query("data=[out:xml][timeout:500];" + Q4.convert() + "out body;")
print(waifu1.directive_text_temp)'''

# 检索在上京站或人民广场周围1000m内的公交站
waifu = Kokomi()
waifu.Watatsumi_set("OGF")

Q3 = OceanHuedClam("node")\
    .include_OceanHuedClam("SJZstop", OceanHuedClam("node")\
                                     .include_OceanHuedClam("SJZ", OceanHuedClam("node")\
                                                                  .id(301074167))\
                                     .key_value("highway", "=", "bus_stop")
                                     .around("SJZ", 1000))\
    .include_OceanHuedClam("RMGCstop", OceanHuedClam("node")\
                                      .include_OceanHuedClam("RMGC", OceanHuedClam("way")\
                                                                    .id(28800254))\
                                      .key_value("highway", "=", "bus_stop")\
                                      .around("RMGC", 1000))\
    .set_from("SJZstop").set_from("RMGCstop").set_from(["SJZstop", "RMGCstop"])

Q_list = Q3.how_many_query()
for x in Q_list:
    # TODO:合并还没做；how_many_query()之后并入query函数
    waifu.query("data=[out:xml][timeout:500];" + x.convert() + "out body;")

    print(waifu.directive_text_temp)
