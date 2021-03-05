"""
Define person model
"""
from . import db
from .abc import BaseModel, MetaBaseModel

class Person(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Person model """

    __tablename__ = "person"

    number = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(6), nullable=False)
    nameset = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(6), nullable=False)
    givenname = db.Column(db.String(20), nullable=False)
    middleinitial = db.Column(db.String(1), nullable=False)
    surname = db.Column(db.String(23), nullable=False)
    streetaddress = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(22), nullable=False)
    statefull = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    countryfull = db.Column(db.String(100), nullable=False)
    emailaddress = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    browseruseragent = db.Column(db.String(255), nullable=False)
    telephonenumber = db.Column(db.String(25), nullable=False)
    telephonecountrycode = db.Column(db.Integer, nullable=False)
    maidenname = db.Column(db.String(23), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    tropicalzodiac = db.Column(db.Integer, nullable=False)
    cctype = db.Column(db.String(10), nullable=False)
    ccnumber = db.Column(db.String(16), nullable=False)
    cvv2 = db.Column(db.String(3), nullable=False)
    ccexpires = db.Column(db.String(10), nullable=False)
    nationalid = db.Column(db.String(20), nullable=False)
    upstracking = db.Column(db.String(24), nullable=False)
    westernunionmtcn = db.Column(db.String(10), nullable=False)
    moneygrammtcn = db.Column(db.String(8), nullable=False)
    color = db.Column(db.String(6), nullable=False)
    occupation = db.Column(db.String(70), nullable=False)
    company = db.Column(db.String(70), nullable=False)
    vehicle = db.Column(db.String(255), nullable=False)
    domain = db.Column(db.String(70), nullable=False)
    bloodtype = db.Column(db.String(3), nullable=False)
    pounds = db.Column(db.Numeric(5,1), nullable=False)
    kilograms = db.Column(db.Numeric(5,1), nullable=False)
    feetinches = db.Column(db.String(6), nullable=False)
    centimeters = db.Column(db.Integer, nullable=False)
    guid = db.Column(db.String(36), nullable=False)
    latitude = db.Column(db.Numeric(10,8), nullable=False)
    longitude = db.Column(db.Numeric(11,8), nullable=False)

    def __ini__(self,
                number, gender, nameset, title, givenname,
                middleinitial, surname, streetaddress, city, state,
                statefull, zipcode, country, countryfull, emailaddress,
                username, password, browseruseragent, telephonenumber, telephonecountrycode,
                maidenname, birthday, age, tropicalzodiac, cctype,
                ccnumber, cvv2, ccexpires, nationalid, upstracking,
                westernunionmtcn, moneygrammtcn, color, occupation, company,
                vehicle, domain, bloodtype, pounds, kilograms,
                feetinches, centimeters, guid, latitude, longitude
                ):
        """ Create a new person """
        self.number = number
        self.gender = gender
        self.nameset = nameset
        self.title = title
        self.givenname = givenname
        self.middleinitial = middleinitial
        self.surname = surname
        self.streetaddress = streetaddress
        self.city = city
        self.state = state
        self.statefull = statefull
        self.zipcode = zipcode
        self.country = country
        self.countryfull = countryfull
        self.emailaddress = emailaddress
        self.username = username
        self.password = password
        self.browseruseragent = browseruseragent
        self.telephonenumber = telephonenumber
        self.telephonecountrycode = telephonecountrycode
        self.maidenname = maidenname
        self.birthday = birthday
        self.age = age
        self.tropicalzodiac = tropicalzodiac
        self.cctype = cctype
        self.ccnumber = ccnumber
        self.cvv2 = cvv2
        self.ccexpires = ccexpires
        self.nationalid = nationalid
        self.upstracking = upstracking
        self.westernunionmtcn = westernunionmtcn
        self.moneygrammtcn = moneygrammtcn
        self.color = color
        self.occupation = occupation
        self.vehicle = vehicle
        self.domain = domain
        self.bloodtype = bloodtype
        self.pounds = pounds
        self.kilograms = kilograms
        self.feetinches = feetinches
        self.centimeters = centimeters
        self.guid = guid
        self.latitude = latitude
        self.longitude = longitude
