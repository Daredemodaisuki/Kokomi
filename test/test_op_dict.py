from main import OceanHuedClam

# 测试1：是否能正确存储标识符序列
Q1 = OceanHuedClam("nwr").set_bbox(1, 2, 3, 4)
Q2 = OceanHuedClam("nwr").include_OceanHuedClam("Q1", Q1).key_value("railway", "exist").extend("<")\
    .key_value("name", "exist").extend("<")\
    .key_value("name", "exist").extend("<")\
    .key_value("name", "exist").key_value("name", "!exist")
Q1.convert_new()
Q2.convert_new()
