"""
Defines the Person repository
"""

import csv
import requests
from contextlib import closing

from models import rdb
from config import args, logger
from flask import abort, g

from rethinkdb.errors import RqlRuntimeError, RqlDriverError

class DatasetRepository:
    """ The repository for the dataset model """

    # download and import the dataset in rethinkdb
    @staticmethod
    def create(url):
        """ Import a dataset from a download url """

        logger.info('Download dataset URL:"{0}"'.format(url))

        # check that dataset exists
        try:
            request_response = requests.head(url)
        except Exception as e:
            logger.error('Could not find: "{0}", response: {1}'.format(url, e))
            abort(500)

        # connect to the database
        try:
            g.rdb_conn = rdb.connect(host=args.rethinkdb_host, port=args.rethinkdb_port, db=args.rethinkdb_database)
        except RqlDriverError:
            abort(503, "Database connection could be established.")

        # proceed the online dataset line by line
        with closing(requests.get(url, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.DictReader(f)
            for data in reader:
                try:
                    rdb.table(args.rethinkdb_table).insert(data).run(g.rdb_conn)
                except RqlRuntimeError as e:
                    abort(503, f'Record cloud not be inserted. Message: {e}')