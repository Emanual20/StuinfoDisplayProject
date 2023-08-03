# Server

后端部分，以`flask`为后端框架，便于轻量级部署；数据库使用了传统的`mysql`（妹有为什么）

## Quick Start

以development开发模式或以production生产模式运行：

```{python}
# development mode
python main.py --mode dev
# product mode
python main.py --mode production
```

## 组织架构

代码遵循以main.py为入口的组织架构，具体文件组织如下：

```
config
  - settings.py ··· 配置文件
utils
  - db ··· 和mysql交互
  - flask ··· flask启动
  - router ··· 路由配置
  - utils ··· 一些大多数文件会用到的模块
main.py ··· 入口
```