from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# Create a metadata object
metadata_obj = MetaData()
# Create an engine object
engine = create_engine("sqlite:///category_app.db")
# Create a session factory
SessionFactory = sessionmaker(bind=engine)

# Create a table object
merchant_table = Table(
    "merchant_marketplace",
    metadata_obj,
    Column("merchant_id", Integer, primary_key=True),
    Column("merchant_name", String(30)),
    Column("email", String),
)
# Create a table object
product_table = Table(
    "products",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(30)),
    Column("description", String(300), nullable=True),
    Column("price", Integer),
    Column("merchant_id",ForeignKey("merchant_marketplace.merchant_id"), Integer),
)
# Create the table in the database
with SessionFactory() as session:
    session.execute("PRAGMA foreign_keys=ON")
    metadata_obj.create_all(engine)
    session.commit()


class Base(DeclarativeBase):
    pass
# Create a class for the merchant table
class Merchant(Base):
    __tablename__ = "merchant_marketplace"
    merchant_id: Mapped[int] = mapped_column(primary_key=True)
    merchant_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String)
    products: Mapped[List["Product"]] = relationship(back_populates="merchant")
    def __repr__(self) -> str:
        return f"Merchant(merchant_id={self.merchant_id!r}, merchant_name={self.merchant_name!r}, email={self.email!r})"
# Create a class for the product table
class Product(Base):
    __tablename__ = "products"
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(300))
    price: Mapped[int] = mapped_column(Integer)
    merchant_id: Mapped[int] = mapped_column(ForeignKey("merchant_marketplace.merchant_id"))
    merchant: Mapped[Merchant] = relationship(back_populates="products")
    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, product_name={self.product_name!r}, description={self.description!r}, price={self.price!r}, merchant_id={self.merchant_id!r})"

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
session = SessionFactory()
