import psycopg2
from config import RDS_ENDPOINT, RDS_USERNAME, RDS_PASSWORD, RDS_PORT

def create_connection(db_name: str = "musical-bot-db"):
    return psycopg2.connect(
        database=db_name,
        user=RDS_USERNAME,
        password=RDS_PASSWORD,
        host=RDS_ENDPOINT,
        port=RDS_PORT
    )
