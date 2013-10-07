'''
Created on Oct 6, 2013

@author: toantran
'''

from django.contrib import admin
from polls.models import Poll

admin.site.register(Poll)