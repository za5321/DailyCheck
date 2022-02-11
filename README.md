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
* __Log__ monitoring results into log file (__json__)
* __Transfer__ the log to the main server (__FTP__)
    
🔧 For the project DailyCheck, you should install:<br/>
* BeautifulSoup4: To parse xml<br/>(Event Viewer, Windows Defender, Task Scheduler logs are written in xml format.)<br/>
`pip install beautifulsoup4`
* Pymssql: Database - SQL Server (MS-SQL) 2019.<br/>
`pip install beautifulsoup4`

🔧 How to execute DailyCheck:<br/>
>   1. Install Pyinstaller - It helps build python project into exe file easily.<br/>
    `pip install pyinstaller`
>   2.  Type the command line below. <br/>
    `pyinstaller --onefile --add-data=conf\*;conf --name daily_check Main.py`<br/>
    These options are:<br/>
    --onefile: Should you need a neat single exe file, this option is going to help you.<br/>
    --add-data: The option must be added in order to apply configuration to your executable program.<br/>
    --name: You can set the name of exe file.<br/>
>   3. After building, you can find **_'daily_check.exe'_** at **_'dist'_** folder.
