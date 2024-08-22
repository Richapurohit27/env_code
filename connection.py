from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# Replace 'sqlite:///your_database.db' with your actual database connection string
# For example, for a PostgreSQL database: 'postgresql://username:password@localhost:5432/your_database'
engine = create_engine('sqlite:///your_database.db')

# Create a metadata object
metadata = MetaData()

# Define a schema called "web_scrapes"
web_scrapes_schema = Table('web_scrapes', metadata,
    Column('id', Integer, primary_key=True),
    Column('date', String),  # Replace 'String' with the actual data type for date
    Column('location', String),
    Column('type', String),
    Column('value', Integer),
    schema='web_scrapes'
)

# Create the schema and table
metadata.create_all(engine)

# Example data to insert into the table
example_data = [
    {'date': '2023-01-01', 'location': 'Alabama', 'type': 'Land', 'value': 10},
    {'date': '2023-01-02', 'location': 'Alaska', 'type': 'Offshore', 'value': 15},
    # Add more data as needed
]

# Insert example data into the table
with engine.connect() as connection:
    for data_point in example_data:
        connection.execute(web_scrapes_schema.insert().values(data_point))
