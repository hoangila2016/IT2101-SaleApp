from sqlalchemy import Column, Integer, String,Float,Boolean,ForeignKey,Enum
from sqlalchemy.orm import relationship
from app import db,app
from flask_login import UserMixin
import enum
class UserRoleEnum(enum.Enum):
    USER=1
    ADMIN=2

class User(db.Model,UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50),unique=True,nullable=True)
    password= Column(String(50),nullable=True)
    user_role= Column(Enum(UserRoleEnum),default=UserRoleEnum.ADMIN)
class Category(db.Model):
    __tablename__="category"
    id= Column(Integer, primary_key=True,autoincrement=True)
    name= Column(String(50),nullable=True)
    products = relationship("Product", backref="category", lazy= True)
    def __str__(self):
        return self.name
class Product(db.Model):
    id  = Column(Integer,primary_key=True, autoincrement=True)
    name= Column(String(50),nullable=True)
    price = Column(Float,default=0)
    image = Column(String(255),default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(Boolean,default=True)
    category_id= Column(Integer,ForeignKey(Category.id),nullable=False)
    def __str__(self):
        return  self.name
if __name__=="__main__":
    with app.app_context():
        db.create_all()
        import hashlib
        # u= User(name="admin",username="admin",password=str(hashlib.md5("123".encode("utf-8")).hexdigest()))
        # db.session.add(u)
        # c1= Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Desktop")
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        #
        # p1= Product(name="tablet",price= 2000000,category_id= 3)
        # p2 = Product(name="tablet", price=2000000, category_id=3)
        # p3 = Product(name="tablet", price=2000000, category_id=3)
        # p4 = Product(name="tablet", price=2000000, category_id=3)
        # db.session.add_all([p1,p2,p3,p4])
        # db.session.commit()
        """ánkjdasdkasbkdbashkdb"""