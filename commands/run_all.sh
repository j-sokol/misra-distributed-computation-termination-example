#!/bin/bash

set -eux


bash add_nodes.sh

bash assign_token.sh

bash simulate_computing.sh