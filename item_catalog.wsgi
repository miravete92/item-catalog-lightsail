import sys
sys.path.insert(0, '/var/www/item-catalog')
from item_catalog import app as application
application.secret_key = 'super_secret_key'
