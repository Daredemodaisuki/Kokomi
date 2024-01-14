# Kokomi

  一位用派森构造的贴心伙伴，可以提供较QL来说视觉稍友好的Overpass查询指令（但注意，其本质还是基于QL的）并且可以做一些轻量的查询工作，当然，Kokomi也可以作为QL生成帮手（不是）；最后，Kokomi不涉及数据更改（暂时？）。
  
  A python-based Overpass QL "translator" and Overpass querier.

## N 一些应用场景示例

+ 我想查询一些地名，做一个词库，方便调教输入法；
+ 我想看看某物大概在某地有多少，做个小统计；
+ 我只是单纯查个要素，但看QL很吃力，不想单独学QL或开JOSM了；
+ ……

## N+1 已知的问题 / TODO

+ <del>Kokomi手撸xml不能识别没有tag的节点；</del>
+ 潜在的append和extend错误使用问题；
+ OceanHuedClam需要flag_dict以便Kokomi在查询后于本地筛选；
+ 尚无法实现引用的OceanHuedClam中的多次查询需求。
