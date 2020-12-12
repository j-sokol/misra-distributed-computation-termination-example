#!/bin/bash

set -eux

my_ip=`hostname -I | cut -d' ' -f1`
port=5049

echo "My IP is $my_ip"

curl -XGET "$my_ip:$port/nodes"
