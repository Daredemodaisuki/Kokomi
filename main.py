import requests


class Kokomi:
    def __init__(self):
        self.energy = 50
        self.check_energy = 1
        self.directive_type = ["node", "way", "relation"]
        self.directive_dict = {"node": {}, "way": {}, "relation": {}}
        self.directive_text_temp = ""
        self.Watatsumi = {"Sangonomiya_name": "", "Sangonomiya_api": ""}
        # Sangonomiya_name = Overpass_name, Sangonomiya_api = Overpass_api
        print("INFO: Kokomi is ready.\nKokomi就绪。\n")

    # 诶，这个是...
    def energy_check(self):
        if self.check_energy == 1 and self.energy <= 30:
            print("NOTICE: Now Kokomi has low energy(", self.energy,
                  ") due to mass ERRORs.\n"
                  "    For not showing this message, please set Kokomi's check_energy as 0.\n"
                  "注意：发生的错误有点多，Kokomi感觉到有点累了。\n"
                  "    退订请设置Kokomi的check_energy为0。\n"
                  )

    # 还——给——我——
    def I_come_back(self):
        self.energy = self.energy + 4
        print("KOKOMI: 今天剑鱼二番队队长回来了，能量值+4。\n")

    # 你都看到了吧
    def how_are_you(self):
        print("KOKOMI: 当前能量值为", self.energy, "。\n")

    # 海祇岛（Network）连接参数设置：指定查询的api参数。
    #   参数1为【预设名称，str】（"OSMde"、"OSMru"、"OGF"、"None"）：使用预设珊瑚宫（Overpass）伺服器配置，或不使用预设（"None"）；
    #   参数2为【自定名称，str】：参数1为"None"时，自定义珊瑚宫伺服器名称，默认为空；
    #   参数3为【自定API地址，str】：参数1为"None"时，自定义珊瑚宫伺服器API地址，填写至"interpreter?..."前，默认为空。
    # 返回int：
    #   【1】：成功使用预设配置；
    #   【0】：成功使用自定义配置；
    #   【-1】：使用了未定义的预设名称；
    #   【-2】：不完整的自定义配置。
    def Watatsumi_set(self, preset: str, name: str = "", api: str = "") -> int:
        self.energy_check()
        Watatsumi_list = {
            "OSMde": {
                "Sangonomiya_name": "OSMde",
                "Sangonomiya_api": "https://overpass-api.de/api/"
            },
            "OSMru": {
                "Sangonomiya_name": "OSMru",
                "Sangonomiya_api": "http://overpass.openstreetmap.ru/cgi/"
            },
            "OGF": {
                "Sangonomiya_name": "OGF",
                "Sangonomiya_api": "https://overpass.ogf.rent-a-planet.com/api/"
            }
        }
        if preset in Watatsumi_list:
            self.Watatsumi["Sangonomiya_name"] = Watatsumi_list.get(preset)["Sangonomiya_name"]
            self.Watatsumi["Sangonomiya_api"] = Watatsumi_list.get(preset)["Sangonomiya_api"]
            print("INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.\n信息：已在海祇岛上建立珊瑚宫。"
                  "（指定Overpass成功）：\n", self.Watatsumi["Sangonomiya_name"], self.Watatsumi["Sangonomiya_api"], "\n")
            self.energy = self.energy + 1
            return 1
        else:
            if preset == "None":
                if name != "" and api != "":
                    self.Watatsumi["Sangonomiya_name"] = name
                    self.Watatsumi["Sangonomiya_api"] = api
                    print(
                        "NOTICE: Self-defined Sangonomiya(Overpass) set.\n注意：你正在使用自定义的珊瑚宫（Overpass）配置:\n",
                        self.Watatsumi["Sangonomiya_name"], self.Watatsumi["Sangonomiya_api"], "\n")
                    self.energy = self.energy + 0
                    return 0
                else:
                    print("ERROR: Uncompleted Sangonomiya(Overpass) set.\n错误的：珊瑚宫（Overpass）配置不完整。\n")
                    self.energy = self.energy - 2
                    return -2
            else:
                print("ERROR: Undefined Sangonomiya(Overpass) preset.\n错误的：没有定义的珊瑚宫（Overpass）预设配置。\n")
                self.energy = self.energy - 1
                return -1

    # 查询要素：本次查询收到的报文将储存在kokomi的临时锦囊（directive_text_temp）中，并调用get_directive_dict处理信息。
    #   参数1为【查询指令，str】：在珊瑚宫（Overpass）查询的参数，以“data="后开始，默认为空，当然返回的报文也会告诉你不给东西查不到。
    # 返回int：
    #   【2】：向珊瑚宫成功地GET了报文；
    #   【-1】：珊瑚宫没有传回任何消息，可能是海祇岛（Network）连接原因；
    #   【-2】：珊瑚宫api未指定。
    def query(self, content: str = "") -> int:
        self.energy_check()
        if self.Watatsumi["Sangonomiya_api"] == "":
            print("ERROR: No Sangonomiya(Overpass) info.\n错误的：珊瑚宫（Overpass）未指定。\n")
            self.energy = self.energy - 2
            return -2
        else:
            text_temp = requests.get(self.Watatsumi["Sangonomiya_api"] + "interpreter?" + content).text
            print("INFO: Kokomi is finding in Sangonomiya(Overpass).\n信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜：\n",
                  self.Watatsumi["Sangonomiya_api"] + "interpreter?" + content, "\n")
            if text_temp == "":
                print("ERROR: No info from Sangonomiya(Overpass).\n错误的：珊瑚宫（Overpass）没有回传任何信息。\n")
                self.energy = self.energy - 1
                return -1
            else:
                self.directive_text_temp = text_temp
                self.directive_dict["node"].update(self.get_directive_dict("node", text_temp))
                self.directive_dict["way"].update(self.get_directive_dict("way", text_temp))
                self.directive_dict["relation"].update(self.get_directive_dict("relation", text_temp))
                self.energy = self.energy + 2
                return 2

    # 锦囊（要素）报文分割：将指定类型每个要素的信息切开，放入dict中。
    #   参数1为【锦囊类型】（"node"、"way"、"relation"）：应当是点、线、关系的一种；
    #   参数2为【欲切割报文】：需要处理的报文，默认为空。
    # 返回dict：
    #   {锦囊ID: {
    #       "type": 锦囊类型,
    #       "tag_dict": {键名: 值, ...},
    #       "member_dict": {成员类型 + ID: 角色, ...},
    #       "node_list": [ID1, ID2, ...]
    #       "text": 报文全文
    #       },
    #   ...
    #   }。
    def get_directive_dict(self, directive_type: str, directive_text: str = ""):
        if directive_type in self.directive_type:
            directive_front = 0
            directive_behind = 0
            directive_found = 0
            directive_list = {}
            while directive_text.find("<" + directive_type, directive_behind) != -1:
                # 找报文开头结尾
                directive_front = directive_text.find("<" + directive_type, directive_behind)
                directive_behind = directive_text.find("</" + directive_type + ">", directive_front)
                dealt_text = directive_text[directive_front: directive_behind]
                directive_found = directive_found + 1

                # 找id
                id_front = dealt_text.find("id=") + 4
                id_behind = dealt_text.find("\"", id_front)
                directive_id = dealt_text[id_front:id_behind]

                # 分割dealt_text
                line_front = 0
                line_behind = 0
                # line_found = 0
                tag_dict = {}
                member_dict = {}
                node_list = []
                while dealt_text.find(">\n", line_behind) != -1:
                    line_front = dealt_text.find(">\n", line_behind)
                    line_behind = dealt_text.find(">\n", line_front + 1)
                    line_text = dealt_text[line_front + 2:line_behind]
                    # print(line_text)
                    # line_found = line_found + 1
                    # 处理tag、member、nd
                    if line_text.find("<tag") != -1:
                        line_key = line_text[
                                   line_text.find("k=\"") + 3:line_text.find("\" ", line_text.find("k=\"") + 3)]
                        line_value = line_text[
                                     line_text.find("v=\"") + 3:line_text.find("\"/", line_text.find("k=\"") + 3)]
                        # print(line_key, line_value)
                        tag_dict.update({line_key: line_value})
                    if line_text.find("<member") != -1:
                        member_type = line_text[line_text.find("type=\"") + 6
                                                :line_text.find("\" ", line_text.find("type=\"") + 6)]
                        member_ref = line_text[line_text.find("ref=\"") + 5
                                               :line_text.find("\" ", line_text.find("ref=\"") + 5)]
                        member_role = line_text[line_text.find("role=\"") + 6
                                                :line_text.find("\"/", line_text.find("role=\"") + 6)]
                        # print(member_type, member_ref, member_role)
                        member_dict.update({member_type + member_ref: member_role})
                    if line_text.find("<nd") != -1:
                        node_ref = line_text[line_text.find("ref=\"") + 5
                                             :line_text.find("\"/", line_text.find("ref=\"") + 5)]
                        # print(node_ref)
                        node_list.append(node_ref)

                # 准备返回的dict的子项
                directive = {"type": directive_type,
                             "tag_dict": tag_dict,
                             "member_dict": member_dict,
                             "node_list": node_list,
                             "text": dealt_text
                             }
                directive_list.update({directive_id: directive})

            # 结束
            print("INFO:", directive_found, directive_type, "(s) have been found.\n信息：Kokomi找到了", directive_found,
                  "个", directive_type, "。\n")
            self.energy = self.energy + 1
            return directive_list
        else:
            print("ERROR: Undefined Directive(Feature) type.\n错误的：没有定义的锦囊（要素）类型。\n")
            self.energy = self.energy - 1
            return {}


# QL条件语句类，一个海染对象即句话
class OceanHuedClam:
    def __init__(self, directive_type: str, if_this_main: int = 1):
        self.if_main = if_this_main
        self.main_type = directive_type  # 查询的 主 体 要素类型
        self.time = "100"
        self.limit_dict = {}  # 限制信息字典
        self.jellyfish_dict = {}  # 要素集字典
        self.output_jellyfish = "_"
        self.text = ""  # 最终的文本

    # 键值关系限制语句：限定查询主体的key与value。
    #   参数1为【限定键】：限定必须出现或有对应值要求的键；
    #   参数2为【限制关系】（"exist"、"!exist"、"="、"!="、"=!="、"v-reg"、"!v-reg"、"kv-reg"、"v-Aa_no_care"）：限定键值之间的关系
    #   参数3为【限定值】：对限定键的值的要求
    # 返回OceanHuedClam：
    #   如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。
    def key_value(self, key: str, relation: str, value: str = "") -> 'OceanHuedClam':
        relation_list = ["exist", "!exist", "=", "!=", "=!=", "v-reg", "!v-reg", "kv-reg", "v-Aa_no_care"]
        # 存在key（value可不填）、不存在key、存在key且对应value匹配、存在key但对应value不匹配或不存在key、必须存在key但对应value不匹配，
        # v可含正则表达式、v可含正则表达式但不匹配、kv皆可含正则表达式，v可含正则表达式且不分大小写
        if relation in relation_list:
            if relation not in ["exist", "!exist"] and value == "":
                print("ERROR: Value needed except exist and !exist.\n错误的：除exist、!exist条件外需要键的值。\n")
                return self
            else:
                self.limit_dict.update({key: {"value": value, "relation": relation}})
                return self
        else:
            print("ERROR: Undefined key-value relation.\n错误的：未定义的键值关系。\n")
            return self

    def subset(self, name: str, subset: 'Jellyfish') -> 'OceanHuedClam':
        self.jellyfish_dict.update({name: subset})
        return self

    def timeout(self, time: str) -> 'OceanHuedClam':
        self.time = time
        return self

    # 输出kv关系、id、局部bbox限制关系语句
    def get_this_text(self) -> str:
        limit_info = ""
        for key in self.limit_dict:
            # 开始处理key?value
            value = self.limit_dict[key].get("value")
            match self.limit_dict[key].get("relation"):
                case "exist":  # 存在key（value可不填）
                    now_info = "[\"" + key + "\"]"
                case "!exist":  # 不存在key
                    now_info = "[!\"" + key + "\"]"
                case "=":  # 存在key且对应value匹配
                    now_info = "[\"" + key + "\"" + "=\"" + value + "\"]"
                case "!=":  # 存在key但对应value不匹配 或 不存在key
                    now_info = "[\"" + key + "\"" + "!=\"" + value + "\"]"
                case "=!=":  # 必须存在key但对应value不匹配
                    now_info = "[\"" + key + "\"][\"" + key + "\"!=\"" + value + "\"]"
                case "v-reg":  # v可含正则表达式
                    now_info = "[\"" + key + "\"~\"" + value + "\"]"
                case "!v-reg":  # v可含正则表达式但不匹配
                    now_info = "[\"" + key + "\"!~\"" + value + "\"]"
                case "kv-reg":  # kv皆可含正则表达式
                    now_info = "~[\"" + key + "\"~\"" + value + "\"]"
                case "v-Aa_no_care":  # v可含正则表达式且不分大小写
                    now_info = "~[\"" + key + "\"~\"" + value + "\",i]"
                case _:
                    now_info = ""
            limit_info = limit_info + now_info
        self.text = limit_info + ";"
        return self.text
        # self.text = "data=[out:xml][timeout:" + self.time + "];" + limit_info + ";" + "out body;" 对单独语句先不写头和尾巴了，最后加

    # 取到(nwr["name"~"郁州"];)->.a;nwr.a["railway"]（如果self中有jellyfish，并指定a）
    def get_semi_full_text(self, jellyfish_used: str = "_") -> str:
        main_type = self.main_type
        jellyfish_text = ""

        for jellyfish in self.jellyfish_dict:
            jellyfish_text = jellyfish_text + self.jellyfish_dict[jellyfish].get_this_text()

        if jellyfish_used != "_":
            semi_full_text = jellyfish_text + main_type + "." + jellyfish_used + self.get_this_text()
        else:
            semi_full_text = main_type + self.get_this_text()
        return semi_full_text

    # 如果这是最中心哪个要输出的内容，则这里生成API全文
    def get_full_text(self, jellyfish_used: str = "_") -> str:
        main_type = self.main_type
        jellyfish_text = ""
        for jellyfish in self.jellyfish_dict:
            jellyfish_text = jellyfish_text + self.jellyfish_dict[jellyfish].get_this_text()
        if jellyfish_used != "_":
            full_text = "data=[out:xml][timeout:" + self.time + "];" + jellyfish_text + main_type + "." \
                        + jellyfish_used + self.get_this_text() + "out body;"
        else:
            full_text = "data=[out:xml][timeout:" + self.time + "];" + jellyfish_text + main_type \
                        + self.get_this_text() + "out body;"
        return full_text


# 要素集
class Jellyfish:
    def __init__(self, name: str, OHC: 'OceanHuedClam'):
        self.name = name
        self.OceanHuedClam = OHC

    # 取到(nwr["name"~"郁州"];)->.a;
    def get_this_text(self):
        return "(" + self.OceanHuedClam.get_semi_full_text() + ")->." + self.name + ";"