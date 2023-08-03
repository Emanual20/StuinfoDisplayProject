#  VUE3.0: 从后端读取数据，展示页面

## axios : 让vue从后端读取数据

## 我踩过的一些坑

> 问题1：只有主页home可以显示，路由到其他页面浏览器控制台报错 Uncaught SyntaxError: Unexpected token ‘＜‘ (at chunk-vendors.js:1:1) app.j
> 这是因为在build时候把vue.config.js中 module.exports = { publicPath: "/", ... } 的 publicPath改成了 "./" ，这个改动主要是为了在生产环境build时候解决路径问题，注意这里如果在开发环境下 "npm run serve" 的时候需要再改回来。

> 问题2：本地navicat访问不到服务器mysql的3306端口，非常难搞。
> 这是因为mysql初始生成的root虽然是最高权限但是为了安全考虑，只有内网访问权限。

可以进入服务器mysql后使用下面代码把mysql表里的root记录修改一下，开放全域访问权限。

```
mysql -u root -p <your mysql password>
mysql> use mysql; 
mysql> update user set host = '%' where user = 'root'; 
mysql> select host, user from user; 
mysql> flush privileges;
```

> 问题3 宝塔的pm2运行flask后端脚本的时候，无法正常加入虚拟环境导致找不到flask，pymysql之类的包，而这些包都是安装在某个虚拟环境里的。
> 那就直接ssh连接一下，在命令行里让pm2运行脚本即可。

``` 
可以通过pm2 start <program name>来启动某个js脚本或python程序，之后就能看到这个进程的监听状态；
可以通过pm2 log来查看正在运行的进程所有log；
```

> 问题4 宝塔的nginx因为80端口冲突无法启动，用netstat查看占用端口之后发现是被系统进程system占用
> 我总不能kill系统进程吧，查看占用80端口的详细信息后发现是Alibaba Apache Cloud服务占用，那就是阿里云初始化时候配套自带的Apache服务了，那就没办法，直接卸载nginx...

> 问题5 Apache报错AH00526: Syntax error on line 4 of /etc/httpd/...: Systemd socket activation is used, but this port is not configured in systemd
> 这是因为我搞了虚拟端口，我想让一个apache服务器的多个端口，每个端口对应一个虚拟根目录，达到在一台服务器同时运行多个服务的功能。按照一些博客的做法，我们需要先在httpd.conf里面listen要开启的端口，然后再在httpd/conf.d/...目录下建立一些配置对应虚拟端口的文件。但是还需要让这个端口也在systemd里注册一下，也就是报错信息所讲到的"this port is not configured in systemd"。
> 一些可以参考的链接：[链接1](https://www.digitalocean.com/community/tutorials/apache-configuration-error-ah00558-could-not-reliably-determine-the-server-s-fully-qualified-domain-name) [链接2](https://serverfault.com/questions/1033563/systemd-socket-activation-for-multiple-ports-on-apache)
> 最终我是大概读懂了链接1里面的原理，参考链接2其中一部分做法解决的，通过systemctl edit httpd.socket编辑一下这个文件，如果没有的话我们就模仿/usr/lib/systemd/system/httpd.socket.d/路径下的10-listen443.conf对照重新写一个对应自己端口的配置文件。然后注意修改完配置文件之后要重启apache服务，systemctl restart httpd，或者用service也可以。