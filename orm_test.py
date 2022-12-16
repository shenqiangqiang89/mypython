'''
ORM
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,mapper
from sqlalchemy import Column,INTEGER,String,ForeignKey,MetaData,Table

mysql_conn_str = "mysql+pymysql://root:beta1234@localhost:3306/pythontest"
engine = create_engine(mysql_conn_str)

OrmBase = declarative_base()

metadata = MetaData()

''' 第一种创建表
class User(OrmBase):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key = True, autoincrement=True)
    user_name = Column(String(20))
    pass_word = Column(String(64))
'''
'''
第二针创建表
'''
user = Table('user', metadata,
             Column('id',INTEGER, primary_key = True, autoincrement=True),
             Column('user_name', String(20)),
             Column('full_name', String(40)),
             Column('full_name1', String(40)),
             Column('pass_word', String(64)))

class User(object):
    def __init__(self, user_name, full_name, full_name1, pass_word):
        self.use_rname = user_name
        self.full_name = full_name
        self.full_name1 = full_name1
        self.pass_word = pass_word

mapper(User, user) #User类和表user关联映射


class OrmManager(object):
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.__session = Session()
    '''
    第一种创建表
    '''
    def create_table(self):
        try:
            OrmBase.metadata.create_all(engine)
        except Exception as e:
            print(f"create_table has error with {e}")

    '''
        第二种创建表
        '''
    def create_table1(self):
        try:
            metadata.create_all(engine)
        except Exception as e:
            print(f"create_table has error with {e}")

    def add_records(self, objs):
        if isinstance(objs, list):
            self.__session.add_all(objs)
        else:
            self.__session.add(objs)
        self.__session.commit()

    def query_records(self, Cls):
        return self.__session.query(Cls).all()

orm = OrmManager()
#orm.create_table()
orm.create_table1()

#user = User(user_name = "admin",pass_word="admin")
#orm.add_records(user)

'''
query_user = orm.query_records(User)

for u in query_user:
    print(u.user_name,u.pass_word)
'''