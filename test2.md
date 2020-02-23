# Monitoring Challenge

## Requirement
'Monitoring a server used for SSL offloading'

## Metrics
For this server, two groups of monitoring information are often taken into account: 'Host/Server generic' and 'Application/Service specific'

### Host Generic Metrics
At least, following metrics are taken into account:
* CPU Usage (%)
* Memory Usage (%)
* Disk Usage (%)
* Number of Threads
* Inbound/Outbound traffic per Network Interfaces (Mbps)


### Service Specific Metrics
As this server is used for SSL offloading, following metrics are important:

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

As a reverse proxy, this server needs other backend(upstream) servers for its functionality. As a result, related information from such servers are also importance for monitoring (e.g. upstream servers status, active connection ...) 


## Proposed Solution
```Deploying Elastic Beats at the SSL offload server to send monitoring information to a central ELK Stack monitoring system```

### Beats on the SSL offload server
* Metricbeat: Allows the collection of related generic metrics
* Filebeat: Allows the collection, parsing and sending of service specific log files (access log, error log)

### Central Monitoring System
It should include following core services:
* Logstash (Data Collection)
* Elasticsearch (Data Processing, Storage, Query)
* Kibana (Dashboard)
* ElastAlert (Alert)

## Challenges
With the propsed solution, there are several main challenges that can be briefly described as follows:
* Data Collection: We need to update/configure server to include related information in service access/error log files. Depend on which software solution running on the server (e.g. nginx, traffik, apache), we might have not all above mentioned specific metrics (as received information are limited/incomplete).     

* Performance: Running Beats log on the server will have some impact on the overal performance. The more information Beats collect, the more performance degradation the server has. Moreover, tranporting data over network to the centralized monitoring is subject to the delays and packet loss.

* Security and Privacy: Such system increases attack surface. The communication between server and central monitoring system needs to be protected (e.g. by encryption). Moreover, selected information for monitoring (log) might need to take into consideration related privacy protection regulations such as GDPR ...   

* Cost: Budget and time are required for maintaing/purchase such monitoring system, experts to manage/resolve issues.  
