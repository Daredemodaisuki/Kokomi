import copy

from global_ import print_dict
# 要按照type.A(other_condition)[k_v](if)->.B;>;的顺序和结构去整理
# TODO:不需要改变输入输出集时只需要一句话，需要怎么判断？

# 海染砗磲（QL语句）：查询要素的条件，条件取上名称后就代表符合该条件的要素集。
class OceanHuedClam:
    def __init__(self, nwr_type: str):
        self.__op_list = []
        self.__include_dict = {}  # TODO:这个保留，其他逐步调整至convert中
        self.__from_OceanHuedClam_list = []  # or列表，列表元素若是列表，则其为and
        self.__main_type = nwr_type
        self.op("TPE", nwr_type)
        self.__kv_dict = {}
        self.__around_dict = {}
        self.__global_bbox_list = []  # 南、西、北、东
        self.__id_dict = {}
        self.__recurse_dict = {}
        self.__located_in_list = []

    def op(self, op: str, para1=None, para2=None, para3=None):
        op_element = None
        match op:
            # 不可变位置操作 normal / 可变位置操作 movable / 独立操作 unique
            case "TPE":  # __init__ -> main_type  # 不可变位置操作（开始）
                #                   ↓nwr_type
                op_element = {"TPE": [para1]}  # 这个貌似不用？
            case "K_V":  # key_value -> kv_dict  # 不可变位置操作  # or列表，列表元素若是列表，则其为and
                #                   ↓key, relation, value
                op_element = {"K_V": [para1, para2, para3]}
            case "ARD":  # around -> around_dict  # 不可变位置操作
                #                   ↓set/points, set_point, r
                op_element = {"ARD": [para1, para2, para3]}
            case "SET":  # set_from -> from_OceanHuedClam_list  # 不可变位置操作
                #                   ↓and/or, set_name
                op_element = {"SET": [para1, para2]}
            case "BOX":  # set_bbox -> global_bbox_list  # 不可变位置操作  # 南、西、北、东
                #                   ↓[S, W, N, E]
                op_element = {"BOX": [para1]}
            case "RCS":  # extend -> recurse_dict  # 可变位置操作
                #                   ↓set_name, direction
                op_element = {"RCS": [para1, para2]}
            case "IDe":  # id -> id_dict  # 独立操作  # id=
                #                   ↓id
                op_element = {"IDe": [para1]}
            case "IDn":  # id -> id_dict  # 不可变位置操作  # id><
                #                   ↓id, operation
                op_element = {"IDn": [para1, para2]}
            case "POL":  # located_in -> located_in_list  # 不可变位置操作
                #                   ↓poly_list
                op_element = {"POL": [para1]}
            case "ICL":  # include_OceanHuedClam -> include_dict  # 不可变位置操作
                #                   ↓name, set
                op_element = {"ICL": [para1, para2]}  # 这个貌似不用？
        self.__op_list.append(op_element)

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
                print(print_dict[0x2105])
                return self
            else:
                self.__kv_dict.update({key: {"value": value, "relation": relation}})  # TODO:后续删除
                self.op("K_V", key, relation, value)
                return self
        else:
            print(print_dict[0x2104])
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
                print(print_dict[0x2108].format(set=set_point))
            else:
                self.__around_dict = {set_point: r}  # TODO:后续删除
                self.op("ARD", "set", set_point, r)
        # 点串线
        else:
            if len(set_point) % 2 != 0:
                print(print_dict[0x2109])
            else:
                self.__around_dict = {r: set_point}  # TODO:后续删除
                self.op("ARD", "points", set_point, r)
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
                self.__from_OceanHuedClam_list.append(set_name)  # TODO:后续删除
                self.op("SET", "or", set_name)
            else:
                print(print_dict[0x210C].format(set=set_name))
        else:
            and_list = []
            for x in set_name:
                if isinstance(x, str):
                    if (x in self.__include_dict) or (x == "_"):
                        and_list.append(x)
                    else:
                        print(print_dict[0x210C].format(set=set_name))
                else:
                    print(print_dict[0x210D])
            if len(and_list) > 0:
                self.__from_OceanHuedClam_list.append(and_list)  # TODO:后续删除
                self.op("SET", "and", set_name)
        return self

    def set_bbox(self, E: float, S: float, W: float, N: float) -> 'OceanHuedClam':
        self.__global_bbox_list = [S, W, N, E]  # TODO:后续删除
        self.op("BOX", [S, W, N, E])
        return self

    def extend(self, direction: str, set_name: str = "_") -> 'OceanHuedClam':  # recurse
        self.__recurse_dict.update({set_name: direction})  # TODO:后续删除
        self.op("RCS", set_name, direction)
        return self

    def id(self, directive_id: (int or str or list), id_operation: str = "=") -> 'OceanHuedClam':
        if isinstance(directive_id, list):
            for x in range(len(directive_id)):
                self.__id_dict.update({str(directive_id[x]): id_operation})  # TODO:后续删除
                if id_operation == "=":
                    self.op("IDe", directive_id[x])
                else:
                    self.op("IDn", directive_id[x], id_operation)
        else:
            self.__id_dict.update({str(directive_id): id_operation})  # TODO:后续删除
            if id_operation == "=":
                self.op("IDe", directive_id)
            else:
                self.op("IDn", directive_id, id_operation)
        print(print_dict[0x1114])
        return self

    # 在多边形中（poly）
    def located_in(self, poly_list: list) -> 'OceanHuedClam':
        if len(poly_list) % 2 != 0:
            print(print_dict[0x2110])
        else:
            self.__located_in_list = poly_list  # TODO:后续删除
            self.op("POL", poly_list)
        return self

    def include_OceanHuedClam(self, set_name: str, the_set: 'OceanHuedClam') -> 'OceanHuedClam':
        if set_name in self.__include_dict:
            print(print_dict[0x1100].format(set=set_name))
        self.__include_dict.update({set_name: the_set})  # 这个要保留
        self.op("ICL", set_name, the_set)
        print(print_dict[0x0100].format(set=set_name))
        return self

    # 输出相关内容

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

    def __op_type(self, op: str) -> str:
        movable_op_list = ["RCS"]
        end_op_list = ["IDe"]
        start_op_list = ["TPE"]
        if not (op in movable_op_list or op in end_op_list or op in start_op_list):
            op_type = "normal"
        elif op in start_op_list:
            op_type = "start"
        elif op in movable_op_list:
            op_type = "movable"
        else:
            op_type = "unique"
        return op_type

    def convert_new(self, set_name: str = "", if_main: bool = True, outputed_list=None) -> list:
        # 如果这个是主语句，最外层的，那么outputed列表应该清空
        temp_set_name = ""
        if outputed_list is None:
            outputed_list = []
        result_info = ""

        # 预先处理引用
        # TODO:引用部分能不能只输出后面用了的？
        include_info = ""
        outputed = outputed_list
        for include in self.__include_dict:
            # 先把引用的"...->.set_name;"输出了，后使用set_name时名称就是一致的，然后内容也对的上（递归）
            # 如果事先已经打印了，就不重复打印，防止A->B;A,B->C中打印两次A
            if include not in outputed:
                # TODO:converted_list = ...；暂时先全部放一起，前置条件要不要分开怎么分开再想想
                for x in self.__include_dict[include].convert_new(include, False, outputed):
                    include_info += x
                # 合并how_many_query()至convert前：result += self.__include_dict[include].convert(include, False, outputed)
                outputed.append(include)
                # print("INFO: OceanHuedClam " + include + " is printed.\n信息：所装备的「海染砗磲」“" + include + "”已打印。\n")
        result_info += include_info

        # 正式数据开始
        # 分段：除了可变位置、独立操作，其余操作可以乱序，所以先寻找需要不同的操作并分段，每段只有一种操作
        op_segment_list = []
        op_start = 0
        op_end = 0
        this_op_type = "start"
        now_op_type = "start"
        same_type_op_list = []
        for x in range(len(self.__op_list)):
            # 提取op标识符
            op_id = list(self.__op_list[x].keys())[0]
            # print(op, self.__op_list[x][op_id])
            # 判断op类型
            this_op_type = self.__op_type(op_id)
            if this_op_type != now_op_type:
                op_end = x  # 找到相同类型op的最后一个，将op类型和同类op添加到段
                op_segment_list.append([now_op_type, self.__op_list[op_start: op_end]])
                op_start = x
                now_op_type = this_op_type
        # 最后一段（前面for循环寻到最后一段因为没有变化不会直接添加，for完成之后this_op_type即是最后一个的、最后一段的type）
        op_segment_list.append([this_op_type, self.__op_list[op_start:len(self.__op_list)]])

        # 分组：判断是下列哪种情况，并将符合条件的段组在一起：
        #   纯不可变位置操作段：type.A(other_conditionL)[k_v](other_conditionR)->.B;
        #   纯独立操作段：type(id)->.B;
        #   不可变位置操作段+可变位置操作段：type.A(other_conditionL)[k_v](other_conditionR)->.B;.B < ->.C;
        #   独立操作段+可变位置操作段：type(id)->.A;.A < ->.B;
        # 上述句法只有最后一个集合名称是convert的set_name参数
        '''==下面一部分基于 New Bing 写的（偷懒）==

        在python中，有1个列表，里面包含多个数字，现在<1的数字属于A类，1~10之间的属于B类，>10的属于C类，
        如果希望分割该列表为数个列表，每个分出的子列表均满足下列4种条件之一：
        1）子列表全部由A类数字组成；
        2）子列表全部由B类数字组成；
        3）子列表最后一项为C类，其余全部由A类数字组成；
        4）子列表最后一项为C类，其余全部由B类数字组成，
        可以如何分割？
        
        def split_list(lst):
            result = []
              temp = []
        for i in lst:
            if i < 1:
                temp.append(i)
            elif 1 <= i <= 10:
                temp.append(i)
            else:
                temp.append(i)
                result.append(temp)
                temp = []
        if temp:
            result.append(temp)
        return result
        
        整挺好，但可能会出现A、B类数字混合在一起的情况，故还需要添加判断是否同temp前一项相同
        '''
        op_group_list = []
        op_group_temp = []
        for op_segment in op_segment_list:
            print(op_segment)
            if op_segment[0] == "start" or op_segment[0] == "normal":
                # 跟temp上一个一不一样，不一样就把之前一样的temp甩给result_list，刷新temp，否则在temp添加op
                if op_group_temp and (op_group_temp[-1][0] == "start" or op_group_temp[-1][0] == "normal"):
                    op_group_temp.append(op_segment)
                else:
                    if op_group_temp:
                        op_group_list.append(op_group_temp)
                    op_group_temp = [op_segment]
            elif op_segment[0] == "unique":
                if op_group_temp and op_group_temp[-1][0] == "unique":
                    op_group_temp.append(op_segment)
                else:
                    if op_group_temp:
                        op_group_list.append(op_group_temp)
                    op_group_temp = [op_segment]
            else:
                op_group_temp.append(op_segment)
                op_group_list.append(op_group_temp)
                op_group_temp = []
        if op_group_temp:
            op_group_list.append(op_group_temp)
        # 按照4类重组后，start必是第一组第一段op_segment，如果其后是normal段，则合并，
        if len(op_group_list[0]) > 1 and op_group_list[0][1][0] == "normal":
            new_op_group = copy.deepcopy(op_group_list)
            op_group_temp = new_op_group[0][0][1]  # [{'TPE': ['nwr']}]
            op_group_temp.extend(new_op_group[0][1][1])
            new_op_group[0][0] = ["normal", op_group_temp]
            if len(new_op_group[0]) > 2:
                for x in range(len(new_op_group[0]) - 2):
                    new_op_group[0][x + 1] = new_op_group[0][x + 2]
            op_group_list[0] = new_op_group[0][0:len(new_op_group[0]) - 1]

        # 对每个op组的每个op段按别不可变位置、可变位置、独立操作开刀
        '''
        match op:
            # 不可变位置操作 normal / 可变位置操作 movable / 独立操作 unique
            case "TPE":  # __init__ -> main_type  # 不可变位置操作
                #                   ↓nwr_type
                op_element = {"TPE": [para1]}  # 这个貌似不用？
            case "K_V":  # key_value -> kv_dict  # 不可变位置操作  # or列表，列表元素若是列表，则其为and
                #                   ↓key, relation, value
                op_element = {"K_V": [para1, para2, para3]}
            case "ARD":  # around -> around_dict  # 不可变位置操作
                #                   ↓set/points, set_point, r
                op_element = {"ARD": [para1, para2, para3]}
            case "SET":  # set_from -> from_OceanHuedClam_list  # 不可变位置操作
                #                   ↓and/or, set_name
                op_element = {"SET": [para1, para2]}
            case "BOX":  # set_bbox -> global_bbox_list  # 不可变位置操作  # 南、西、北、东
                #                   ↓[S, W, N, E]
                op_element = {"BOX": [para1]}
            case "RCS":  # extend -> recurse_dict  # 可变位置操作
                #                   ↓set_name, direction
                op_element = {"RCS": [para1, para2]}
            case "IDe":  # id -> id_dict  # 独立操作  # id=
                #                   ↓id
                op_element = {"IDe": [para1]}
            case "IDn":  # id -> id_dict  # 不可变位置操作  # id><
                #                   ↓id, operation
                op_element = {"IDn": [para1, para2]}
            case "POL":  # located_in -> located_in_list  # 不可变位置操作
                #                   ↓poly_list
                op_element = {"POL": [para1]}
            case "ICL":  # include_OceanHuedClam -> include_dict  # 不可变位置操作
                #                   ↓name, set
                op_element = {"ICL": [para1, para2]}  # 这个貌似不用？
        '''
        #   纯不可变位置操作段：type.A(other_conditionL)[k_v](other_conditionR)->.B;
        #   纯独立操作段：type(id)->.B;
        #   不可变位置操作段+可变位置操作段：type.A(other_conditionL)[k_v](other_conditionR)->.B;.B < ->.C;
        #   独立操作段+可变位置操作段：type(id)->.A;.A < ->.B;
        for op_group in op_group_list:
            print(op_group)

            # segment_result_info = self.__main_type
            from_OceanHuedClam_list = []  # or列表，列表元素若是列表，则其为and
            # main_type = nwr_type
            kv_dict = {}
            around_dict = {}
            global_bbox_list = []  # 南、西、北、东
            id_dict = {}
            recurse_dict = {}
            located_in_list = []
            group_result_info = ""
            for op_segment in op_group:
                # 将不可变位置操作段中的信息保存以备输出
                match op_segment[0]:
                    case "normal":
                        for op in op_segment[1]:
                            op_id = list(op.keys())[0]
                            # op = {op_id: [para1, para2, para3]}
                            # op[op_id] = [para1, para2, para3]
                            # op[op_id][0] = para1
                            match op_id:
                                case "TPE":
                                    continue
                                case "K_V":
                                    # {key: {"value": value, "relation": relation}}
                                    kv_dict.update({op[op_id][0]: {"value": op[op_id][2], "relation": op[op_id][1]}})
                                case "ARD":
                                    # 数据集{set_point: r} 点串线{r: set_point}
                                    if op[op_id][0] == "set":
                                        around_dict.update({op[op_id][1]: op[op_id][2]})
                                    else:
                                        around_dict.update({op[op_id][2]: op[op_id][1]})
                                case "SET":
                                    from_OceanHuedClam_list.append(op[op_id][1])
                                case "BOX":
                                    if global_bbox_list:
                                        print(print_dict[0x11C0])
                                    global_bbox_list = op[op_id][0]
                                # case "IDn":  # TODO:flag位
                                case "POL":
                                    located_in_list = op[op_id][0]
                                case "ICL":
                                    continue
                                case _:
                                    print(print_dict[0x31C0].format(op_id=op_id))

                        # 整体输出不可变位置操作

                        # from_other_set（并集）
                        if len(from_OceanHuedClam_list) > 1:
                            from_info = "("
                            for from_OceanHuedClam in from_OceanHuedClam_list:
                                if isinstance(from_OceanHuedClam, str):
                                    from_info += self.__main_type + "." + from_OceanHuedClam + ";"
                                else:
                                    from_info += self.__main_type
                                    for x in from_OceanHuedClam:
                                        from_info += "." + x
                                    from_OceanHuedClam += ";"
                            temp_set_name = "temp" + str(hash(from_info))[0:4]  # 用hash取个名字
                            from_info += ")->." + temp_set_name + ";"
                            group_result_info += from_info

                        # type
                        group_result_info += self.__main_type

                        # from_other_set（单个集合/交集）
                        if len(from_OceanHuedClam_list) == 1:
                            from_info = ""
                            if isinstance(from_OceanHuedClam_list[0], str):
                                from_info += "." + from_OceanHuedClam_list[0]
                            else:
                                if len(from_OceanHuedClam_list[0]) > 1:
                                    print(print_dict[0x11A0]
                                          .format(set=(set_name if set_name != "" else "default")))
                                for x in from_OceanHuedClam_list[0]:
                                    from_info += "." + x
                            group_result_info += from_info
                        else:  # 并集：前面把并集写出来了，现在缀到type后面
                            if from_OceanHuedClam_list:
                                group_result_info += "." + temp_set_name

                        # around
                        if around_dict:
                            around_info = "(around."
                            for around in around_dict:
                                # 要素集{set_point: r}；点串线{r: set_point}
                                if isinstance(around, str):
                                    around_info += around + ":" + str(
                                        around_dict[around]) + ")"
                                else:
                                    around_info += ":" + str(around)
                                    for point in around_dict[around]:
                                        around_info += "," + str(point)
                                    around_info += ")"
                            group_result_info += around_info

                        # poly
                        if located_in_list:
                            poly_info = "(poly:\""
                            for x in range(len(located_in_list) - 1):
                                poly_info += str(located_in_list[x]) + " "
                            poly_info += str(
                                located_in_list[len(located_in_list) - 1]) + "\")"
                            group_result_info += poly_info

                        # k_v
                        if kv_dict:
                            kv_info = ""
                            print(kv_dict)
                            for key in kv_dict:
                                value = kv_dict[key].get("value")
                                match kv_dict[key].get("relation"):
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
                                        print(print_dict[0x31C1].format(relation=kv_dict[key].get("relation")))
                                kv_info += now_info
                            group_result_info += kv_info

                        # ->.set
                        if set_name != "":
                            group_result_info += "->." + set_name
                        group_result_info += ";"
                        print("op-group:", op_group, "\n>>>", group_result_info)

                    case "":
                        group_result_info = ""
            result_info += group_result_info
        return [result_info]

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
                            print(print_dict[0x11A0].format(set=(set_name if set_name != "" else "default")))
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
                    print(print_dict[0x11A1].format(set=set_name))
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
