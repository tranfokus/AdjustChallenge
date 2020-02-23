# Monitoring Challenge

## Requirement
'Monitoring a server used for SSL offloading'

## Metrics
For this server, two groups of monitoring information are often taken into account: 'Host/Server generic' and 'Application/Service specific'

### Host Generic Metrics
There are different metrics including some common ones as follows:
* CPU Usage (%)
* Memory Usage (%)
* Disk Usage (%)
* Number of Threads
* Inbound/Outbound traffic per Network Interfaces (Mbps)
...

### Service Specific Metrics
As this server is used for SSL offloading, following metrics should be taken into consideration:

Performance-related Metrics
* Service Inbound traffic (bytes)
* Service Outbound traffic (bytes)

* Request Rate (/s)
* Request Duration/Time (ms)

* Number of active connection 

Error-related Metrics
* Number of drop connection
* Error Rate (%): is equal number of 5xx errors divided by total number of status codes


Dependance-related Metrics

As a reverse proxy, this server needs other backend(upstream) servers for its functionality. As a result, related information from such servers are also importance for the monitoring (e.g. upstream servers status, active connection ...) 


## Proposed Solution
```Enabling/Deploying Elastic Beats on the SSL offload server to send monitoring information to a central ELK Stack monitoring system```

### Beats on the SSL offload server
* Metricbeat: Allows the collection of related generic metrics
* Filebeat: Allows the collection, parsing and sending of service specific log files (access log, error log)

### Monitoring System
Core components:
* Logstash (Collection)
* Elasticsearch (Processing, Storage, Query)
* Kibana (Dashboard)
* ElastAlert (Alert)
...



## Challenges
With the propsed solution, there are several main challenges that can be briefly describes as follows:
* Data Collection: Filebeat

* Performance
Tranporting data over network to the centralized monitoring is subject to the delays and packet loss

* Cost: 
