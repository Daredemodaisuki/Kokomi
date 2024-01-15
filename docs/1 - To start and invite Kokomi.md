↑ 已是尽头
[↓ 海染砗磲 · 查询语句基础](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/2%20-%20QL%20with%20OceanHuedClam.md)

## Ⅰ 开始
### 1.请邀请Kokomi：

Kokomi暂时不需要其他的三方库，欲邀请Kokomi及各附属，请：

```python
from src.Kokomi.main import *
```

### 2.请赋予Kokomi在你的文件的中一个化身：

  示例：
```python
waifu = Kokomi()
```

## Ⅱ 请Kokomi查询

### 1.为Kokomi所在的海祇岛【Watatsumi（Network）】指定珊瑚宫【Sangonomiya（Overpass）】：

使用Watatsumi_set函数可以指定珊瑚宫（Overpass），其：
+ 参数1为【预设名称，str】（"OSMde"、"OSMru"、"OGF"、"None"）：使用预设珊瑚宫（Overpass）伺服器配置，或不使用预设（"None"）；
+ 参数2为【自定名称，str】：参数1为"None"时，自定义珊瑚宫（Overpass）伺服器名称，默认为空；
+ 参数3为【自定API地址，str】：参数1为"None"时，自定义珊瑚宫（Overpass）伺服器API地址，填写至"interpreter?..."前，默认为空。

  返回int：
+ 【1】：成功使用预设配置；
+ 【0】：成功使用自定义配置；
+ 【-1】：使用了未定义的预设名称；
+ 【-2】：不完整的自定义配置。

示例：
```python
waifu.Watatsumi_set("OSMde")
```

  后续Kokomi会在你指定的珊瑚宫（Overpass）寻找数据。

### 2.告诉Kokomi希望查询的内容：

使用query函数可以请她帮帮忙，在前述指定的珊瑚宫（Overpass）寻找一些锦囊（OSM要素）数据，此函数：
+ 参数1为【查询指令，str或OceanHuedClam】：在珊瑚宫（Overpass）查询的参数，默认为空str：
    + str：以“data="后开始，当然返回的报文也会告诉你不给东西查不到；
    + list：传入一个海染砗磲（QL语句）对象，并直接按照其中设置的条件查询；
+ 参数2为【延时，int】：设置最大超时时长，默认为500，单位为秒；

  返回int：
+ 【2】：向珊瑚宫（Overpass）成功地GET了报文；
+ 【-1】：珊瑚宫（Overpass）没有传回任何消息，可能是海祇岛（Network）连接原因；
+ 【-2】：珊瑚宫（Overpass）api未指定。
  
如果您已经对各珊瑚宫（Overpass）的QL语句十分甚至九分熟悉，你可以直接写QL语句，即填入str；关于海染砗磲（QL语句）详见[海染砗磲 · 查询语句基础](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/2%20-%20QL%20with%20OceanHuedClam.md)。

示例：请帮我找一找名称为“粮站院内”（name=粮站院内）的锦囊（要素）node
    
```python
waifu.query("data=[out:xml][timeout:25];node[\"name\"=\"粮站院内\"];out body;")
```

稍等片刻，她会将找到的全部数据报报文先存在她的directive_text_temp中，然后她会把数据归类，存储在directive_dict中，并且给你如下的答复：
  
```
INFO: 4 node (s) have been found.
信息：Kokomi找到了 4 个 node 。

INFO: 0 way (s) have been found.
信息：Kokomi找到了 0 个 way 。

INFO: 0 relation (s) have been found.
信息：Kokomi找到了 0 个 relation 。
```

ℹ 数据截止至2023年6月26日。

### 3.查看内容：

上回书说到，彼时的Kokomi会把数据归类，但注意，她目前是在手撸XML（人话：通过“</”之类的关键字做切割，说不准来个阿拉伯文她也会头大），她把分好的内容放在了directive_dict中，包含“点（node）”“线（way）”“关系（relation）”三类，里面长这样：

```python
{"node": {
  {点ID: {
            "type": "node",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},  # 空的
            "node_list": [],  # 空的
            "text": 报文全文,
            "lon_lat": [经度, 纬度]
            },
        ...
        }
    },
 "way": {
  {线ID: {
            "type": "way",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},  # 空的
            "node_list": [ID1, ID2, ...],
            "text": 报文全文,
            "lon_lat": []  # 空的
            },
        ...
        }
    },
 "relation": {
  {关系ID: {
            "type": "relation",
            "tag_dict": {键名: 值, ...},
            "member_dict": {成员类型 + ID: 角色, ...},
            "node_list": [],  # 空的
            "text": 报文全文,
            "lon_lat": []  # 空的
            },
        ...
        }
    },
}
```

其中，所有内容均为str。

#### ① 读某个锦囊（要素）的tag

按照珊瑚宫（Overpass）的要求，对于前述三类锦囊（要素），如果有用于描述它们的tag，那tag会包括“键（key）”与“值（value）”两部分。Kokomi将它们放在了directive_dict字典>对应锦囊（要素）类别的分字典>对应锦囊ID的锦囊（要素）字典>tag字典中，可以一级一级的向下读，并返回你需要的内容。

示例：遍历directive_dict中的所有锦囊（要素）中点的名称（键为“name”，如果有）：
    
```python
for nodeID in waifu.directive_dict.get("node")[nodeID]:
  if "name" in nodeID["tag_dict"]:
    print nodeID["tag_dict"]["name"]
```

#### ② 对于线、关系

线和关系比点额外多出一些内容：线的内容中有构成其的拐点的ID，关系包含组成其的成员类型、ID和在关系中的角色，可以按照读取tag类似的方法实现，但注意，关系的member_dict中的字典ID是成员类型和ID（数字）的组合。

↑ 已是尽头
[↓ 海染砗磲 · 查询语句基础](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/2%20-%20QL%20with%20OceanHuedClam.md)
