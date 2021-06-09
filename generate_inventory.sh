#!/bin/sh

build_number=$1
job_name=$2
host_env=$3
echo $1 $2

echo "host env for adhoc is "
echo $host_env

echo "[windows]" > /var/jenkins/workspace/$job_name/inventory

host=$(echo $host_env|sed 's/,/\n/g')

echo "$host" >> /var/jenkins/workspace/$job_name/inventory
