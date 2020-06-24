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

Run bash_scripts/kafka_setup.sh and bash_scripts/timescaledb_setup.sh and follow the instructions in docs/setup.md to create required clusters, install and start technologies.

**DEMO**
![Credit Card Fraud Detection Demo](docs/demo/grafana-dashboard.gif)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
