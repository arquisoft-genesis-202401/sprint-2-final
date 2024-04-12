#!/bin/bash
sudo apt update && sudo apt install -y influxdb
sudo sed -i 's/^  bind-address.*/  bind-address = "${INTERFACE_LOG_DATABASE}:${PORT_LOG_DATABASE}"/' /etc/influxdb/influxdb.conf
sudo sed -i 's/^  max-connections.*/  max-connections = ${MAX_CONN_LOG_DATABASE}/' /etc/influxdb/influxdb.conf
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb
sudo systemctl enable influxdb.service
influx -execute 'CREATE DATABASE ${LOG_DB_NAME}'
influx -execute "CREATE USER ${LOG_DB_USER} WITH PASSWORD '${LOG_DB_PASSWORD}'"
influx -execute "GRANT ALL ON ${LOG_DB_NAME} TO ${LOG_DB_USER}"
echo "Done"


