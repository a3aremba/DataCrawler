# -*- coding: utf-8 -*-
import datetime
import time
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from core.webservices.GetCountry.AddressReferenceInterface import CAddressReferenceInterface

class Command(BaseCommand):
    help = 'example: python manage.py country_parser'
    
    def handle(self, *args, **options):
        CAddressReferenceInterface('RUS', 'False', 'False').sendParam()
        
        