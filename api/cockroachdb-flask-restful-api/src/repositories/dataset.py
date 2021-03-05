"""
Defines the Person repository
"""

import csv
import logging
import requests
from models import Person

logger = logging.getLogger('dataset')

class DatasetRepository:
    """ The repository for the dataset model """

    # download and import the dataset in cockroachdb
    @staticmethod
    def create(url):
        """ Import a dataset from a download url """

        logger.info('Download dataset URL:"{0}"'.format(url))

        # check that dataset exists
        try:
            request_response = requests.head(url)
        except Exception as e:
            logger.error('Could not find: "{0}", {1}'.format(url, request_response))
            abort(500)

        # proceed the online dataset line by line
        with closing(requests.get(url, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.DictReader(f)
            for data in reader:
                try:
                    person = Person(number=data['number'], gender=data['gender'], nameset=data['nameset'], title=data['title'], givenname=data['givenname'],
                                    middleinitial=data['middleinitial'], surname=data['surname'], streetaddress=data['streetaddress'], city=data['city'], state=data['state'],
                                    statefull=data['statefull'], zipcode=data['zipcode'], country=data['country'], countryfull=data['contryfull'], emailaddress=data['emailaddress'],
                                    username=data['username'], password=data['password'], browseruseragent=data['browseruseragent'], telephonenumber=data['telephonenumber'], telephonecountrycode=data['telephonecountrycode'],
                                    maidenname=data['maidenname'], birthday=data['birthday'], age=data['age'], tropicalzodiac=data['tropicalzodiac'], cctype=data['cctype'],
                                    ccnumber=data['ccnumber'], cvv2=data['ccv2'], ccexpires=data['ccexpires'], nationalid=data['nationalid'], upstracking=data['upstracking'],
                                    westernunionmtcn=data['westernunionmtcn'], moneygrammtcn=data['moneygrammtcn'], color=data['color'], occupation=data['occupation'], company=data['company'],
                                    vehicle=data['vehicle'], domain=data['domain'], bloodtype=data['bloodtype'], pounds=data['pounds'], kilograms=data['kilograms'],
                                    feetinches=data['feetinches'], centimeters=data['centimeters'], guid=data['guid'], latitude=data['latitude'], longitude=data['longitude']
                                    )
                except RqlRuntimeError:
                    abort(503, "Record cloud not be inserted.")
                return person.save()
