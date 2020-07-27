from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# get DeclarativeMeta class to use as parent class
Base = declarative_base()


# create a model class that describes the table in the database
class Table(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


# create database file
engine = create_engine('sqlite:///file_name?check_same_thread=False')
# create described table in database
Base.metadata.create_all(engine)

# create session to use for access the database
Session = sessionmaker(bind=engine)
session = Session()

# create object and add it as new row in table
new_row = Table(string_field='This is string field',
                date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()

# get all rows from table as Python list
rows = session.query(Table).all()

# access the row fields
first_row = rows[0]
print(first_row.string_field)
print(first_row.id)
print(first_row)