# My Web Framework

## 安装依赖

`pip install waitress httpie`

## 执行DEMO

1. 打开终端，进入项目目录（即包含本README文件的目录）
2. 执行命令 `python app.py` 启动HTTP服务器
3. 保持HTTP服务运行，另外打开一个终端，执行

   ```shell
   python -m httpie http://127.0.0.1:18080/order item=cup username=abcd quantity:=13
   ```

   测试服务器。应该可以看到类似如下的输出：

   ```text
   HTTP/1.1 200 OK
   Content-Length: 2
   Content-Type: application/json
   Date: Sun, 05 Dec 2021 07:04:09 GMT
   Server: waitress

   OK
   ```

## 代码结构

* `app.py`为应用侧代码，即使用My Web Framework的业务开发者需要实现的代码；
* 其余为框架代码。
