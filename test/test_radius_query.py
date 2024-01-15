import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import Kokomi, OceanHuedClam

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

waifu.query(Q3)
print(waifu.directive_text_temp)

'''
【成功】
测试输出（数据截至2024-01-14）
————————————————————————————————————————
INFO: Kokomi is ready.
Kokomi就绪。

INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.
信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：
 OGF https://overpass.ogf.rent-a-planet.com/api/ 

INFO: OceanHuedClam SJZ is included.
信息：「海染砗磲」“SJZ”已装备。

INFO: OceanHuedClam SJZstop is included.
信息：「海染砗磲」“SJZstop”已装备。

INFO: OceanHuedClam RMGC is included.
信息：「海染砗磲」“RMGC”已装备。

INFO: OceanHuedClam RMGCstop is included.
信息：「海染砗磲」“RMGCstop”已装备。

WARN: When there is id limitation in a OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

WARN: When there is id limitation in a OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

INFO: OceanHuedClam default uses data from a intersection of multiple OceanHuedClams.
信息：所装备的「海染砗磲」“全集”使用了多个其他「海染砗磲」的交集。

INFO: Kokomi is finding in Sangonomiya(Overpass) ( 1 / 1 ):
信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 1 次/共 1 次）：
https://overpass.ogf.rent-a-planet.com/api/interpreter?data=[out:xml][timeout:500];node(id:301074167)->.SJZ;node(around.SJZ:1000)["highway"="bus_stop"]->.SJZstop;way(id:28800254)->.RMGC;node(around.RMGC:1000)["highway"="bus_stop"]->.RMGCstop;node.SJZstop.RMGCstop;out body; 

INFO: 1 node (s) have been found.
信息：Kokomi找到了 1 个 node 。

INFO: 0 way (s) have been found.
信息：Kokomi找到了 0 个 way 。

INFO: 0 relation (s) have been found.
信息：Kokomi找到了 0 个 relation 。

<?xml version="1.0" encoding="UTF-8"?>
<osm version="0.6" generator="Overpass API 0.7.58.2 2b5354b1">
<note>The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.</note>
<meta osm_base="2024-01-14T11:51:51Z"/>

  <node id="335187564" lat="12.4847682" lon="148.4085599">
    <tag k="bus" v="yes"/>
    <tag k="highway" v="bus_stop"/>
    <tag k="name" v="民安坊公园"/>
    <tag k="public_transport" v="platform"/>
  </node>

</osm>
'''

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
    .set_from("SJZstop").set_from("RMGCstop").key_value("name", "exist")

waifu1 = Kokomi()
waifu1.Watatsumi_set("OGF")
waifu1.query(Q3)
print(len(waifu1.directive_dict["node"]))  # -> 30 + 31 - 1交集 = 60成功
# print(waifu1.directive_text_temp)
# TODO:Kokomi中query之后的合并 -> 原来已经合并了啊

'''
【成功】
测试输出（数据截至2024-01-14）
————————————————————————————————————————
INFO: Kokomi is ready.
Kokomi就绪。

INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.
信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：
 OGF https://overpass.ogf.rent-a-planet.com/api/ 

INFO: OceanHuedClam SJZ is included.
信息：「海染砗磲」“SJZ”已装备。

INFO: OceanHuedClam SJZstop is included.
信息：「海染砗磲」“SJZstop”已装备。

INFO: OceanHuedClam RMGC is included.
信息：「海染砗磲」“RMGC”已装备。

INFO: OceanHuedClam RMGCstop is included.
信息：「海染砗磲」“RMGCstop”已装备。

INFO: Kokomi is ready.
Kokomi就绪。

INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.
信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：
 OGF https://overpass.ogf.rent-a-planet.com/api/ 

WARN: When there is id limitation in a OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

WARN: When there is id limitation in a OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

INFO: Kokomi is finding in Sangonomiya(Overpass) ( 1 / 2 ):
信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 1 次/共 2 次）：
https://overpass.ogf.rent-a-planet.com/api/interpreter?data=[out:xml][timeout:500];node(id:301074167)->.SJZ;node(around.SJZ:1000)["highway"="bus_stop"]->.SJZstop;way(id:28800254)->.RMGC;node(around.RMGC:1000)["highway"="bus_stop"]->.RMGCstop;node.SJZstop["name"];out body; 

INFO: 30 node (s) have been found.
信息：Kokomi找到了 30 个 node 。

INFO: 0 way (s) have been found.
信息：Kokomi找到了 0 个 way 。

INFO: 0 relation (s) have been found.
信息：Kokomi找到了 0 个 relation 。

INFO: Kokomi is finding in Sangonomiya(Overpass) ( 2 / 2 ):
信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 2 次/共 2 次）：
https://overpass.ogf.rent-a-planet.com/api/interpreter?data=[out:xml][timeout:500];node(id:301074167)->.SJZ;node(around.SJZ:1000)["highway"="bus_stop"]->.SJZstop;way(id:28800254)->.RMGC;node(around.RMGC:1000)["highway"="bus_stop"]->.RMGCstop;node.RMGCstop["name"];out body; 

INFO: 31 node (s) have been found.
信息：Kokomi找到了 31 个 node 。

INFO: 0 way (s) have been found.
信息：Kokomi找到了 0 个 way 。

INFO: 0 relation (s) have been found.
信息：Kokomi找到了 0 个 relation 。

60
'''