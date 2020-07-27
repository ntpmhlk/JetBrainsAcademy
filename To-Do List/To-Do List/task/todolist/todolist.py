from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# get DeclarativeMeta class to use as parent class
Base = declarative_base()


# create a model class that describes the table in the database
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __str__(self):
        return f'id={self.id}, task={self.task}, deadline={self.deadline}'


# create database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
# create described table in database
Base.metadata.create_all(engine)

# create session to use for access the database
Session = sessionmaker(bind=engine)
session = Session()


def show_command():
    commands = ["Today's tasks", 'Add task', 'Exit']
    for i in range(len(commands) - 1):
        print(f'{i + 1}) {commands[i]}')
    print(f'0) {commands[-1]}')


def show_task():
    rows = session.query(Table).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        print('Today:')
        for i in range(len(rows)):
            print(f'{i + 1}. {rows[i].task}')


def add_task():
    print('Enter task')
    task = input()
    new_row = Table(task=task, deadline=datetime.today())
    session.add(new_row)
    session.commit()
    print('The task has been added!')


def delete_task():
    pass


while True:
    show_command()
    user_input = input()
    print()
    if user_input == '0':
        print('Bye!')
        break
    elif user_input == '1':
        show_task()
    elif user_input == '2':
        add_task()
    else:
        print('Invalid input.')
    print()
