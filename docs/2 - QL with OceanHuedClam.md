[↑ 开始 · Kokomi基本内容](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/1%20-%20To%20start%20and%20invite%20Kokomi.md)
[↓ 海染砗磲 · 使用与输出](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/3%20-%20More%20thing%20from%20multiple%20OceanHuedClams.md)

## Ⅲ 海染砗磲（QL语句）

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

ℹ：如果确实需要，请善用deepcopy()。

### 3. 海染砗磲（QL语句）类方法调用顺序

根据作者瞪眼与总结，海染砗磲（QL语句）类提供的方法按照下列QL语句的格式：

```
① type.set_A(other_conditionL)[k_v](other_conditionR)->.set_B;
② type.set_A(other_conditionL)[k_v](other_conditionR)->.set_B;(movable_condition);
③ type.(unique_condition)->.set_B;(movable_condition);
④ type.(unique_condition)->.set_B;

或

QL语句 → <不可变位置限制> | <不可变位置限制><可变位置限制> | <独立限制><可变位置限制> | <独立限制>
```

大致可以分为可变位置（movable）、不可变位置（normal）、独立（unique）方法三类：

+ 不可变位置方法：即涉及「type」「.set_A」「(other_conditionL)」「[k_v]」「(other_conditionR)」等限制的内容，这些内容是基本QL语句的要素，在QL语句中位置相对固定。在使用海染砗磲（QL语句）类方法时，连续追加的不可变位置方法之间先后顺序不影响最终输出，即可以随时添加；
+ 可变位置方法：即涉及「(movable_condition)」相关内容，这些内容在QL语句中与不可变位置内容的相对位置可变，随位置不同输出结果不同。在使用海染砗磲（QL语句）类方法时，这些方法会切割连续的不可变位置方法，且可变位置方法追加的位置会影响最终结果。
+ 独立方法：即涉及「(unique_condition)」相关内容，它们在QL语句中单独使用；在使用海染砗磲（QL语句）类方法时，一般地，一个海染砗磲（QL语句）对象应该只有1个独立方法，其后可以适当追加可变位置方法。

  示例：Q1、Q2之间可变位置方法位置不同；Q2、Q3之间可变位置方法位置相同，但连续的不可变位置方法之间相对位置不同
```
Q1 = OceanHuedClam("node").set_bbox(7.3, 50.6, 7.0, 50.8).extend("<", "_").key_value("name", "exist")
Q2 = OceanHuedClam("node").set_bbox(7.3, 50.6, 7.0, 50.8).key_value("name", "exist").extend("<", "_")
Q3 = OceanHuedClam("node").key_value("name", "exist").set_bbox(7.3, 50.6, 7.0, 50.8).extend("<", "_")

for x in [Q1, Q2, Q3]:
    print(x.convert_new())
```

得到：

```
['node(bbox:50.6,7.0,50.8,7.3);<->.temp-778;node.temp-778["name"];']
['node["name"](bbox:50.6,7.0,50.8,7.3);<;']
['node["name"](bbox:50.6,7.0,50.8,7.3);<;']
```

上面提及的方法的具体用法将会在下一篇讲述。

[↑ 开始 · Kokomi基本内容](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/1%20-%20To%20start%20and%20invite%20Kokomi.md)
[↓ 海染砗磲 · 使用与输出](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/3%20-%20More%20thing%20from%20multiple%20OceanHuedClams.md)
