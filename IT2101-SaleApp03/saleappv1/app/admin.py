from app.models import Category,Product,UserRoleEnum
from app import app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView,expose
from flask_login import logout_user,current_user
from flask import redirect
class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN
class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated
class MyProductView(AuthenticatedAdmin):
    column_list = ["id","name","price","image"]
    column_searchable_list = ["name"]
    column_filters = ["name","price"]
    column_editable_list = ["name","price"]
    edit_modal = True

class MyCategoryView(AuthenticatedAdmin):
    column_list = ["name","id","products"]
class StatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")
class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")

admin = Admin(app,name="Quản trị bán hàng",template_mode="bootstrap4")
admin.add_view(MyCategoryView(Category,db.session))
admin.add_view(MyProductView(Product,db.session))
admin.add_view((StatsView(name="Thống kê báo cáo")))
admin.add_view((LogoutView(name="Đăng xuất ")))
