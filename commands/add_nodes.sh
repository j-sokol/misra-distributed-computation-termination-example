
set -eux

# my_ip=`hostname -I | cut -d' ' -f1`

subnet_part=`hostname -I | cut -d' ' -f1 | cut -d'.' -f1,2,3`
port=5049

# echo "My IP is $my_ip"

cluster_range="2 3 4"
for i in $cluster_range; do
    curl -XGET "${subnet_part}.${i}:$port/find_nodes?subnet=${subnet_part}.0"
done
