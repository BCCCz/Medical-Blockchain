## GO Team后端

框架：Django 2.2　

前提：需要提前部署WEBASE，并部署Medical合约　

参考资料：https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Install/index.html

一键部署即可，暂时只需要前三个子系统

```python
python manage.py runserver #默认端口8000
```

注意：前后端不分离，前端页面看到的效果都是由后端控制，由后端渲染页面或重定向，后端需要控制前端的展示，前端与后端的耦合度很高。
会让后期的工作量有所增加．

主页：　http://localhost:8000/homepge

重要文件
- page
一些网页的跳转，整个web的逻辑

- accout
实现登录，未开放注册和修改密码（需要admin用户去总览平台进行添加或修改）

- information
用合约给的五个接口发送交易

- templates
一些基础的html，因为前后端没分离所以测试使用

前端的设计可以参考网信年鉴里面的优秀作品进行设计,有问题及时讨论

大多数的东西还没有加上去，功能也不完善，后期一步步来

