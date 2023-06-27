### 3. 海染砗磲的全局限定

当你配置好了海染砗磲（QL语句）和水母（要素集），然后就是指定一些全局的要求，多是有关于海祇岛（Network）和锦囊范围的限定。

#### ① 设置延时

海染砗磲会设置一个延时，即Kokomi向珊瑚宫（Overpass）发送请求后珊瑚宫（Overpass）内部查询的等待时间，如果Kokomi在里面转悠到了101s，那么她会因为狠狠地超时而被珊瑚宫强制请离（Overpass返回超时信息），海染砗磲（QL语句）的延时默认为100（单位：秒），你可以通过timeout方法变更，此方法：
+ 参数1为【等待时间, str】：本次查询的最大等待时间，后续get_full_text方法会将时间写在最前面。

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
