# scanner/__init__.py

from .sql_injection import sqlscanner
from .xss import xssVulnurable
from .weak_passwords import weakpasswords
from .deface import defacesite
from .dnsrecords import find_dns_records
from .fullscan import full_attack
from .generalinfo import gather_website_info
from .websitestresser import SocketStress
