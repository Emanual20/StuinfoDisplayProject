# StuinfoDisplayProject

这是一个很像学生信息管理系统的毕业去向管理系统，只供内部使用。

### 技术栈

- Frontend：vue3+bootstrap
- Backend：flask
- Database：mysql+navicat(phpmyadmin of navicat)
- Server: AliCloud

### 目前支持什么

- 目前支持本地运行或挂载到服务器上（需要修改flask的端口配置，vue的mysql等配置文件）
- 用户登录、注册、修改密码，按照用户自己设定的权限展示个人毕业去向信息，修改他人查看权限，更新个人信息一些很基本的操作
- Get/Post数据均通过RSA256加密解密

### 目前不支持什么

- 用户友好的界面
- 压力测试，漏洞测试等爆破
- 其他我想不到的功能。
