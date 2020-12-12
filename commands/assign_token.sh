#!/bin/bash

subnet_part=`hostname -I | cut -d' ' -f1 | cut -d'.' -f1,2,3`
port=5049

curl -XGET "${subnet_part}.2:${port}/assign_token"
