![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
![Confluent Platform 5.5.1](https://img.shields.io/badge/Confluent%20Platform-5.5.1-orange)
![TimescaleDB 1.7](https://img.shields.io/badge/TimescaleDB-1.7.0%20-red)
![Grafana 6.7](https://img.shields.io/badge/Grafana-6.7-brightgreen)
![License MIT](https://img.shields.io/badge/License-MIT-yellowgreen)
# SwipeCheck

**A Platform for Real-time anomaly detection in Credit Card Transactions**

# Table of Contents
1. [Background](README.md#Background)
2. [Project Goal](README.md#Project-Goal)
3. [Approach](README.md#Approach)
4. [Architechture](README.md#Architecture)
5. [Repository Structure](README.md#Repository-Structure)
6. [Instructions](README.md#Instructions)
7. [Demo](README.md#Demo)
8. [Slide Deck](README.md#Slide-Deck)
9. [License](README.md#License)


**Chetan Patil - Insight Data Engineering (New York - Summer 2020)**

## Background
Credit card fraud has been steadily increasing over the years, but it exploded in 2019, with the number of reports increasing by 72.4% from 2018. In 2019 consumers reported losing more than $1.9 billion related to fraud complaints, an increase of $293 million from 2018 for lost/stolen cards. One of the major challenges in payment industry today is detecting credit card  fraudulent transactions for lost/stolen cards. 

## Project Goal
The goal of this project is to identify suspicious credit card transactions by comparing user and transaction location data in realtime and sending alert to user if the user is more than 8 km away in last 10 minutes.

## Approach

To simulate user location and transaction location data. A kafka producer is streaming the data at rate of 30000 messages/sec. the two stream (user and location) are joined with in 10 minute window and further calculte the distance between the user location and transaction location and if the user location more than 8 km away from transaction location we will alert the user.

## Architecture
  ![GitHub Logo](/docs/architecture.png)

## Repository Structure
   <pre>
   ├── bash_scripts           Scripts to run producer and consumer, setup kafka cluster and timescaledb
   ├── docs                   Configuration and setup information
   ├── src                    Source code for data generation and kafka producer, consumer
   ├── README.md              Information for running and setting up project
   └── application_config.py  config file which contains the properties constants
   </pre>

## Instructions

Pegasus is a tool that allows you to quickly deploy a number of distributed technologies.

Install and configure [AWS CLI](https://aws.amazon.com/cli/) and [Pegasus](https://github.com/InsightDataScience/pegasus) on your local machine, and clone this repository using 'https://github.com/chetanpatilofficial/SwipeCheck.git'

**SET UP CLUSTER**

(3 nodes) Kafka-Cluster , instance type: m4.large <br>
(1 node) PostgreSQL(Timescale) and Grafana , instance type: m5.2xlarge

Run bash_scripts/kafka_setup.sh and bash_scripts/timescaledb_setup.sh and follow the instructions in docs/setup.md to create required clusters, install and start technologies.

## DEMO
![Credit Card Fraud Detection Demo](docs/demo/grafana-dashboard.gif)

## Slide Deck
[Demo Slides](https://tinyurl.com/yc9sclht)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
