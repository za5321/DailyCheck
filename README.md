###Windows Server Status Check System

+ Checking List
    * IP Address / Hostname
    * CPU / Memory
    * Disk Capacity
    * Task Scheduler
    * Service
    * Windows Defender
    * Event Viewer

+ Function
    * Logging
    * Create a result file (json format)
    * Transfer the result to the main server (FTP)
    
+ Library
    * BeautifulSoup4 : To parse xml (Event Viewer, Windows Defender, Task Scheduler log file)
    * Database : Pymssql
    