import os

os.system('oc new-app https://github.com/rebeccaSimmonds19/WineMapDatabase.git \
--name database \
-e server=\'postgresql\' \
-e user=\'username\' \
-e password=\'password\' \
-e dbname=\'wineDb\'')
