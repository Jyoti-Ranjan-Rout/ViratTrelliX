from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Products
from database import Base , engine ,session , Product 
from sqlalchemy.orm import Session

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://virat-trelli-x-seven.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = session()
    try : 
        yield db 
    finally :
        db.close()


@app.get("/")
def greet():
    return "Welcome to @theviratvision018 Trac"

@app.get("/products")
def all_products(db : Session = Depends(get_db) ):
    products = db.query(Product).all()
    return products

@app.post("/products")
def add_product(product : Products , db : Session = Depends(get_db) ):
    new_product = Product(name=product.name,description=product.description,price=product.price,quantity=product.quantity)
    db.add(new_product)
    db.commit()
    return new_product

@app.get("/products/{id}")
def get_product_by_id(id:int,db : Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product : 
        return db_product
    return "No Data Found"

@app.put("/products/{id}")
def update_product(id : int , product : Products ,db : Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product is None :
        return "No Data to Update !"
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    return "Updated Successfully !"

@app.delete("/products/{id}")
def delete_product(id:int,db : Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product : 
        db.delete(db_product)
        db.commit()
        return "Data Deleted Successfully ! "
    else:
        return "No Data to Delete ! "
