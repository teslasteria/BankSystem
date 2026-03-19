from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///./finance.db'

# For SQLite, disable check_same_thread so the connection can be used in different threads
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

# autocommit - only we control any commit, autoflush - only we can send sql requests
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

