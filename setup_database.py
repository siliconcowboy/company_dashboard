from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database
DATABASE_URL = "sqlite:///companies.db"  # Change this if using PostgreSQL or another database
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Define the Company table
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    geographic_location = Column(String)
    latest_funding_round = Column(String)
    latest_funding_size = Column(Float)
    valuation = Column(Float)
    employees = Column(Integer)
    industry = Column(String)
    year_founded = Column(Integer)
    description = Column(Text)
    current_investors = Column(Text)

# Create the database
Base.metadata.create_all(engine)

print("Database and table created successfully!")
