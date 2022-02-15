## ✅ **_Windows Server Monitoring System_**
***

DailyCheck is for you if you want to __check status of Windows Server__ without installing Python in the server by running an __executable program__ with extension exe.
<br/>In order to build the exe file, please refer to _'How to execute DailyCheck'_ at the below.<br/><br/>

📝 DailyCheck is able to monitor:<br/>
* IP Address & Hostname
* CPU & Memory
* Disk Capacity
* Task Scheduler
* Windows Service
* Windows Defender
* Windows Event Viewer

📝 DailyCheck can also:<br/>
* __Log__ monitoring results (__json__)
* __Transfer__ the result file to the main server (__FTP__)
    
🔧 For the project DailyCheck, you should install (I also offer _requirements.txt_):<br/>
* BeautifulSoup4: To parse xml<br/>(Event Viewer, Windows Defender, Task Scheduler logs are written in xml format.)<br/>
`pip install beautifulsoup4`
* Pymssql: Database - SQL Server (MS-SQL) 2019.<br/>
`pip install pymssql`

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
>   4. Upload **_'daily_check.exe'_** to the Windows Server you want to monitor and run it.

🕑 If you want to run **_'daily_check.exe'_** with regularity:<br/>
>   1. Run **_Windows Task Scheduler_**
>   2. Open _'Create Task'_ and set _'General'_ and _'Triggers'_.
>   3. Go to _'Actions'_ and create new.
>   4. Add _DailyCheck_ to the _'Program/Script'_.

