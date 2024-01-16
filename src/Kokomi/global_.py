# 全局常量
print_dict = {
    # Kokomi
    0x0000: "INFO: Kokomi is ready.\n"
            "Kokomi就绪。\n",
    0x0001: "INFO: Define Sangonomiya(Overpass) for Watatsumi(Network) successfully.\n"
            "信息：已在海祇岛上建立珊瑚宫。（指定Overpass成功）：\n"
            "  {name} {api}\n",
    0x0010: "INFO: Kokomi is finding in Sangonomiya(Overpass).\n"
            "信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜：",  # 下接http-request的地址
    0x0011: "INFO: Kokomi is finding in Sangonomiya(Overpass) ( {now} / {total} ):\n"
            "信息：Kokomi正在珊瑚宫（Overpass）翻箱倒柜（第 {now} 次/共 {total} 次）：",  # 下接http-request的地址
    0x0012: "INFO: {number} {type}(s) have been found.\n"
            "信息：Kokomi找到了 {number} 个 {type}。\n",

    0x1001: "WARN: Self-defined Sangonomiya(Overpass) set.\n"
            "警示意义的：你正在使用自定义的珊瑚宫（Overpass）配置:\n"
            "  {name} {api}\n",

    0x2000: "ERROR: No Sangonomiya(Overpass) info.\n"
            "错误的：珊瑚宫（Overpass）未指定。\n",
    0x2001: "ERROR: Uncompleted Sangonomiya(Overpass) set.\n"
            "错误的：珊瑚宫（Overpass）配置不完整。\n",
    0x2002: "ERROR: Undefined Sangonomiya(Overpass) preset.\n"
            "错误的：没有定义的珊瑚宫（Overpass）预设配置。\n",
    0x2010: "ERROR: No info from Sangonomiya(Overpass).\n"
            "错误的：珊瑚宫（Overpass）没有回传任何信息。\n",
    0x2011: "",  # 超时
    0x201A: "ERROR: Undefined Directive(Feature) type: {type}.\n"
            "错误的：没有定义的锦囊（要素）类型：{type}。\n",

    # OceanHuedClam
    0x0100: "INFO: OceanHuedClam  {set}  is included.\n"  # include
            "信息：「海染砗磲」“{set}”已装备。\n",

    0x1100: "WARN: OceanHuedClam with the same name {set} has been included and will be replaced.\n"  # include
            "警示意义的：同名「海染砗磲」“{set}”已存在，将被替换。",
    0x1114: "WARN: When there is id limitation in an OceanHuedClam, other limitations cannot function.\n"  # id
            "警示意义的：使用id限定后，其他「海染砗磲」条件无法生效。\n",
    0x11A0: "INFO: OceanHuedClam {set} uses data from a intersection of multiple OceanHuedClams.\n"  # convert
            "信息：所装备的「海染砗磲」“{set}”使用了多个其他「海染砗磲」的交集。\n",
    0x11A1: "WARN: Bbox in set {set} is disabled due to it is not the main set in this query.\n"
            "警示意义的：因为「海染砗磲」“{set}”不是最外层语句，其界定框限制不生效。\n",
    0x11C0: "WARN: Multiple bboxes have been set in one OceanHuedClam op-group.\n"  # new convert
            "警示意义的：在同一「海染砗磲」方法组中出现了多个界定框方法，仅生效最后一个。\n",

    0x2104: "ERROR: Undefined key-value relation.\n"  # k_v
            "错误的：未定义的键值关系。\n",
    0x2105: "ERROR: Value needed except exist and !exist.\n"
            "错误的：除exist、!exist条件外需要键的值。\n",
    0x2108: "ERROR: Not-included OceanHuedClam {set}.\n"  # around
            "错误的：找不到「海染砗磲」“{set}”。\n",
    0x2109: "ERROR: Lat/lon-s not in pairs.\n"
            "错误的：传入的点串线坐标[纬度1, 经度1, 纬度2, 经度2, ...]不成对。\n",
    0x210C: "ERROR: Not-included OceanHuedClam {set}.\n"  # set_from
            "错误的：找不到「海染砗磲」“{set}”。\n",
    0x210D: "ERROR: Name list not made up with str.\n"
            "错误的：传入名称列表包含非字符串元素。\n",
    0x2110: "ERROR: Lat/lon-s not in pairs.\n"  # located_in
            "错误的：传入的多边形坐标[纬度1, 经度1, 纬度2, 经度2, ...]不成对。\n",
    # 内部错误
    0x31C0: "【 ↓ 内部错误】\n"
            "ERROR: Unacceptable OceanHuedClam op-id \"{op_id}\".\n"  # new convert
            "错误的：处理方法段时传入了不可接受方法标识符「{op_id}」。\n",
    0x31C1: "【 ↓ 内部错误】\n"
            "ERROR: Unacceptable key_value relation \"{relation}\".\n"
            "错误的：处理方法段-k_v关系时传入了不可接受的关系参数「{relation}」。\n",

}
