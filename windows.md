## Firewall

To allow a port to be accessed from outside it has to be whitelisted in windows firewall rules.  
**Windows Defender firewall** hosts the rules of windows firewall. Two kind of rules.  
1. Inbound Rules  
    Rules to specify connection from other computers to this computer.
2. Outbound Rules  
    Rules to connect to other computer/network by an application of this computer.


## Password Reset

Reset Password if you are logged in
* Open cmd with admin privilege
* Type <code>net user Administrator *</code>

## Task Scheduler

* To have the console screen up user has to be specified. The task should start when that specified user is logged on.
* A bat file containing the excutor and script file works better than simply putting the script file direct to the action list.
  `python_path\python.exe  script.py `
* If console window is to be avoided then use file extension 'pyw' for python scripts
* To open startup folder from run type `shell:startup`