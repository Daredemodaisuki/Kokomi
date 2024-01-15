import requests

from global_ import print_dict

class Kokomi:
    def __init__(self):
        self.energy = 50
        self.check_energy = 1
        self.directive_type = ["node", "way", "relation"]
        self.directive_dict = {"node": {}, "way": {}, "relation": {}}
        self.directive_text_temp = ""
        self.Watatsumi = {"Sangonomiya_name": "", "Sangonomiya_api": ""}
        # Sangonomiya_name = Overpass_name, Sangonomiya_api = Overpass_api
        print(print_dict[0x0000])

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
            print(print_dict[0x0001].format(name=self.Watatsumi["Sangonomiya_name"],
                                            api=self.Watatsumi["Sangonomiya_api"]))
            self.energy = self.energy + 1
            return 1
        else:
            if preset == "None":
                if name != "" and api != "":
                    self.Watatsumi["Sangonomiya_name"] = name
                    self.Watatsumi["Sangonomiya_api"] = api
                    print(print_dict[0x1001].format(name=self.Watatsumi["Sangonomiya_name"],
                                                    api=self.Watatsumi["Sangonomiya_api"]))
                    self.energy = self.energy + 0
                    return 0
                else:
                    print(print_dict[0x2001])
                    self.energy = self.energy - 2
                    return -2
            else:
                print(print_dict[0x2000])
                self.energy = self.energy - 1
                return -1

    # 查询要素：本次查询收到的报文将储存在kokomi的临时锦囊（directive_text_temp）中，并调用get_directive_dict处理信息。
    #   参数1为【查询指令，str或OceanHuedClam】：在珊瑚宫（Overpass）查询的参数，默认为空str，其中：
    #       str：以“data="后开始，当然返回的报文也会告诉你不给东西查不到。
    #       OceanHuedClam：传入一个海染砗磲对象，并直接按照其中设置的条件查询
    #   参数2为【延时，int】：设置最大超时时长，默认为500。
    # 返回list，其中：
    #   第1项为int：总分割查询次数n；
    #   随后n项，每项均为int：每次查询结果：
    #   【2】：向珊瑚宫成功地GET了报文；
    #   【-1】：珊瑚宫没有传回任何消息，可能是海祇岛（Network）连接原因；
    #   【-2】：珊瑚宫api未指定。
    def query(self, query_info: (str or 'OceanHuedClam') = "", timeout: int = 500) -> list:
        self.energy_check()
        result_list = []
        if isinstance(query_info, str):
            print("INFO: Kokomi is finding in Sangonomiya(Overpass).\n信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜：")
            result_list.append(1)
            result = self.get_content("data=[out:xml][timeout:" + str(timeout) + "];" + query_info + "out body;")
            result_list.append(result)
        else:
            query_list = query_info.convert()
            result_list.append(len(query_list))
            for x in range(len(query_list)):
                print("INFO: Kokomi is finding in Sangonomiya(Overpass) (", x + 1, "/", len(query_list), "):\n"
                      "信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第", x + 1, "次/共", len(query_list), "次）：")
                result = self.get_content("data=[out:xml][timeout:" + str(timeout) + "];" + query_list[x] + "out body;")
                result_list.append(result)
        return result_list

    def get_content(self, query_info: str = ""):
        print(self.Watatsumi["Sangonomiya_api"] + "interpreter?" + query_info, "\n")
        if self.Watatsumi["Sangonomiya_api"] == "":
            print("ERROR: No Sangonomiya(Overpass) info.\n错误的：珊瑚宫（Overpass）未指定。\n")
            self.energy = self.energy - 2
            return -2
        else:
            text_temp = requests.get(self.Watatsumi["Sangonomiya_api"] + "interpreter?" + query_info).text
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
    # 返回dict，其中：
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
                # 如果“"/>”比“">”先来，那说明只有一行，结尾是“/>“（/>不取双引号"因为取id要用）
                # TODO：经纬度
                if directive_text.find("/>", directive_front) < directive_text.find("\">", directive_front):
                    directive_behind = directive_text.find("/>", directive_front)
                else:  # 否则是很多行，结尾是"</" + directive_type + ">"
                    directive_behind = directive_text.find("</" + directive_type + ">", directive_front)
                dealt_text = directive_text[directive_front: directive_behind]
                directive_found = directive_found + 1

                # 找id
                id_front = dealt_text.find("id=\"") + 4
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