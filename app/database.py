from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqllite:///./finance.db'

engine = create_engine(DATABASE_URL, connect_args={'check_some_th   read': False})

# autocommit - only we control any commit, autoflush - only we can send sql requests
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bing=engine)

Base = declarative_base()


