# Running New-news
## Loading Kafka Services
Run the following commands on your local machine:
1. ```bash peg sshcmd-cluster kafka-cluster "nohup sudo ~/confluent/bin/zookeeper-server-start ~/confluent/etc/kafka/zookeeper.properties &> ~/confluent/logs/zookeeper.out&"```
2. ```bash peg sshcmd-cluster kafka-cluster "nohup sudo ~/confluent/bin/kafka-server-start ~/confluent/etc/kafka/server.properties &> ~/confluent/logs/kafka.out&"```
3. ```bash peg sshcmd-cluster kafka-cluster "nohup sudo ~/confluent/bin/ksql-server-start ~/confluent/etc/ksql/ksql-server.properties --queries-file ~/new-news/src/kafka/ksql/queries.sql &> ~/confluent/logs/ksql.out&"```
