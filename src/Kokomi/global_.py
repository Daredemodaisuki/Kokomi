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
}
