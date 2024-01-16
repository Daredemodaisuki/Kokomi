from main import OceanHuedClam

# 测试1：是否能正确存储、分割标识符序列（不代表有意义的数据）
Q1 = OceanHuedClam("nwr").set_bbox(1, 2, 3, 4)
Q2 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1).key_value("railway", "exist")\
    .key_value("name:zh", "exist").extend(">")\
    .key_value("name:en", "exist").id(114514).extend(">>")\
    .key_value("name", "exist").key_value("name", "!exist").extend("<")
Q1.convert_new()
Q2.convert_new()

'''
【成功】
----------
INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

WARN: When there is id limitation in an OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

['start', [{'TPE': ['nwr']}]]
['normal', [{'BOX': [[2, 3, 4, 1]]}]]
[['normal', [{'TPE': ['nwr']}, {'BOX': [[2, 3, 4, 1]]}]]]
WARN: Bbox in set Q1 is disabled due to it is not the main set in this query.
警示意义的：因为「海染砗磲」“Q1”不是最外层语句，其界定框限制不生效。

['start', [{'TPE': ['nwr']}]]
['normal', [{'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x000002B2E2F006D0>]}, {'K_V': ['railway', 'exist', '']}, {'K_V': ['name:zh', 'exist', '']}]]
['movable', [{'RCS': ['_', '>']}]]
['normal', [{'K_V': ['name:en', 'exist', '']}]]
['unique', [{'IDe': [114514]}]]
['movable', [{'RCS': ['_', '>>']}]]
['normal', [{'K_V': ['name', 'exist', '']}, {'K_V': ['name', '!exist', '']}]]
['movable', [{'RCS': ['_', '<']}]]
[['normal', [{'TPE': ['nwr']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x000002B2E5519050>]}, {'K_V': ['railway', 'exist', '']}, {'K_V': ['name:zh', 'exist', '']}]], ['movable', [{'RCS': ['_', '>']}]]]
[['normal', [{'K_V': ['name:en', 'exist', '']}]]]
[['unique', [{'IDe': [114514]}]], ['movable', [{'RCS': ['_', '>>']}]]]
[['normal', [{'K_V': ['name', 'exist', '']}, {'K_V': ['name', '!exist', '']}]], ['movable', [{'RCS': ['_', '<']}]]]
'''

# 测试2：输出kv
print("=====================")
Q1 = OceanHuedClam("nwr").key_value("name:zh", "=", "北京市").key_value("highway", "!exist").key_value("name:en", "exist")\
    .convert_new()

'''
【成功】
----------
['start', [{'TPE': ['nwr']}]]
['normal', [{'K_V': ['name:zh', '=', '北京市']}, {'K_V': ['highway', '!exist', '']}, {'K_V': ['name:en', 'exist', '']}]]
[['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', '=', '北京市']}, {'K_V': ['highway', '!exist', '']}, {'K_V': ['name:en', 'exist', '']}]]]
{'name:zh': {'value': '北京市', 'relation': '='}, 'highway': {'value': '', 'relation': '!exist'}, 'name:en': {'value': '', 'relation': 'exist'}}
op-group: [['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', '=', '北京市']}, {'K_V': ['highway', '!exist', '']}, {'K_V': ['name:en', 'exist', '']}]]] 
>>> nwr["name:zh"="北京市"][!"highway"]["name:en"]
'''

# 测试3：from、around
print("=====================")
Q1 = OceanHuedClam("nwr").key_value("name:zh", "v-reg", "北京市").key_value("name:en", "exist").located_in([1,1,4,5,1,4])
# Q1.convert_new()
Q2 = OceanHuedClam("nwr").key_value("highway", "!exist").include_OceanHuedClam("Q1", Q1).set_from("Q1")
# Q2.convert_new()
Q3 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1).include_OceanHuedClam("Q2", Q2).set_from("Q1").set_from("Q2")
print("※ Q3 >>>", Q3.convert_new())
Q4 = OceanHuedClam("nwr").include_OceanHuedClam("Q3", Q3).around("Q3", 100)
print("※ Q4 >>>", Q4.convert_new())

'''
【成功】
----------
INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

INFO: OceanHuedClam  Q2  is included.
信息：「海染砗磲」“Q2”已装备。

['start', [{'TPE': ['nwr']}]]
['normal', [{'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]
[['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]]
{'name:zh': {'value': '北京市', 'relation': 'v-reg'}, 'name:en': {'value': '', 'relation': 'exist'}}
op-group: [['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]] 
>>> nwr(poly:"1 1 4 5 1 4")["name:zh"~"北京市"]["name:en"]->.Q1;
['start', [{'TPE': ['nwr']}]]
['normal', [{'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FDD0>]}, {'SET': ['or', 'Q1']}]]
[['normal', [{'TPE': ['nwr']}, {'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640150>]}, {'SET': ['or', 'Q1']}]]]
{'highway': {'value': '', 'relation': '!exist'}}
op-group: [['normal', [{'TPE': ['nwr']}, {'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640150>]}, {'SET': ['or', 'Q1']}]]] 
>>> nwr.Q1[!"highway"]->.Q2;
['start', [{'TPE': ['nwr']}]]
['normal', [{'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FDD0>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FFD0>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]
[['normal', [{'TPE': ['nwr']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640210>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640250>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]]
op-group: [['normal', [{'TPE': ['nwr']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640210>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640250>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]] 
>>> (nwr.Q1;nwr.Q2;)->.temp2950;nwr.temp2950;
※ Q3 >>> ['nwr(poly:"1 1 4 5 1 4")["name:zh"~"北京市"]["name:en"]->.Q1;nwr.Q1[!"highway"]->.Q2;(nwr.Q1;nwr.Q2;)->.temp2950;nwr.temp2950;']
INFO: OceanHuedClam  Q3  is included.
信息：「海染砗磲」“Q3”已装备。

['start', [{'TPE': ['nwr']}]]
['normal', [{'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]
[['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]]
{'name:zh': {'value': '北京市', 'relation': 'v-reg'}, 'name:en': {'value': '', 'relation': 'exist'}}
op-group: [['normal', [{'TPE': ['nwr']}, {'K_V': ['name:zh', 'v-reg', '北京市']}, {'K_V': ['name:en', 'exist', '']}, {'POL': [[1, 1, 4, 5, 1, 4]]}]]] 
>>> nwr(poly:"1 1 4 5 1 4")["name:zh"~"北京市"]["name:en"]->.Q1;
['start', [{'TPE': ['nwr']}]]
['normal', [{'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FDD0>]}, {'SET': ['or', 'Q1']}]]
[['normal', [{'TPE': ['nwr']}, {'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640610>]}, {'SET': ['or', 'Q1']}]]]
{'highway': {'value': '', 'relation': '!exist'}}
op-group: [['normal', [{'TPE': ['nwr']}, {'K_V': ['highway', '!exist', '']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640610>]}, {'SET': ['or', 'Q1']}]]] 
>>> nwr.Q1[!"highway"]->.Q2;
['start', [{'TPE': ['nwr']}]]
['normal', [{'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FDD0>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D6662FFD0>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]
[['normal', [{'TPE': ['nwr']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D666406D0>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640790>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]]
op-group: [['normal', [{'TPE': ['nwr']}, {'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000028D666406D0>]}, {'ICL': ['Q2', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640790>]}, {'SET': ['or', 'Q1']}, {'SET': ['or', 'Q2']}]]] 
>>> (nwr.Q1;nwr.Q2;)->.temp2950;nwr.temp2950->.Q3;
['start', [{'TPE': ['nwr']}]]
['normal', [{'ICL': ['Q3', <OceanHuedClam.OceanHuedClam object at 0x0000028D66548210>]}, {'ARD': ['set', 'Q3', 100]}]]
[['normal', [{'TPE': ['nwr']}, {'ICL': ['Q3', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640910>]}, {'ARD': ['set', 'Q3', 100]}]]]
op-group: [['normal', [{'TPE': ['nwr']}, {'ICL': ['Q3', <OceanHuedClam.OceanHuedClam object at 0x0000028D66640910>]}, {'ARD': ['set', 'Q3', 100]}]]] 
>>> nwr(around.Q3:100);
※ Q4 >>> ['nwr(poly:"1 1 4 5 1 4")["name:zh"~"北京市"]["name:en"]->.Q1;nwr.Q1[!"highway"]->.Q2;(nwr.Q1;nwr.Q2;)->.temp2950;nwr.temp2950->.Q3;nwr(around.Q3:100);']
'''

# 测试4：extend
print("=====================")
Q1 = OceanHuedClam("nwr").key_value("place", "=", "city").extend("<").located_in([1,1,4,5])
Q2 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1).set_from("Q1").set_bbox(11,45,14,19).extend(">>")
print(Q2.convert_new())
