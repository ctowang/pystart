# coding:utf-8
from flask import Flask,request,render_template
#引入路由
from ws.qxsp import qx
from ws.test.test import test
from ws.shell.ip import ip
app=Flask(__name__)

#注册蓝图
app.register_blueprint(qx,url_prefix='/')
app.register_blueprint(test,url_prefix='/py')
app.register_blueprint(ip,url_prefix='/linux')

#启动服务
if __name__ == '__main__':
    app.run(
      host='192.168.213.30',
      port= 28021,
      debug=True
    )
