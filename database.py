from sqlalchemy import create_engine

# ideally should be in .env
postgres_url = "postgresql+psycopg2://dhruv:admin@127.0.0.1:5432/natlov"


engine = create_engine(postgres_url)
