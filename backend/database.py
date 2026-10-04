from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

DATABASE_URL = "sqlite:///./virat_trac.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String,nullable=False)
    description: Mapped[str] = mapped_column(String,nullable=False)
    price: Mapped[float] = mapped_column(Float,nullable=False)
    quantity: Mapped[int] = mapped_column(Integer,nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
 