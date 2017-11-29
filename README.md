# WineMapDatabase
Creates a postgresql container on OS and then loads wine review data from a data loader image as a job

oc cluster up

oc new-app \
    -p POSTGRESQL_USER=username \
    -p POSTGRESQL_PASSWORD=password \
    -p POSTGRESQL_DATABASE=wineDb\
    --template=postgresql-persistent
    
docker build . -t loader --build-arg server='postgresql' --build-arg user='username' --build-arg password='password' --build-arg dbname='wineDb'

docker tag loader 172.30.1.1:5000/myproject/loader

docker login -u $(oc whoami) -p $(oc whoami -t) 172.30.1.1:5000

docker push 172.30.1.1:5000/myproject/loader

oc create -f job.yaml
