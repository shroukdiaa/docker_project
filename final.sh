#!/bin/bash

# Create directory for results if it doesn't exist
mkdir -p /home/doc-bd-a1/service-result

# Copy all output files
cp res_dpre.csv eda-in-*.txt vis.png k.txt /home/doc-bd-a1/service-result/

# Exit container
exit