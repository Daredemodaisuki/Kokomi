from main import Kokomi
from main import OceanHuedClam

# 检索同时在上京站和人民广场周围1000m内的公交站
Q0 = OceanHuedClam("node")\
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

waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(Q0)
print(waifu.directive_text_temp)

# 检索在上京站或人民广场周围1000m内的公交站
Q1 = OceanHuedClam("node")\
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
    .set_from("SJZstop").set_from("RMGCstop").key_value("name", "exist")

waifu1 = Kokomi()
waifu1.Watatsumi_set("OGF")
waifu1.query(Q1)
print(len(waifu1.directive_dict["node"]))  # -> 30 + 31 - 1交集 = 60成功
# print(waifu1.directive_text_temp)
# TODO:Kokomi中query之后的合并 -> 原来已经合并了啊
