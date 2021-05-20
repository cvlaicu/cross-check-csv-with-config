# cross-check-csv-with-config
A script that cross checks the information from a CSV report with the actual device configuration. 

Scenario: 
We were provided with a large .xlsx file containing details regarding server hostname, the switch interface to which the server was connected and the VLAN number that was configured on the switch interface.

However, we noticed that the information provided by the .xlsx file regarding the VLANs configured did not correspond to the actual configuration on the switches.
We received the switches configuration and our job was to manually check whether the VLANs from our .xlsx file were the same ones that were configured on the switches.

This script replicates the enviornment (.xlsx file being file.csv) along with two puppet configs and eliminates the need to manually check hundreds of interfaces on dozens of switches to see whether they were correctly registered in the large .xlsx file. 
