[↑ 开始 · Kokomi基本内容](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/1%20-%20To%20start%20and%20invite%20Kokomi.md)
[↓ 海染砗磲 · 进阶联用与输出](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/3%20-%20More%20thing%20from%20multiple%20OceanHuedClams.md)

## Ⅲ 使用海染砗磲（QL语句）精确地查询

如果您对珊瑚宫（Overpass）的QL语句不是很熟悉，或者单纯嫌看着难受，请考虑给Kokomi整一个海染砗磲（QL语句）来方便地查询；当然，当需求比较复杂，可能需要不止一个。

### 1. 海染砗磲（QL语句）的概念

海染（音：hǎirǎn）砗磲（我猜你知道怎么读）在这里的概念大致是QL中的语句或集合。一个海染砗磲（QL语句）对象就是代表一条QL完整的语句（以及其随后的递归语句，如果有），QL语句的大致格式是：

```
type.set_A[k_v](extra_condition)->.set_B;>;
```

这些语句可以用来在珊瑚宫（Overpass）查询锦囊（要素），QL具体语法请参考[该Wiki页面](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL)。

在Python中，使用海染砗磲（QL语句）类的方法即可输出上述内容；当你想做限定时，先刷一个海染砗磲（QL语句）并指定前述QL语句格式中的「type」，其初始化方法中：
+ 参数1为【限定主体的类型，str】（"node"、"way"、"relation"、"nw"、"nr"、"wr"、"nwr"）：该海染砗磲（QL语句）对象是用来查询或者修饰何种类型的锦囊（要素），其中：
    + "node"：点；
    + "way"：线（一些闭合线段可视作区域）
    + "relation"：关系
    + "nw"：点和线
    + "nr"：点和关系
    + "wr"：线和关系
    + "nwr"：点、线和关系

  示例：同时查询node、way以及relation

```python
Q1 = OceanHuedClam("nwr")
```

然后，对要查询的内容做限定，海染砗磲（QL语句）类有如下一些方法，其中部分方法需要与其他海染砗磲（QL语句）对象一并使用，见后：

```python
· def key_value(self, key: str, relation: str, value: str = "") -> 'OceanHuedClam'
· def around(self, set_point: (str or list), r: int) -> 'OceanHuedClam'
· def id(self, directive_id: (int or str or list), id_opreation: str = "=") -> 'OceanHuedClam'
· def set_bbox(self, E: int, S: int, W: int, N: int) -> 'OceanHuedClam'
· def located_in(self, poly_list: list) -> 'OceanHuedClam'
# ----------
· def include_OceanHuedClam(self, set_name: str, the_set: 'OceanHuedClam') -> 'OceanHuedClam'
· def set_from(self, set_name: (str or list)) -> 'OceanHuedClam'
· def extend(self, direction: str, set_name: str = "_") -> 'OceanHuedClam'
...
```

### 2. 海染砗磲（QL语句）类使用方法链

你可能注意到，这些方法都返回新的海染砗磲对象，海染砗磲采用**方法链（method chaining）**模式，所以使用其的方法是直接将方法追加至现有的海染砗磲（QL语句）后，可以连续追加；这些方法内部也对self的内容进行了修改，所以你可以选择使用一个新的变量来承载追加方法后海染砗磲（QL语句），也可以不用，即下面的示例中limit1和limit2是等价的；此外，派森的赋值只大致算是赋地址，所以即使在limit1变化前将其赋给limit3，limit3在limit1变化后还是与limit1保持等价：

```python
limit1 = OceanHuedClam("nwr")
limit3 = limit1
limit2 = limit1.key_value("name", "v-reg", "foo").key_value("amd", "=", "yes")

if limit1 == limit2:
  print("这都能一样？")
if limit3 == limit1:
  print("不可能，绝对不可能")

print(limit1.convert())  # 再调用一个输出的方法试试看？
print(limit2.convert())
print(limit3.convert())
```

输出：

```
这都能一样？
不可能，绝对不可能
[data=[out:xml][timeout:100];(nwr["name"~"foo"]["amd"="yes"];);out body;]
[data=[out:xml][timeout:100];(nwr["name"~"foo"]["amd"="yes"];);out body;]
[data=[out:xml][timeout:100];(nwr["name"~"foo"]["amd"="yes"];);out body;]
```
### 3. 单纯的海染砗磲（QL语句）类方法
#### ① key_value方法

此方法用于限定查询主体的键值关系，其：
+ 参数1为【限定键，str】：限定必须出现或有对应值要求的键；
+ 参数2为【限制关系，str】（"exist"、"!exist"、"="、"!="、"=!="、"v-reg"、"!v-reg"、"kv-reg"、"v-Aa_no_care"）：限定键值之间的关系，其中：
    + "exist"：存在key，此时参数3可不填；
    + "!exist"：不存在key，此时参数3可不填；
    + "="：存在key且对应value匹配；
    + "!="：存在key但对应value不匹配或key单纯不存在；
    + "=!="：必须存在key但对应value不匹配；
    + "v-reg"：存在key且对应value匹配，此时参数3的value可含正则表达式；
    + "!v-reg"：存在key但对应value不匹配，此时参数3的value可含正则表达式；
    + "kv-reg"：存在key且对应value匹配，此时参数1的key、此时参数3的value皆可含正则表达式；
    + "v-Aa_no_care"：存在key且对应value匹配，此时参数3的value可含正则表达式且不分大小写。
+ 参数3为【限定值，str】：对限定键的值的要求；

  返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

  示例：查询英语名称包含“Shimo-Kitazawa”（不清楚“k”的大小写是否正确）的铁道站（至少包含键为“train”的tag）：

```python
limit1.key_value("name:en", "v-Aa_no_care", "Shimo-Kitazawa").key_value("train", "exist")
```

其相当于QL中的：

```
[~"name:en"~"Shimo-Kitazawa",i]["train"]
```

如果对同一个键做出了多次规定，则只保留最后一次规定，示例：

```python
limit1.key_value("name", "=", "天云峠").key_value("name", "=", "天云山上下")  #“天云峠”将被顶掉
```

其相当于QL中的：

```
["name"="天云山上下"]
```

#### ② around方法

此方法查询特定锦囊（要素）周边指定半径的内容。
+ 参数1为【中心锦囊（要素），str或list】：检索周边的圆心：
    + str：中心锦囊集（要素集）的名称，将检索其中各锦囊（要素）周边指定半径的内容；
    + list：由一串经纬度对组成的偶数项列表，形如[纬度1, 经度1, 纬度2, 经度2, ...]，表示各经纬度对组成的点构成的线段，将检索其周边指定半径的内容，其中：
        + 第2n-1项为float、int或str：第n个点的纬度；
        + 第2n项为float、int或str：第n个点的经度；
+ 参数2为【半径，int】：周边检索的半径，单位为米；

  返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

#### ③ id方法

此方法用于限定查询主体的id；id在珊瑚宫（Overpass）上是锦囊（要素）的唯一标识符，限制后该海染砗磲（QL语句）只会查询到特定id的锦囊（要素），所以追加其他限制无意义，本方法在限制"="id时不应也不能与其他方法连用；此方法：
+ 参数1为【锦囊（要素）id，int、str或list】：欲限定的id：
    + str：输入一个欲限定的id；
    + int：输入一个欲限定的id；
    + list：输入多个欲限定的id：
        + 每一项均为str或int：欲限定的id；
+ 参数2为【id关系，str】（"="、">"、"<"）：欲查询的id范围，默认为"="，其中；
    + "="：查询的锦囊（要素）的id必须与参数1的id相同；
    + ">"：查询的锦囊（要素）的id大于参数1的id，convert()输出QL语句时不会携带id限制，会通过self的flag位告知Kokomi收到报文后进一步筛选；
    + "<"：查询的锦囊（要素）的id小于参数1的id，convert()输出QL语句时不会携带id限制，会通过self的flag位告知Kokomi收到报文后进一步筛选；

  返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

  ℹ：当一个海染砗磲（QL语句）对象多次使用本方法可以指定多个id；

  ℹ：当一个海染砗磲（QL语句）对象多次使用本方法，传入的参数2有多种时，则Kokomi在query()时会分为多次查询；

  ℹ：如果参数1是列表，参数2的内容对列表各项均有效。

请注意：目前">"、"<"功能尚未实现（flag位还没做）。

  示例：查询id为114514的点：

```python
Q1 = OceanHuedClam("node").id(114514)
```

其相当于QL中的：

```
node(id:114514);
```

#### ④ set_bbox方法

此方法用于限定查询主体的位置，将会按经纬度构造一个界定框，锦囊（要素）不论是点、线、关系（包括其下的点、线），只要擦进了界定框就会被查询，此方法：
+ 参数1为【东至，str】：欲限定的界定框的东边界的十进制经度；
+ 参数2为【南至，str】：欲限定的界定框的南边界的十进制经度；
+ 参数3为【西至，str】：欲限定的界定框的西边界的十进制纬度；
+ 参数4为【北至，str】：欲限定的界定框的北边界的十进制纬度；

  返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

  示例：查询海埼一带的社区（palce=neighbourhood）：

```python
# 易得「海埼」在东经133.2983175，北纬35.5598934一带，经纬度稍微加减可构建附近一带的界定框
Q1 = OceanHuedClam("node").set_bbox(133.4, 35.3, 133.0, 35.8).key_value("place", "=", "neighbourhood")
```

其相当于QL中的：

```
node["place"="neighbourhood"](bbox:35.3,133.0,35.8,133.4);
```

#### ⑤ located_in方法

此方法与set_bbox方法类似，也用于限定查询主体的位置，但是是按照输入的内容构建一个闭合多边形，锦囊（要素）不论是点、线、关系（包括其下的点、线），只要擦进了该多边形就会被查询，此方法：
+ 参数1为【多边形点的经纬对，list】：欲构成多边形的点的十进制经纬度对的偶数项列表，其中：
    + 第2n-1项为float、int或str：第n个点的纬度；
    + 第2n项为float、int或str：第n个点的经度；

    返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

海染砗磲（QL语句）类的一些基本方法到此结束，已经可以满足相当一部分需求，如需查看如何输出，请移步后文[直接查询或生成QL语句](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/3%20-%20More%20thing%20from%20multiple%20OceanHuedClams.md#5-%E7%9B%B4%E6%8E%A5%E6%9F%A5%E8%AF%A2%E6%88%96%E7%94%9F%E6%88%90ql%E8%AF%AD%E5%8F%A5)。

[↑ 开始 · Kokomi基本内容](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/1%20-%20To%20start%20and%20invite%20Kokomi.md)
[↓ 海染砗磲 · 进阶联用与输出](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/3%20-%20More%20thing%20from%20multiple%20OceanHuedClams.md)
