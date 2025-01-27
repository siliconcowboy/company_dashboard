from sqlalchemy.orm import sessionmaker
from setup_database import engine, Company

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data
new_company = Company(
    name="Tech Innovators Inc.",
    geographic_location="San Francisco, CA",
    latest_funding_round="Series B",
    latest_funding_size=25.5,
    valuation=200.0,
    employees=150,
    industry="Technology",
    year_founded=2015,
    description="Develops cutting-edge AI solutions.",
    current_investors="Sequoia Capital, Andreessen Horowitz"
)

session.add(new_company)
session.commit()

print("Sample data added successfully!")
