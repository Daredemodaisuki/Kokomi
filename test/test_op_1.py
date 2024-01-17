from main import *

Q1 = OceanHuedClam("node")\
    .key_value("name", "=", "冚家便利")\
    .set_bbox(157.41, 11.58, 157.33, 11.67)  # located_in([12.42, 148.28, 12.58, 148.25, 12.6, 148.49, 12.39, 148.52])
Q2 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1)\
    .around("Q1", 300)\
    .key_value("name", "exist")
Q3 = OceanHuedClam("nwr").include_OceanHuedClam("Q2", Q2).set_from("Q2")\
    .extend("<")

print(Q1.convert())
print(Q2.convert())
print(Q3.convert())

waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query(Q2)

for way_id in waifu.directive_dict["way"]:
    print(way_id, waifu.directive_dict["way"][way_id]["tag_dict"]["name"])

'''
【成功】
----------
INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

INFO: OceanHuedClam  Q2  is included.
信息：「海染砗磲」“Q2”已装备。

['node["name"="冚家便利"](bbox:11.58,157.33,11.67,157.41);']
['node["name"="冚家便利"](bbox:11.58,157.33,11.67,157.41)->.Q1;nwr(around.Q1:300)["name"];']
['node["name"="冚家便利"](bbox:11.58,157.33,11.67,157.41)->.Q1;nwr(around.Q1:300)["name"]->.Q2;nwr.Q2->.TempInner2415;.TempInner2415<']
INFO: Kokomi is ready.
Kokomi就绪。

INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.
信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：
  OGF https://overpass.ogf.rent-a-planet.com/api/

INFO: Kokomi is finding in Sangonomiya(Overpass) ( 1 / 1 ):
信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 1 次/共 1 次）：
https://overpass.ogf.rent-a-planet.com/api/interpreter?data=[out:xml][timeout:500];node["name"="冚家便利"](bbox:11.58,157.33,11.67,157.41)->.Q1;nwr(around.Q1:300)["name"];out body; 

INFO: 6 node(s) have been found.
信息：Kokomi找到了 6 个 node。

INFO: 67 way(s) have been found.
信息：Kokomi找到了 67 个 way。

INFO: 4 relation(s) have been found.
信息：Kokomi找到了 4 个 relation。

25098848 海祇街
25098851 礼嘉大道
25104184 央湖大学（珊瑚宫中心校区）
25104187 礼嘉大道
25104188 礼嘉大道
25104190 水月北街
25104191 水月西街
25104193 水月公园
25104197 水月西街
25104201 水月花园
25109681 礼嘉大道
25109735 使者大道
25109748 键纹街
25109749 御灵路
25109753 月浴街
25109755 坊渡街
25109756 恩典一支路
25109757 绘真横巷
25109758 渊下二巷
25109759 灵庙街
25109760 大日巷
25109761 渊下街
25109762 绘真巷
25109763 常夜巷
25109764 大日巷
25109765 狭间街
25109766 恩典二支路
25109768 常夜灵庙
25109769 常夜殿
25109771 御舆巷
25110195 鸣神商业街
25110224 央湖巿公安局珊瑚宫分局剑鱼一大队
25110228 恩典三支路
25110230 尚恩典
25118281 使者大道
25118301 恩典路
25118302 键纹街
25118303 键纹街
25118308 恩典路
25140612 御灵西路
25140613 恩典三支路
25140615 桃山路
25140621 城轨路
25147134 御灵西路
25147143 撒库拉公园
25147144 八重江山-A区
25147145 八重江山-B区
25147146 恩典典中典-B区
25147171 恩典典中典-A区
25147175 天领小区
25170670 社奉新居
25170671 勘定家园
25192951 八重堂珊瑚分公司
25410408 狭间街
25411619 央湖医科大学附属医院
25426210 月浴街一里
25426239 渊下自产自销市场
25430478 央湖大学（鸣神校区）
25430479 大日巷
25701813 自强体育场
25701866 梅一舍
25701867 梅二舍
32277966 规划地铁(世界树线)
32461375 规划地铁(珊瑚宫线)
32521308 地下商业街
32521379 站前路
32521380 车站路
'''