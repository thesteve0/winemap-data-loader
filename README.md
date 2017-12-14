# winemap-data-loader
Creates a postgresql container on OS and then loads wine review data from a data loader image as a job


```sh
oc cluster up

oc new-app --template=postgresql-persistent -p POSTGRESQL_USER=username -p POSTGRESQL_PASSWORD=password -p POSTGRESQL_DATABASE=wineDb
```
    
clone this repo

```sh
oc create -f wine-data-loader.yaml

oc new-app --template=wine-data-loader -p SERVER=postgresql -p USER=username -p PASSWORD=password -p DBNAME=wineDb
```
