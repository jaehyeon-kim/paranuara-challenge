import os
import time
import re
import psycopg2


def pytest_sessionstart(session):
    config = {
        "user": os.environ["POSTGRES_USER"],
        "password": os.environ["POSTGRES_PASSWORD"],
        "host": os.environ["POSTGRES_HOST"],
        "port": "5432",
        "dbname": os.environ["POSTGRES_DB"],
    }

    this_trial = 0
    while True:
        this_trial += 1
        try:
            psycopg2.connect(**config)
            break
        except Exception:
            pass
        if this_trial > 10:
            raise Exception("DB not available, config - {0}".format(config))
        time.sleep(1)
