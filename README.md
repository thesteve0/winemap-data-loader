# WineMapDatabase
Creates a postgresql container on OS and then loads wine review data from a data loader image as a job

oc cluster up

oc new-app \
    -p POSTGRESQL_USER=username \
    -p POSTGRESQL_PASSWORD=password \
    -p POSTGRESQL_DATABASE=wineDb\
    --template=postgresql-persistent
    
clone this repo

oc create -f wine-data-loader.yaml

oc new-app --template=wine-data-loader -p SERVER=postgresql -p PASSWORD=password -p USER=username -p DBNAME=wineDb
