from sqlalchemy.orm import sessionmaker
from setup_database import engine, Company

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query all companies
companies = session.query(Company).all()

# Display results
for company in companies:
    print(f"Name: {company.name}, Industry: {company.industry}, Location: {company.geographic_location}")
