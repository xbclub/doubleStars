from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from config.config import db_user, db_dbname, db_host, db_passwd

engine = create_engine(
    "mysql+pymysql://" + db_user + ":" + db_passwd + "@" + db_host + ":3306/" + db_dbname + "?charset=utf8",
    encoding='utf-8',
    max_overflow=5)
Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)
