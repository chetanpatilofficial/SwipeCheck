# SwipeCheck

**A Platform for Real-time anomaly detection in Credit Card Transactions**

**Chetan Patil - Insight Data Engineering (New York - Summer 2020)**

The goal of this project is to identify suspicious credit card transactions by comparing user and transaction location data in realtime and sending alert to user if the user is more than 8 km away in last 10 minutes.

**Approach**

To simulate user location and transaction location data. A kafka producer is streaming the data at rate of 30000 messages/sec. the two stream (user and location) are joined with in 10 minute window and further calculte the distance between the user location and transaction location and if the user location more than 8 km away from transaction location we will alert the user.


**Architecure**
  ![GitHub Logo](/docs/architecture.png)


**Instructions**

Pegasus is a tool that allows you to quickly deploy a number of distributed technologies.

Install and configure [AWS CLI](https://aws.amazon.com/cli/) and [Pegasus](https://github.com/InsightDataScience/pegasus) on your local machine, and clone this repository using 'https://github.com/chetanpatilofficial/SwipeCheck.git'

**SET UP CLUSTER**

(3 nodes) Kafka-Cluster , instance type: m4.large <br>
(1 node) PostgreSQL(Timescale) and Grafana , instance type: m5.2xlarge

Follow the instructions in docs/pegasus.txt to create required clusters, install and start technologies

Install Postgres with Timescale extension using this [link](https://docs.timescale.com/latest/getting-started/installation/ubuntu/installation-apt-ubuntu) then follow instructions in docs/postgres.txt
