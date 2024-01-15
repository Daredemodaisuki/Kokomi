[↑ 海染砗磲 · 查询语句基础](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/2%20-%20QL%20with%20OceanHuedClam.md)

### 4. 多个海染砗磲（QL语句）联用

当查询需求比较复杂，则需要多个海染砗磲（QL语句）对象共同构成一个查询语句组，如从符合某一个海染砗磲（QL语句）的锦囊（要素）中筛选符合另一海染砗磲（QL语句）的锦囊（要素）。

在一个海染砗磲（QL语句）对象使用另一个海染砗磲（QL语句）对象，需要通过include_OceanHuedClam方法先引用，此方法：
+ 参数1为【新对象命名，str】：新对象在本海染砗磲（QL语句）的名称，应当是唯一的；
+ 参数2为【新对象，OceanHuedClam】：新的需要使用的海染砗磲（QL语句）对象本身；

    返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

  示例：在已有海染砗磲（QL语句）对象Q1、Q2的情况下，Q2希望引用Q1
```python
Q2.include_OceanHuedClam("Q1", Q1)
```

请注意：任何需要使用其他海染砗磲（QL语句）对象的海染砗磲（QL语句）必须先引用后使用，此是目前海染砗磲（QL语句）对方法链调用顺序的唯一要求。

#### ① set_from方法

此方法用于限制本海染砗磲（QL语句）对象的其他限制的适用对象，即从指定的海染砗磲（QL语句）中提取符合本海染砗磲（QL语句）对象要求的锦囊（要素），此方法：
+ 参数1为【对象海染砗磲（QL语句）命名，str或list】：指定的海染砗磲（QL语句）：
    + str：或查询（并集）：单次使用本方法时输入一个海染砗磲（QL语句）的命名，通过连续使用数次本方法达到从多个海染砗磲（QL语句）的并集提取；
    + list：和查询（交集）：由数个海染砗磲（QL语句）命名组成的列表，列表内的海染砗磲（QL语句）需要同时满足，即从它们的交集提取；输入的列表与其他使用本方法输入的海染砗磲（QL语句）呈并集；其中：
      + 每一项均为str：需要同时满足的海染砗磲（QL语句）命名；

    返回OceanHuedClam：
+ 如果成功，则返回已经追加限制语句的OceanHuedClam；否则原样不动地返回。

  示例：海染砗磲（QL语句）对象Q1表示名称中包含「郁」字的node，Q2希望在Q1中筛选出铁路相关的要素

```python
Q1 = OceanHuedClam("nwr")\
    .key_value("name", "v-reg", "郁")  # 限制nwr["name"~"郁"]
Q2 = OceanHuedClam("node")\
    .include_OceanHuedClam("a", Q1).set_from("a")\  # 引用集合Q1，命名为「a」，指定Q2要从Q1中提取
    .key_value("railway", "exist")  #设定为在Q2中检索限制语句nwr["railway"]
```

其相当于QL中的：

```
nwr["name"~"郁"]->.a;node.a["railway"]
```

#### ② extend方法

此方法用于递归查询，比如Kokomi找到了一个锦囊（要素）点，它在一条线上，你希望揪出那条线，当然，顺着线可能可以找到它所在的关系，等等等等，这叫递归，此方法：

#### ③ 递归查询

#### ③ 逐个查询

### 5. 直接查询或生成QL语句

处理完了前面的所有操作，最后请将最终的海染砗磲（QL语句）对象装备给Kokomi，如前文所述使用Kokomi的query方法查询：

  示例：将前文提到的查询名称为「粮站院内」（name=粮站院内）的锦囊（要素）node使用海染砗磲（QL语句）对象写出来并查询

```python
waifu = Kokomi()
waifu.Watatsumi_set("OGF")
Q1 = OceanHuedClam("nwr")\
    .key_value("name", "=", "粮站院内")

waifu.query(Q1)
```

您也可以通过追加convert方法取得QL语句，此方法：
+ 参数1-3存在，但应仅供内部使用；

  返回list，包含所有需要查询的QL语句，其中：
    + 每一项均为str：一个QL语句；

  ℹ：一般地，此方法返回的list应该只包含一个元素，但当使用前面的方法时遇到需要Kokomi分次查询的情况，此处会有多个元素。

  示例：

```python
result = OceanHuedClam("nwr").key_value("name", "=", "粮站院内").convert()
```

  得到:

```python
['nwr["name"="粮站院内"];']
```

[↑ 海染砗磲 · 查询语句基础](https://github.com/Daredemodaisuki/Kokomi/blob/main/docs/2%20-%20QL%20with%20OceanHuedClam.md)
