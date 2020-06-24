# Setting Up SwipeCheck
This guide makes use of Pegasus (documentation [here](https://github.com/InsightDataScience/pegasus)). The .yml files necessary to set up each individual cluster are found in <path to project>/docs/pegasus. Make sure to input the subnet id, PEM keypair, and security group ids for your AWS account in each configuration file.

## Setting up Clusters
### Setting up Confluent
Run the command `bash <path to project>/src/bash_scripts/kafka_setup.sh` to set up kafka cluster.


After that is complete, you need to use the files list in this repository under <path to project>/docs/confluent and update the corresponding files on each Kafka node located in the following directories
* `~/confluent/etc/kafka/zookeeper.properties`
* `~/confluent/etc/kafka/server.properties`
* `~/confluent/etc/ksql/ksql-server.properties`

**Make sure to update any public DNS addresses or private IPs listed in these files to match the configuration of your servers**

**Also, make sure to move this repo file structure to the home path of each node in your Kafka cluster.**

### Setting up TimescaleDB(PostgreSQL)

Install Postgres with Timescale extension using this [link](https://docs.timescale.com/latest/getting-started/installation/ubuntu/installation-apt-ubuntu) then follow instructions in docs/postgres.txt

### Setting up Grafana

Install Grafana server using this [link](https://grafana.com/docs/grafana/latest/installation/debian/) then attach timescaledb datasource to grafana and create dashboard by attaching a query that you want to be fired evey 1s to get the tranasaction data
