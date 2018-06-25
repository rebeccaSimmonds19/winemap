# How to Take Advantage of Microservice Architectures: Wine Map Use Case

This lab is intended to empower developers to create their own cloud native application and give them a look at microservice architectures. The application itself is made up of a database, an data processing application and a flask application server. The data is processed using an Apache Spark cluster (read more here:  deployed by the Oshinko webui (read more here https://radanalytics.io/get-started). The application will visulaise wine reviews on to a map so that traveling to countries with better wine is made easier. The microservices will be deployed onto an openshift cluster (read more here https://openshift.com), you will need to access this cluster by going to the following URL: <insert url>.

Before you can deploy the application we will need to create an Apache Spark cluster for processing the data as well as a database to hold the data we will process.

# Creating a Database and Loading the Data

## Step 1 Create a new project

On the right hand side of the console there will be a button to create a new project, click on this and name your new project “winemap”. After you have created the project click on the winemap link to enter it.


## Step 2. Deploy a database

In the console click the browse catalogue button and search for the postgresql database, click to make the new database. Click the next button this will show you the configuration page, here we will configure your database settings. In the configuration window make sure you enter the details show in the picture, do not worry about changing anything else. Click the create button and then close, you have deployed the first microservice a postgresql database.

## Step 3 Loading the Data

In the consol go to the right hand side and you will see an “add to project” button, click on this and choose the “from project” option. We are going to use a data loader template to run a one time job and load the data into the database. The job is a kubernetes job you can find out more about this at this link: http://kubernetesbyexample.com/jobs/
You then be presented with the window below, select the wine-data-loader and click the next button. Click the next button twice and then the create button to make the job (you do not need to enter a job name as a random name will be generated from the template.

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

