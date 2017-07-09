Linux Server Configuration Project
==================================

Author
------
Alberto Miravete Arrufat

IP Address and Port
-------------------
IP: 52.56.77.58
Port: 2200

Application URL
---------------
[http://52.56.77.58](http://52.56.77.58)

Software Installed
------------------
### Apache2 server (Version 2.4.18)
Modified */etc/apache2/sites-avilable/000-default.conf* as follows:

<VirtualHost *>
    ServerName example.com

    WSGIDaemonProcess item-catalog user=catalog group=catalog threads=5 home=/var/www/item-catalog
    WSGIScriptAlias / /var/www/item-catalog/item_catalog.wsgi

    <Directory /var/www/item-catalog>
        WSGIProcessGroup item-catalog
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>


### Postgresql (Version 9.5.7)

created user catalog
created database catalog for this user

### python 2.7 and pip
Installed *sqlalchemy, flask, psycopg2, httplib2, oauth2client, requests* modules logged in as catalog user


Note
---------------------
Google Oauth client does not allow public IPs for redirecting URLs, so Google authentication is not working. 
Instead you can use Facebook authentication.
