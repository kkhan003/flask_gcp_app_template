# Flask + Google Cloud SQL Example (Simplified)
import os

SECRET_KEY = os.urandom (256)
SQLALCHEMY_TRACK_MODIFICATIONS = False


# GCP
CLOUDSQL_USER = 'postgres'
CLOUDSQL_PASSWORD = '1234'
CLOUDSQL_DATABASE = 'apptemp'
CLOUDSQL_CONNECTION_NAME = 'ifrs16project:asia-south1:leasedb'
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'postgres+pg8000://{nam}:{pas}@127.0.0.1:5432/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

LIVE_SQLALCHEMY_DATABASE_URI = (
    'postgres+pg8000://{nam}:{pas}@/{dbn}?unix_sock=/cloudsql/{con}/.s.PGSQL.5432').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)


if os.environ.get ('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

    # # postgres+pg8000://<db_user>:<db_pass>@/<db_name>?unix_sock=/cloudsql/<cloud_sql_instance_name>/.s.PGSQL.5432
    # sqlalchemy.engine.url.URL(
    #     drivername='postgres+pg8000',
    #     username=db_user,
    #     password=db_pass,
    #     database=db_name,
    #     query={
    #         'unix_sock': '/cloudsql/{}/.s.PGSQL.5432'.format(
    #             cloud_sql_connection_name)



# Override to SQLITE (for testing ...)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'