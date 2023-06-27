from main import Kokomi
from main import OceanHuedClam

# test
# 测试区
'''
waifu = Kokomi()
waifu.Watatsumi_set("OGF")
waifu.query("data=[out:xml][timeout:25];relation[\"name\"=\"华夏共和国陆地\"];out body;")
# "data=[out:xml][timeout:25];node[name](id:6229630725);out meta;>;out meta qt;"
# "data=[out:xml][timeout:25];(area[\"ISO3166-1\"=\"GB\"][admin_level=2]; )->.a;"
print("源报文：", waifu.directive_text_temp)
print("============分割线============")
for test_data in waifu.directive_dict["relation"]:
    print("测试数据ID：" + test_data, "\n", waifu.directive_dict["relation"][test_data])
waifu.how_are_you()
waifu.I_come_back()
waifu.how_are_you()
'''


waifu = Kokomi()
waifu.Watatsumi_set("OGF")
limit = OceanHuedClam("nwr").timeout("25").key_value("name", "v-reg", "郁州")
waifu.query(limit.get_this_text())
for test_data in waifu.directive_dict["node"]:
    print("点ID：" + test_data, "：", waifu.directive_dict["node"][test_data])
for test_data in waifu.directive_dict["relation"]:
    print("关系ID：" + test_data, "：", waifu.directive_dict["relation"][test_data])

waifu.directive_dict["node"] = {}
waifu.directive_dict["relation"] = {}

limit = limit.key_value("railway", "exist")
waifu.query(limit.get_this_text())
for test_data in waifu.directive_dict["node"]:
    print("点ID：" + test_data, "：", waifu.directive_dict["node"][test_data])
