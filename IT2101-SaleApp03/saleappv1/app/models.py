from sqlalchemy import Column, Integer, String,Float,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from app import db,app
class Category(db.Model):
    __tablename__="category"
    id= Column(Integer, primary_key=True,autoincrement=True)
    name= Column(String(50),nullable=True)
    products = relationship("Product", backref="category", lazy= True)
class Product(db.Model):
    id  = Column(Integer,primary_key=True, autoincrement=True)
    name= Column(String(50),nullable=True)
    price = Column(Float,default=0)
    image = Column(String(100),default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(Boolean,default=True)
    category_id= Column(Integer,ForeignKey(Category.id),nullable=False)
if __name__=="__main__":
    with app.app_context():
        """c1= Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Desktop")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()"""
        db.create_all()
        p1= Product(name="SamSung galaxy",price= 2000000,category_id= 1)
        p2 = Product(name="iPhone", price=2000000, category_id=1)
        p3 = Product(name="SamSung galaxy s23", price=2000000, category_id=1)
        p4 = Product(name="SamSung galaxy ultra", price=2000000, category_id=1)
        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()
        """ánkjdasdkasbkdbashkdb"""