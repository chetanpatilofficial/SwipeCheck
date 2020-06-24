#!/bin/bash
ROOT=$(dirname ${BASH_SOURCE})/../..

CLUSTER_NAME=postgres-node

# starting instances
peg up ${ROOT}/docs/config/pegasus/kafka/master-postgresql.yml &
wait
peg fetch $CLUSTER_NAME

# install necessary components
peg install ${CLUSTER_NAME} ssh
peg install ${CLUSTER_NAME} aws
peg install ${CLUSTER_NAME} environment

