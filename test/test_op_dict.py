from main import OceanHuedClam

# 测试1：是否能正确存储、分割标识符序列（不代表有意义的数据）
Q1 = OceanHuedClam("nwr").set_bbox(1, 2, 3, 4)
Q2 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1).key_value("railway", "exist").extend("<")\
    .key_value("name:zh", "exist").extend("<")\
    .key_value("name:en", "exist").id(114514)\
    .key_value("name", "exist").key_value("name", "!exist")
Q1.convert_new()
Q2.convert_new()

'''
【成功】
----------
INFO: OceanHuedClam  Q1  is included.
信息：「海染砗磲」“Q1”已装备。

WARN: When there is id limitation in an OceanHuedClam, other limitations cannot function.
警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。

TPE ['nwr']
BOX [[2, 3, 4, 1]]
['start', [{'TPE': ['nwr']}]]
['normal', [{'BOX': [[2, 3, 4, 1]]}]]
WARN: Bbox in set Q1 is disabled due to it is not the main set in this query.
警示意义的：因为「海染砗磲」“Q1”不是最外层语句，其界定框限制不生效。

TPE ['nwr']
ICL ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000024E3C980490>]
K_V ['railway', 'exist', '']
RCS ['_', '<']
K_V ['name:zh', 'exist', '']
RCS ['_', '<']
K_V ['name:en', 'exist', '']
IDe [114514]
K_V ['name', 'exist', '']
K_V ['name', '!exist', '']
['start', [{'TPE': ['nwr']}]]
['normal', [{'ICL': ['Q1', <OceanHuedClam.OceanHuedClam object at 0x0000024E3C980490>]}, {'K_V': ['railway', 'exist', '']}]]
['movable', [{'RCS': ['_', '<']}]]
['normal', [{'K_V': ['name:zh', 'exist', '']}]]
['movable', [{'RCS': ['_', '<']}]]
['normal', [{'K_V': ['name:en', 'exist', '']}]]
['end', [{'IDe': [114514]}]]
['normal', [{'K_V': ['name', 'exist', '']}, {'K_V': ['name', '!exist', '']}]]
'''