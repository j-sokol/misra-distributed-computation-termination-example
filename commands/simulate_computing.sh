#!/bin/bash

random_compute_time() {
    echo $(( ( RANDOM % 10 )*3 + 5))
}



subnet_part=`hostname -I | cut -d' ' -f1 | cut -d'.' -f1,2,3`
port=5049

# curl -XGET "${subnet_part}.2:${port}/assign_token"

for node in {2..4}; do 

    compute_time=`random_compute_time`
    echo "Starting compute on ${subnet_part}.${node} for ${compute_time}s"
    echo curl -XGET "${subnet_part}.${node}:${port}/compute?compute_time=${compute_time}"
    # & to detach it and run "compute" in paralel
    curl -XGET "${subnet_part}.${node}:${port}/compute?compute_time=${compute_time}" &


done 