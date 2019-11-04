#!/bin/bash


celery -A automate_test_py3 multi stop w1 
echo "start celery"

celery -A automate_test_py3 multi start w1 --logfile=./logs/celery.log 
