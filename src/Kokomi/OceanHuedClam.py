import copy

from global_ import print_dict
# 要按照type.A(other_condition)[k_v](if)->.B;>;的顺序和结构去整理
# TODO:不需要改变输入输出集时只需要一句话，需要怎么判断？

# 海染砗磲（QL语句）：查询要素的条件，条件取上名称后就代表符合该条件的要素集。
class OceanHuedClam:
    def __init__(self, nwr_type: str):
        self.__include_dict = {}
        self.__from_OceanHuedClam_list = []  # or列表，列表元素若是列表，则其为and
        self.__main_type = nwr_type
        self.__kv_dict = {}
        self.__around_dict = {}
        self.__global_bbox_list = []  # 南、西、北、东
        self.__id_dict = {}
        self.__recurse_dict = {}
        self.__located_in_list = []

    # 海染砗磲（QL语句）之键值关系限制语句：限定查询主体的key与value。
    #   参数1为【限定键，str】：限定必须出现或有对应值要求的键；
    #   参数2为【限制关系，str】（"exist"、"!exist"、"="、"!="、"=!="、"v-reg"、"!v-reg"、"kv-reg"、"v-Aa_no_care"）：限定键值之间的关系；
    #   参数3为【限定值，str】：对限定键的值的要求，默认为空str
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
                self.__kv_dict.update({key: {"value": value, "relation": relation}})
                return self
        else:
            print("ERROR: Undefined key-value relation.\n错误的：未定义的键值关系。\n")
            return self

    # 海染砗磲（QL语句）之周边检索：查询特定锦囊（要素）周边指定半径的内容。
    #   参数1为【中心锦囊（要素），str或list】：检索周边的圆心：
    #       str：中心锦囊集（要素集）的名称，将检索其中各锦囊（要素）周边指定半径的内容；
    #       list：由一串经纬度对组成的偶数项列表，形如[纬度1, 经度1, 纬度2, 经度2, ...]，表示各经纬度对组成的点构成的线段，将检索其周边指定半径的内容，其中：
    #           第2n-1项为float、int或str：第n个点的纬度；
    #           第2n项为float、int或str：第n个点的经度；
    #   参数2为【半径，int】：周边检索的半径，单位为米；
    # 返回OceanHuedClam：
    #   如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。
    def around(self, set_point: (str or list), r: int) -> 'OceanHuedClam':
        # 要素集合
        if isinstance(set_point, str):
            if (set_point not in self.__include_dict) and (set_point != "_"):
                print("ERROR: Not-included OceanHuedClam " + set_point + ".\n"
                      "错误的：找不到「海染砗磲」“" + set_point + "”。\n")
            else:
                self.__around_dict = {set_point: r}
        # 点串线
        else:
            if len(set_point) % 2 != 0:
                print(
                    "ERROR: Lat/lon-s not in pairs.\n错误的：传入的点串线坐标[纬度1, 经度1, 纬度2, 经度2, ...]不成对。\n")
            else:
                self.__around_dict = {r: set_point}
        return self

    # 海染砗磲（QL语句）之从海染砗磲（QL语句）提取：从满足其他海染砗磲（QL语句）的内容中进一步查询。
    #   参数1为【中心锦囊（要素），str或list】：海染砗磲（QL语句）：
    #       str：或查询（并集），单次使用本方法时输入一个集合，通过连续使用数次本方法达到从多个海染砗磲（QL语句）的并集提取；
    #       list：和查询（交集），由数个海染砗磲（QL语句）名称组成的列表，列表内的海染砗磲（QL语句）需要同时满足，呈交集；
    #             输入的列表与其他使用本方法输入的海染砗磲（QL语句）呈并集，其中：
    #           每一项均为str：需要同时满足的海染砗磲（QL语句）名称；
    # 返回OceanHuedClam：
    #   如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。
    def set_from(self, set_name: (str or list)) -> 'OceanHuedClam':
        if isinstance(set_name, str):
            if (set_name in self.__include_dict) or (set_name == "_"):
                self.__from_OceanHuedClam_list.append(set_name)
            else:
                print("ERROR: Not-included OceanHuedClam " + set_name + ".\n错误的：找不到「海染砗磲」“" + set_name + "”。\n")
        else:
            and_list = []
            for x in set_name:
                if isinstance(x, str):
                    if (x in self.__include_dict) or (x == "_"):
                        and_list.append(x)
                    else:
                        print("ERROR: Not-included OceanHuedClam " + set_name + ".\n"
                              "错误的：找不到「海染砗磲」“" + set_name + "”。\n")
                else:
                    print("ERROR: List not made up with str.\n错误的：传入列表包含非字符串元素。\n")
            if len(and_list) > 0:
                self.__from_OceanHuedClam_list.append(and_list)
                # print(self.__from_OceanHuedClam_list)
        return self

    def set_bbox(self, E: float, S: float, W: float, N: float) -> 'OceanHuedClam':
        self.__global_bbox_list = [S, W, N, E]
        return self

    def extend(self, direction: str, set_name: str = "_") -> 'OceanHuedClam':  # recurse
        self.__recurse_dict.update({set_name: direction})
        return self

    def id(self, directive_id: (int or str or list), id_opreation: str = "=") -> 'OceanHuedClam':
        if isinstance(directive_id, list):
            for x in range(len(directive_id)):
                self.__id_dict.update({str(directive_id[x]): id_opreation})
        else:
            self.__id_dict.update({str(directive_id): id_opreation})
        return self

    # 在多边形中（poly）
    def located_in(self, poly_list: list) -> 'OceanHuedClam':
        if len(poly_list) % 2 != 0:
            print("ERROR: Lat/lon-s not in pairs.\n错误的：传入的多边形坐标[纬度1, 经度1, 纬度2, 经度2, ...]不成对。\n")
        else:
            self.__located_in_list = poly_list
        return self

    def include_OceanHuedClam(self, set_name: str, the_set: 'OceanHuedClam') -> 'OceanHuedClam':
        if set_name in self.__include_dict:
            print("WARN: OceanHuedClam with the same name " + set_name + " has been included and will be replaced.\n"
                  "警示意义的：同名「海染砗磲」“" + set_name + "”已存在，将被替换。")
        self.__include_dict.update({set_name: the_set})
        print("INFO: OceanHuedClam " + set_name + " is included.\n信息：「海染砗磲」“" + set_name + "”已装备。\n")
        return self

    # TODO:判断要几个查询，并把要查询的内容返回出去，以便外部查询，step=已经进行了几步，不重复执行
    def how_many_query(self, step: int = 0) -> list:
        # TODO:添加flag_dict以便Kokomi本地筛选
        query_list = []
        # id是否需要多次查询：如果又有等号也有><，则><部分不索引id，下载完后交给Kokomi筛选
        if step == 0:
            if self.__id_dict:
                id_eq = []
                id_big = []
                id_sml = []  # 不能连等
                for directive_id in self.__id_dict:
                    match self.__id_dict[directive_id]:
                        case "=":
                            id_eq.append(directive_id)
                        case ">":
                            id_big.append(directive_id)
                        case "<":
                            id_sml.append(directive_id)
                        case _:
                            id_eq.append(directive_id)
                if len(id_eq) > 0:
                    sub_OceanHuedClam_eq = copy.deepcopy(self)
                    new_id_dict = {}
                    for x in id_eq:
                        new_id_dict.update({x: "="})
                    sub_OceanHuedClam_eq.__id_dict = new_id_dict
                    query_list.extend(sub_OceanHuedClam_eq.how_many_query(1))
                if len(id_big) > 0:
                    sub_OceanHuedClam_big = copy.deepcopy(self)
                    new_id_dict = {}
                    for x in id_big:
                        new_id_dict.update({x: ">"})
                    sub_OceanHuedClam_big.__id_dict = new_id_dict
                    query_list.extend(sub_OceanHuedClam_big.how_many_query(1))
                if len(id_sml) > 0:
                    sub_OceanHuedClam_sml = copy.deepcopy(self)
                    new_id_dict = {}
                    for x in id_sml:
                        new_id_dict.update({x: "<"})
                    sub_OceanHuedClam_sml.__id_dict = new_id_dict
                    query_list.extend(sub_OceanHuedClam_sml.how_many_query(1))
                # print("第0步完成")
            else:
                query_list.extend(self.how_many_query(1))
        # set_from：长度>1就要拆开
        if step == 1:
            if len(self.__from_OceanHuedClam_list) > 1:
                # and交集要合成一个query，or每个自己分别query：[A, B, [C,D]] = A ∪ B ∪ (C ∩ D)
                for from_OceanHuedClam in self.__from_OceanHuedClam_list:
                    sub_OceanHuedClam_from = copy.deepcopy(self)
                    sub_OceanHuedClam_from.__from_OceanHuedClam_list = [from_OceanHuedClam]
                    query_list.extend(sub_OceanHuedClam_from.how_many_query(2))
            else:
                query_list.extend(self.how_many_query(2))
                # print("第1步完成")
        if step == 2:  # 目前是最后一步
            query_list.append(self)
        return query_list

    # 仅在输出时指定的要素集名称（"...->.set_name"）；有引用的情况下，输出本「海染砗磲」时可在声明引用阶段一层一层往回带；
    # 输出QL语句列表
    def convert(self, set_name: str = "", if_main: bool = True, outputed_list=None) -> list:
        # 如果这个是主语句，最外层的，那么outputed列表应该清空
        if outputed_list is None:
            outputed_list = []
        result = ""
        # 预先处理引用
        # TODO:引用部分能不能只输出后面用了的？
        include_info = ""
        outputed = outputed_list
        for include in self.__include_dict:
            # 先把引用的"...->.set_name;"输出了，后使用set_name时名称就是一致的，然后内容也对的上（递归）
            # 如果事先已经打印了，就不重复打印，防止A->B;A,B->C中打印两次A
            if include not in outputed:
                # TODO:converted_list = ...；暂时先全部放一起，前置条件要不要分开怎么分开再想想
                for x in self.__include_dict[include].convert(include, False, outputed):
                    include_info += x
                # 合并how_many_query()至convert前：result += self.__include_dict[include].convert(include, False, outputed)
                outputed.append(include)
                # print("INFO: OceanHuedClam " + include + " is printed.\n信息：所装备的「海染砗磲」“" + include + "”已打印。\n")
        # 正式数据开始：先how_many_query()确定要几次查询
        query_list = self.how_many_query()
        result_list = []
        for each_query in query_list:
            # 每次都重置为只有include信息的，否则原来写在上面for循环之后只执行一次的话输出的内容会重复：
            # 就像这样：第一次查询include_info;node.A["name"]; 第二次include_info;node.A["name"];node.B["name"];
            result = include_info
            # 类型
            result += each_query.__main_type
            # id（使用「=」限制）
            # TODO：如果又有等号也有>< -> 这里不处理了，交给Kokomi本地筛选，预留flag位
            if each_query.__id_dict:
                id_info = ""
                eq_id_list = []
                for directive_id in each_query.__id_dict:
                    if each_query.__id_dict[directive_id] == "=":
                        eq_id_list.append(directive_id)
                if len(eq_id_list) > 0:
                    id_info = "(id:"
                    for x in range(len(eq_id_list) - 1):
                        id_info += str(eq_id_list[x]) + ","
                    id_info += str(eq_id_list[-1]) + ")"
                result += id_info
                # 有id限制时其他无法生效，直接处理集合并结束
                if set_name != "":
                    result += "->." + set_name
                print("WARN: When there is id limitation in a OceanHuedClam, other limitations cannot function.\n"
                      "警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。\n")
                result += ";"
                result_list.append(result)
                continue
            # .from_other_set
            if each_query.__from_OceanHuedClam_list:
                for from_OceanHuedClam in each_query.__from_OceanHuedClam_list:
                    if isinstance(from_OceanHuedClam, str):
                        result += "." + from_OceanHuedClam
                    else:
                        if len(from_OceanHuedClam) > 1:
                            print("INFO: OceanHuedClam " + (set_name if set_name != "" else "default") +
                                  " uses data from a intersection of multiple OceanHuedClams.\n"
                                  "信息：所装备的「海染砗磲」“" + (set_name if set_name != "" else "全集") +
                                  "”使用了多个其他「海染砗磲」的交集。\n")
                        for x in from_OceanHuedClam:
                            result += "." + x
            # around
            if each_query.__around_dict:
                around_info = ""
                for around in each_query.__around_dict:
                    # 要素集{set_point: r}；点串线{r: set_point}
                    if isinstance(around, str):
                        around_info += "(around." + around + ":" + str(each_query.__around_dict[around]) + ")"
                    else:
                        around_info += "(around" + ":" + str(around)
                        for point in each_query.__around_dict[around]:
                            around_info += "," + str(point)
                        around_info += ")"
                result += around_info
            # poly
            if each_query.__located_in_list:
                poly_info = "(poly:\""
                for x in range(len(each_query.__located_in_list) - 1):
                    poly_info += str(each_query.__located_in_list[x]) + " "
                poly_info += str(each_query.__located_in_list[len(each_query.__located_in_list) - 1]) + "\")"
            # k_v
            limit_info = ""
            for key in each_query.__kv_dict:
                value = each_query.__kv_dict[key].get("value")
                match each_query.__kv_dict[key].get("relation"):
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
                        now_info = "[~\"" + key + "\"~\"" + value + "\"]"
                    case "v-Aa_no_care":  # v可含正则表达式且不分大小写
                        now_info = "[~\"" + key + "\"~\"" + value + "\",i]"
                    case _:
                        now_info = ""
                limit_info += now_info
            result += limit_info
            # 全局界定框
            if each_query.__global_bbox_list:
                if not if_main:
                    # TODO:这个判断需要吗？
                    print(
                        "WARN: Bbox in set " + set_name + " is disabled due to it is not the main set in this query.\n"
                        "警示意义的：因为「海染砗磲」“" + set_name + "”不是最外层语句，其界定框限制不生效。\n")
                else:
                    bbox_info = "(bbox:"
                    for x in range(3):
                        bbox_info += str(each_query.__global_bbox_list[x]) + ","
                    bbox_info += str(each_query.__global_bbox_list[3]) + ")"
                    result += bbox_info
            # ->.set
            if set_name != "":
                result += "->." + set_name
            result += ";"
            # extend(recurse)
            recurse_info = ""
            if self.__recurse_dict:
                for recurse in self.__recurse_dict:
                    recurse_info += "." + recurse + self.__recurse_dict[recurse] + ";"
            result += recurse_info
            # 结束
            result_list.append(result)
        return result_list
