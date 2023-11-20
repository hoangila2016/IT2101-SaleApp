from flask import render_template, request,redirect
import dao
import math
from app import app,login
from flask_login import login_user
@app.route("/admin/login",methods=["post"])
def login_admin():
    username= request.form.get("username")
    password= request.form.get("password")
    user = dao.auth_user(username=username,password=password)
    if user:
        login_user(user)
    return redirect("/admin")

@app.route("/")
def index():

    kw = request.args.get('kw')
    cate_id= request.args.get("cate_id")
    page = request.args.get("page")

    cates = dao.get_categories()
    prods = dao.get_products(kw,cate_id,page)
    num= dao.count_products()
    page_size = app.config["PAGE_SIZE"]

    return render_template('index.html', categories=cates, products=prods
                           ,pages=math.ceil(num/page_size))
@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
