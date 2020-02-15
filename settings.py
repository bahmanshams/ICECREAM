# icecream framework settings
import os

from dotenv import load_dotenv

project_directory = os.getcwd()
load_dotenv(os.path.join(project_directory, '.env'))

apps = [
    'app_book.urls.BookApp',
    'app_foo.urls.FOOApp',
]
default_address = {
    'host': os.getenv('host'),
    'port': os.getenv('port'),
}

database = {
    'db_user': os.getenv('db_user'),
    'db_pass': os.getenv('db_pass'),
    'db_host': os.getenv('db_host'),
    'db_port': os.getenv('db_port'),
    'db_name': os.getenv('db_name')
}
