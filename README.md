# Kokomi

  一位用派森构造的贴心伙伴，可以提供较QL来说视觉稍友好的Overpass查询指令（但注意，其本质还是基于QL的）并且可以做一些轻量的查询工作，当然，Kokomi也可以作为QL生成帮手（不是）；最后，Kokomi不涉及数据更改。
  
  A python-based Overpass querier.

## Ⅰ 开始
### 1.Kokomi暂时不需要其他的三方库，欲邀请Kokomi，请：

```python
from main import Kokomi
```

### 2.当然请不要忘记带上她心爱的海染套（OceanHuedClam）：

```python
from main import OceanHuedClam
```

ℹ 这是现阶段的，后续合并了就只用 import Kokomi 了。

### 3.请赋予Kokomi在你的文件的中一个化身：

  示例：
```python
waifu = Kokomi()
```


## Ⅱ 请Kokomi查询
### 1.为Kokomi所在的海祇岛【Watatsumi（Network）】指定珊瑚宫【Sangonomiya（Overpass）】：

  使用Watatsumi_set函数可以指定Sangonomiya，其：
+ 参数1为【预设名称，str】（"OSMde"、"OSMru"、"OGF"、"None"）：使用预设珊瑚宫（Overpass）伺服器配置，或不使用预设（"None"）；
+ 参数2为【自定名称，str】：参数1为"None"时，自定义珊瑚宫伺服器名称，默认为空；
+ 参数3为【自定API地址，str】：参数1为"None"时，自定义珊瑚宫伺服器API地址，填写至"interpreter?..."前，默认为空。

  返回int：
+ 【1】：成功使用预设配置；
+ 【0】：成功使用自定义配置；
+ 【-1】：使用了未定义的预设名称；
+ 【-2】：不完整的自定义配置。

  示例：
```python
waifu.Watatsumi_set("OSMde")
```

  后续Kokomi会在你指定的Sangonomiya寻找数据。

### 2.告诉Kokomi希望查询的内容：

  使用query函数可以请她帮帮忙，在前述指定的珊瑚宫寻找一些锦囊（OSM要素）数据，此函数：
+ 参数1为【查询指令，str】：在珊瑚宫（Overpass）查询的参数，以“data="后开始，默认为空，当然返回的报文也会告诉你不给东西查不到。

  返回int：
+ 【2】：向珊瑚宫成功地GET了报文；
+ 【-1】：珊瑚宫没有传回任何消息，可能是海祇岛（Network）连接原因；
+ 【-2】：珊瑚宫api未指定。
  
  如果你已经对各珊瑚宫的QL语句十分甚至九分熟悉，你可以直接写QL条件。
  
    示例：请帮我找一找名称为“粮站院内”（name=粮站院内）的锦囊点
    
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

  上回书说到，彼时的Kokomi会把数据归类，但注意，她目前是在手搓XML（说不准来个阿拉伯文她也会头大），她把分好的内容放在了directive_dict中，里面长这样：

```python
{"node": {
  {点ID: {
            "type": "node",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},
            "node_list": []
            "text": 报文全文
            },
        ...
        }
    },
 "way": {
  {线ID: {
            "type": "way",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},
            "node_list": [ID1, ID2, ...]
            "text": 报文全文
            },
        ...
        }
    },
 "relation": {
  {关系ID: {
            "type": "relation",
            "tag_dict": {键名: 值, ...},
            "member_dict": {成员类型 + ID: 角色, ...},
            "node_list": []
            "text": 报文全文
            },
        ...
        }
    },
}
```

## N 一些应用场景示例

+ 我想查询一些地名，做一个词库，方便调教输入法；
+ 我想看看某物大概在某地有多少，做个小统计；
+ 我只是单纯查个要素，但看QL很吃力，不想单独学QL或开JOSM了；
+ ……
