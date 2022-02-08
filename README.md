## ✅ **_Windows Server Monitoring System_**
***

DailyCheck is for you if you want to __check status of Windows Server__ without installing Python in the server by running an __executable program__.<br/>In order to build the exe file, please refer to _'How to execute DailyCheck'_ at the below.<br/><br/>

📝 DailyCheck is able to monitor:<br/>
* IP Address & Hostname
* CPU & Memory
* Disk Capacity
* Task Scheduler
* Windows Service
* Windows Defender
* Windows Event Viewer

📝 DailyCheck can also:<br/>
* __Log__ monitoring results into log file (__xml__)
* __Transfer__ the log to the main server (__FTP__)
    
🔧 Before using DailyCheck, you should install:<br/>
* BeautifulSoup4: To parse xml<br/>(Event Viewer, Windows Defender, Task Scheduler logs are written in xml format.)<br/>
`pip install beautifulsoup4`

* Pymssql: I've used SQL Server (MS-SQL), version 2019.<br/>
`pip install beautifulsoup4`

🔧 How to execute DailyCheck:<br/>
