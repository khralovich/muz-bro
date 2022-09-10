import psycopg2
from sqlalchemy import create_engine
from config import RDS_ENDPOINT, RDS_USERNAME, RDS_PASSWORD, RDS_PORT, RDS_DB_NAME

sql_alchemy_db_url = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_ENDPOINT}/{RDS_DB_NAME}"
def create_connection():
    return psycopg2.connect(
        database=RDS_DB_NAME,
        user=RDS_USERNAME,
        password=RDS_PASSWORD,
        host=RDS_ENDPOINT,
        port=RDS_PORT
    )

def create_engine():
    engine = create_engine(sql_alchemy_db_url)
    return engine