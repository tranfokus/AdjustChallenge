# Monitoring Challenge

## Requirement
'Monitoring a server used for SSL offloading'

## Metrics
For this server, two groups of monitoring metrics are often taken into account: 'Host/Server generic' and 'Application/Service specific'

### Host Generic Metrics
There are varios metrics including some common ones as follows:
* CPU Usage (%)
* Memory Usage (%)
* Disk Usage (%)
* Number of Threads
* Inbound/Outbound traffic per Network Interfaces (Mbps)
...

### Service Specific Metrics
As this server is used for SSL offloading, there are three types of metrics should be taken into consideration:
####Performance-related Metrics
* Service Inbound traffic (bytes)
* Service Outbound traffic (bytes)

* Request Rate (/s)
* Request Duration/Time (ms)

* Number of active connection 
####Error-related Metrics
* Number of drop connection
* Error Rate (%): is equal number of 5xx errors divided by total number of status codes

####Dependance-related Metrics
Monitoring information of backend(upstream) servers such as status, active connection ... 


## Solution


## Chalenges
