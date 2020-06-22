#!/bin/bash
python src/kafka/transaction_user_location_producer.py

python src/kafka/transaction_user_location_consumer.py