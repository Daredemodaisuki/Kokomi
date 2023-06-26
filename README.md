# Kokomi
  A python-based Overpass querier.

## Ⅰ 开始
### 1.Kokomi暂时不需要其他的三方库，欲邀请Kokomi，请：

```python
from main import Kokomi
```
### 2.当然请不要忘记带上她心爱的OceanHuedClam：

```python
from main import OceanHuedClam
```

ℹ 这是现阶段的，后续合并了就只用 import Kokomi 了。

### 3.请给予Kokomi在你的文件中一个化身：

  示例：
```python
waifu = Kokomi()
```


## Ⅱ 请Kokomi查询
### 1.为她所在的Watatsumi（Network）指定Sangonomiya（Overpass）：
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

### 2.告诉她希望查询的内容：
  使用query函数可以请她帮帮忙，在前述指定的Sangonomiya寻找一些锦囊（OSM要素）数据，此函数：
+ 参数1为【查询指令，str】：在珊瑚宫（Overpass）查询的参数，以“data="后开始，默认为空，当然返回的报文也会告诉你不给东西查不到。

  返回int：
+ 【2】：向珊瑚宫成功地GET了报文；
+ 【-1】：珊瑚宫没有传回任何消息，可能是海祇岛（Network）连接原因；
+ 【-2】：珊瑚宫api未指定。
  如果你已经对各Sangonomiya的QL语句十分甚至九分熟悉，你可以直接写QL条件。
  
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
