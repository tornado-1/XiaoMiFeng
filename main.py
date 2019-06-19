# coding=utf-8
from flask import Flask, jsonify, request, render_template,redirect,url_for,flash,json
from forms import *
import datetime
#from login import login_page
# from login import login_page
# from ctl import ctl_page

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

conn=None

#login page
@app.route('/',methods=['GET'])
def login():
    lf=LoginForm()
    return render_template("login.html",form=lf)

@app.route('/',methods=['POST'])
def try_login():
    #检查登录信息
    if(True):
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))




@app.route('/index/',methods=['GET'])
def index():
    #这个界面直接显示图表信息
    #将图表保存为相应的格式，直接在前端的相关位置调用
    return render_template("index.html")


@app.route('/index/Practice/',methods=['GET'])
def Practice():
    calsInfo=[["1+1=?",2],["1+1=?",2]]
    cf=calProblemForm()
    return render_template("practice.html",cals=calsInfo,form=cf)


@app.route('/index/Exam/',methods=['GET','POST'])
def Exam():
    if (request.method == 'GET'):
        calsInfo=[["1+1=?",None,None,None],["1+1=?",None,None,None]]
        cf=calProblemForm()
    else:
        cf = calProblemForm()
        calsInfo = [["1+1=?",2 ,True, 2], ["1+1=?", 1,False, 2]]
    return render_template("exam.html", cals=calsInfo, form=cf)





if __name__ == '__main__':
    #conn = mysql.connector.connect(user='root', password='saki1208', database='trans', use_unicode=True)
    app.run(host="127.0.0.1",port=80)