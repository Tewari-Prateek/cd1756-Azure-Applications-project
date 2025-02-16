import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacity1234'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or 'JLu+MG14lMbqmg04AsKARcl5XyQtmAWlXY3hbIntUImgKRozP8T+AAShzD227Uy01AcSSJNfLX0l+AStXQKMQw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'udacity1234.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '@Udacitypass'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + \
        SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + \
        SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "N4g8Q~taW.~0li1fowCeLhf1neD6Ip2yflVPidbi"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "dc76ddea-cb48-4630-af23-b50ab28c93d2"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/getAToken"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    # Only need to read user profile for this app
    SCOPE = ["User.ReadBasic.All"]

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
