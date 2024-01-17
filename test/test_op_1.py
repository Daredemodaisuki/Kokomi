from OceanHuedClam import OceanHuedClam

Q1 = OceanHuedClam("node")\
    .key_value("name", "=", "冚家便利")\
    .located_in([12.42, 148.28, 12.58, 148.25, 12.6, 148.49, 12.39, 148.52])
Q2 = OceanHuedClam("node").include_OceanHuedClam("Q1", Q1)\
    .around("Q1", 300)\
    .key_value("bus", "=", "yes")
Q3 = OceanHuedClam("nwr").include_OceanHuedClam("Q2", Q2).set_from("Q2")\
    .extend("<")

print(Q1.convert_new())
print(Q2.convert_new())
print(Q3.convert_new())

'''
【成功】
----------
INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

INFO: OceanHuedClam  Q2  is included.
信息：「海染砗磲」“Q2”已装备。

['node(poly:"12.42 148.28 12.58 148.25 12.6 148.49 12.39 148.52")["name"="冚家便利"];']
['node(poly:"12.42 148.28 12.58 148.25 12.6 148.49 12.39 148.52")["name"="冚家便利"]->.Q1;node(around.Q1:300)["bus"="yes"];']
['node(poly:"12.42 148.28 12.58 148.25 12.6 148.49 12.39 148.52")["name"="冚家便利"]->.Q1;node(around.Q1:300)["bus"="yes"]->.Q2;nwr.Q2->.Temp_inner9347;.Temp_inner9347<;']
'''