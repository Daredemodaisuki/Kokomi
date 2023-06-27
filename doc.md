## Ⅰ 开始

### 1.Kokomi暂时不需要其他的三方库，欲邀请Kokomi，请：

```python
from main import Kokomi
```

### 2.当然请不要忘记带上她心爱的海染砗磲【OceanHuedClam（QL语句）】和水母【Jellyfish（要素集）】：

```python
from main import OceanHuedClam
from main import Jellyfish
```

ℹ 这是现阶段的，后续合并了就只用 import Kokomi 了。

### 3.请赋予Kokomi在你的文件的中一个化身：

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
+ 参数1为【查询指令，str】：在珊瑚宫（Overpass）查询的参数，以“data="后开始，默认为空，当然返回的报文也会告诉你不给东西查不到。

  返回int：
+ 【2】：向珊瑚宫（Overpass）成功地GET了报文；
+ 【-1】：珊瑚宫（Overpass）没有传回任何消息，可能是海祇岛（Network）连接原因；
+ 【-2】：珊瑚宫（Overpass）api未指定。
  
如果你已经对各珊瑚宫（Overpass）的QL语句十分甚至九分熟悉，你可以直接写QL条件。

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

上回书说到，彼时的Kokomi会把数据归类，但注意，她目前是在手撸XML（人话：通过“</”之类的关键字做切割，说不准来个阿拉伯文她也会头大），她把分好的内容放在了directive_dict中，包含“点（node）”“线（way）”“关系（relation）”三类，里面长这样：

```python
{"node": {
  {点ID: {
            "type": "node",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},  # 空的
            "node_list": []  # 空的
            "text": 报文全文
            },
        ...
        }
    },
 "way": {
  {线ID: {
            "type": "way",
            "tag_dict": {键名: 值, ...},
            "member_dict": {},  # 空的
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
            "node_list": []  # 空的
            "text": 报文全文
            },
        ...
        }
    },
}
```

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

## Ⅲ 使用海染砗磲（QL语句）和水母（要素集）帮助Kokomi更精确地查询

如果你对珊瑚宫（Overpass）的QL语句不是很熟悉，或者单纯嫌看着难受，可以考虑给Kokomi刷一套海染砗磲（QL语句）来生成QL语句方便她查询，当需求比较复杂，可以配合水母（要素集）帮你奶一口。

### 1. 海染砗磲

海染（音：hǎirǎn）砗磲在这里的概念是QL语句，一个海染砗磲对象就是代表一条QL语句，可以用来做内容限定，比如要求返回的锦囊（要素）有特定名称。

当你想做限定时，刷一个海染砗磲，其初始化方法中：
+ 参数1为【限定主体的类型】（"node"、"way"、"relation"、"nw"、"nr"、"wr"、"nwr"）：说明该海染砗磲是用来查询或者修饰何种类型的锦囊（要素），括号中的后4中类型为点线关系的2个或3个的组合，可以同时查询多种锦囊（要素）。

示例：

```python
limit1 = OceanHuedClam("nwr")
```

然后，对要查询的内容做限定，有如下一些方法：

```python
① def key_value(self, key: str, relation: str, value: str = "") -> 'OceanHuedClam':
② def ...  # TODO
```

使用海染砗磲的方法时直接将方法追加至现有的海染砗磲后，可以连续追加。

#### ① key_value方法

此方法用于限定查询主体的键值关系，其：
+ 参数1为【限定键】：限定必须出现或有对应值要求的键；
+ 参数2为【限制关系】（"exist"、"!exist"、"="、"!="、"=!="、"v-reg"、"!v-reg"、"kv-reg"、"v-Aa_no_care"）：限定键值之间的关系；
+ 参数3为【限定值】：对限定键的值的要求

  返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；
+ 否则原样不动地返回。

参数2括号中的值的意思如下：
+ "exist"：存在key，此时参数3的value可不填
+ "!exist"：不存在key，此时参数3的value可不填
+ "="：存在key且对应value匹配
+ "!="：存在key但对应value不匹配或key单纯不存在
+ "=!="：必须存在key但对应value不匹配
+ "v-reg"：存在key且对应value匹配，此时参数3的value可含正则表达式
+ "!v-reg"：存在key但对应value不匹配，此时参数3的value可含正则表达式
+ "kv-reg"：存在key且对应value匹配，此时参数1的key、此时参数3的value皆可含正则表达式
+ "v-Aa_no_care"：存在key且对应value匹配，此时参数3的value可含正则表达式且不分大小写

示例：查询英语名称包含“Shimo-Kitazawa”（不清楚“k”的大小写是否正确）的铁道站（至少包含键为“train”的tag）：

```python
limit1.key_value("name:en", "v-Aa_no_care", "Shimo-Kitazawa").key_value("train", "exist")
```

其相当于QL中的：

```
[~"name:en"~"Shimo-Kitazawa",i]["train"]
```

### 2. 水母

### 3. 海染砗磲的全局限定

当你配置好了海染砗磲（QL语句）和水母（要素集），然后就是指定一些全局的要求，多是有关于海祇岛（Network）和锦囊范围的限定。

#### ① 设置延时

海染砗磲会设置一个延时，即Kokomi向珊瑚宫（Overpass）发送请求后珊瑚宫（Overpass）内部查询的等待时间，如果Kokomi在里面多转悠1秒，那么她会因为狠狠地超时而被珊瑚宫强制请离（Overpass返回超时信息），海染砗磲（QL语句）的延时默认为100（单位：秒），你可以通过timeout方法变更，此方法：
+ 参数1为【等待时间, str】：本次查询的最大等待时间，等待超过其+1s后只能得到超时信息，后续get_full_text方法会将时间写在最前面。

  返回OceanHuedClam：
+ 返回已经追加限制语句的OceanHuedClam。

该方法的使用与局部限定方法的使用大同小异，直接追加在海染砗磲后即可，不过需要在最终的、最核心的海染砗磲（QL语句）而不是靠前海染砗磲（QL语句）的进行中设定，注意查询的内容量越大，延时应该越长。

示例：前面已经写好了所有海染砗磲（QL语句），现设定延时为25：

```python
limit1.key_value("name:en", "v-Aa_no_care", "Shimo-Kitazawa").key_value("train", "exist").timeout("25")
```

#### ① 设置全局界定框

TODO

### 4. 生成完整的查询语句

处理完了前面的所有操作，最后请通过追加get_full_text方法取得API链接，其务必写在最后，此方法：

  返回str：
+ 该返回可直接作为API的查询语句，是其“interpreter?”后的部分，可作为Kokomi的query方法的参数。

示例：生成limit5的语句并交由Kokomi查询：

```python
waifu.query(limit5.get_full_text())
```
