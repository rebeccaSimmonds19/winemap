# How to Take Advantage of Microservice Architectures: Wine Map Use Case

This lab is intended to empower developers to create their own cloud native application and give them a look at microservice architectures. The application itself is made up of a database, an data processing application and a flask application server. The data is processed using an Apache Spark cluster (read more here:  deployed by the Oshinko webui (read more here https://radanalytics.io/get-started). The application will visulaise wine reviews on to a map so that traveling to countries with better wine is made easier. The microservices will be deployed onto an openshift cluster (read more here https://openshift.com), you will need to access this cluster by going to the following URL: <insert url>.

Before you can deploy the application we will need to create an Apache Spark cluster for processing the data as well as a database to hold the data we will process.

# Creating a Database and Loading data

# Creating an Apache Spark Cluster using Oshinko

# Deploying the Application

https://github.com/radanalyticsio/winemap-data-loader
 
This is the app that calls a postgresql db to show a map of wine reviews using these commands:


```sh
oc new-app --template=oshinko-python-spark-build-dc \
  -p APPLICATION_NAME=winemap \
  -p GIT_URI=https://github.com/radanalyticsio/winemap.git \
  -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4' \
  -p OSHINKO_CLUSTER_NAME=<oshinko_cluster_name> \
  -e SERVER=postgresql \
  -e DBNAME=wineDb \
  -e PASSWORD=password \
  -e USER=username
  ```

