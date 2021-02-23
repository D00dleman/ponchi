import os
from sys import platform

token = ""

time_to_commit_db = 30


directory_delimiter = "/" if platform != "win32" else "\\"
current_dir = directory_delimiter.join(
    os.path.realpath(__file__).split(directory_delimiter)[:-1]
)

db_settings = {
    'sqlite': dict(
        provider='sqlite',
        filename='{0}{1}test.db'.format(current_dir, directory_delimiter),
        create_db=True
    ),
    'mysql': dict(
        provider='mysql',
        user='user',
        password='1',
        host='localhost',
        database='test_db'
    )
}

db = db_settings['sqlite']
