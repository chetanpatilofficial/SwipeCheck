#!/bin/bash
#!/bin/bash
ROOT=$(dirname ${BASH_SOURCE})/../..

CLUSTER_NAME=kafka-cluster

# starting instances
peg up ${ROOT}/docs/config/pegasus/kafka/master.yml &
peg up ${ROOT}/docs/config/pegasus/kafka/worker.yml &
wait
peg fetch $CLUSTER_NAME

# install necessary components
peg install ${CLUSTER_NAME} ssh
peg install ${CLUSTER_NAME} aws
peg install ${CLUSTER_NAME} environment

# install and unzip confluent kafka files
peg sshcmd-cluster ${CLUSTER_NAME} "curl -O http://packages.confluent.io/archive/5.5/confluent-5.5.1-2.12.zip"
peg sshcmd-cluster ${CLUSTER_NAME} "tar -zxf confluent-5.5.1-2.12.tar.gz"
peg sshcmd-cluster ${CLUSTER_NAME} "mv confluent-5.5.1 confluent"

# install python libraries
peg sshcmd-cluster ${CLUSTER_NAME} "pip install faker"
peg sshcmd-cluster ${CLUSTER_NAME} "pip install confluent_kafka"
