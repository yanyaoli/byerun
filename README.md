<h1 align='center'>
  Unirun Helper | 校园跑助手
</h1>

<p align='center'>
 校园跑辅助工具，为了你的健康，不提倡长期使用
</p>

<div align='center'>
  <img src="./files/logo.png" width=100px height=100px>
</div>


## 介绍说明

UNIRUN校园跑辅助工具，自动规划跑步路径，提交跑步记录，跑步里程与时长已设置阈值，安全可靠，但不排除学校存在其他检测方法，如使用本工具造成的任何问题请自行承担。

![intro](./files/intro.jpg)


| 地图支持                    |
| --------------------------- |
| 成都信息工程大学（航空港校区） |
| 成都信息工程大学（龙泉校区） |
| 成都中医药大学（温江校区） |
| ...                         |


## 地图贡献

**欢迎贡献地图文件**

**地图格式示例**

> 坐标路径建议前后连贯

> 结尾坐标值建议在开始坐标值附近或者与开始坐标值相同。

> 结尾坐标的edge值需要设置为```0```

```python
def MapName():
  mapdata =  [
    {
      "id": 0,　#唯一标识符
      "location": "103.9857179,30.5809638", #地理坐标
      "edge": [1] #路径排序
    },
    {
      "id": 1,
      "location": "103.985738,30.5809205",
      "edge": [2]
    },
    {
      "id": 2,
      "location": "103.9857497,30.5808788",
      "edge": [3]
    },
    {
      "id": 3,
      "location": "103.9857475,30.5808847",
      "edge": [0] #最后路径排序值需设置为0
    }
]
```

**坐标拾取**

[高德地图](https://lbs.gaode.com/console/show/picker) 

[高德地图](https://lbs.amap.com/tools/picker)


## TODO

- [ ] 多用户管理
- [ ] 多用户任务
- [ ] 更多地图


## 使用指南

### 直接使用打包好的程序

进入[发布页面](https://github.com/yanyaoli/unirun/releases/)，下载最新发布的可执行程序


### 本地构建

**项目下载**

> 下载`zip` 压缩包解压至文件夹 或 通过 `git clone`

```shell
cd unirun
git clone https://github.com/yanyaoli/unirun.git
```

**依赖安装**

```shell
pip install -r requirements.txt
```

**开始使用**

```shell
python unirun.py
```


## 特别鸣谢

<p align='center'>
  <a href="https://github.com/yanyaoli/unirun/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=yanyaoli/unirun">
  </a>
</p>