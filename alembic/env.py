import sys
import os
from alembic import context
from sqlalchemy import pool
from logging.config import fileConfig
from sqlalchemy import engine_from_config

config = context.config
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from ICECREAM.db_initializer import Base, get_database_uri


def load_all(module_name):
    import os
    try:
        dircts = []
        path = os.getcwd()
        for root, dirs, files in os.walk(path):
            for file in files:
                script = '{}.py'.format(module_name)
                if file.endswith(script):
                    filepath = os.path.join(root, file)
                    if 'env' not in filepath:
                        dir_address = str(os.path.dirname(filepath))
                        dirname = dir_address.split('/')[-1]
                        if dirname != 'models':
                            dircts.append(dirname)

        for m in dircts:
            print(m)
            __import__('{}.{}'.format(m, module_name),
                       fromlist=['*'])
    except Exception as e:
        print(e)


target_metadata = Base.metadata

load_all('models')
config.set_main_option('sqlalchemy.url', get_database_uri())
fileConfig(config.config_file_name)


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
