### redhat sessions     
[1. Basic linux commands ](https://youtu.be/8Q83qs2MAVA)      
**Summary**      
-  To find out the way to browse a ram. (Suppose when we intialize any variable x=5; in our program than it is taught to us that it gets stored in ram but now how one can proof that it is present in the ram.) 
-  About GUI(Graphical User Interface) and CLI(Command Line Interface) 
-  How to open applications using terminal (eg. Typing Firefox on the radhat and pressing enter will open the browser) 
-  speak-ng command(to speak what O/P it is giving), date cmd, cal command, which command 
-  Saw that the cookies that fb and google send to our systems are very critical and even if someone by any way copies them to his/her system can get a complete acess of our Google and Facebook accounts or and other accounts and will never be asked to enter any username password and no otp verification will be there and also  a 3 level verification will not work

[2. Basic commands, Virtual box setup, Redhat 8 installation](https://youtu.be/JBNvnINsswo)      
**Summary** 
-  how to pause the command by using 'sleep'
-  difference between 'ctrl+z' and 'ctrl+c'
-  use of '&'
-  use of echo and how we can use it in different ways
-  how to install rethat linux 
-  how to recognize the correct IP address

Installation of Rhel:
1. Download any virutal box ([vmware](https://www.vmware.com/in/products/workstation-pro/workstation-pro-evaluation.html) | [oracle](https://www.oracle.com/in/virtualization/technologies/vm/downloads/virtualbox-downloads.html))     
Note: This links are for windows, if your using another os, kindly search for appropriate one.
2. Download the iso file [rhel 8](https://ia801004.us.archive.org/4/items/rhel-8.0-x86_64-dvd/rhel-8.0-x86_64-dvd_archive.torrent)    
3. Install the virtual box and setup the configurations     
Note:  This installation is wrt oracle virtual box
-  open and click `New`
-  we can observe a popup box named "Create Virtual Machine" fill the detials like `Name(any)`, `Type(linux)`, `Version(RedHat 64bit)` and click `Next`   
-  `Memory size` preferred 1GB or more and click `Next`
-  `Hard disk` choose `Create a virtual hard disk now` option and click `Create`
-  `Hard disk file type` choose `VDI(VirtualBox Disk Image)` option and click `Next`
-  `Storage on physical hard disk` choose `Dynamically allocated`option and click `Next`
-  `File location and size` preferred 10GB to 100GB and click `Create`
-  now the hardware setup is done, you can observe it in the left window
-  for software setup, right click and choose `settings` and can check the hardware configuration's, go for `storage` settings
-  `settings` > `storage` > `Controller IDE : empty` click on `empty` find Attributes in side window
-  `Attributes` > `Optical Drive` choose the ISO file location and click `Ok`, now both hardware and software got setuped
-  click on file created (is avaliable in left window with the name 'Name(any)') and click `start`
-  now you can see a black screen with few options (cursor won't work, use arrow keys) and choose `Install Red Hat Enterprise Linux 8.0.0`
-  wait until you see `WELCOME TO RED HAT ENTERPRISE LINUX 8.0.0`and choose the required language
-  now you're at `INSTALLATION SUMMARY` click on `Installation  Destination` Automatic partitioning selected and click `Done`
-  select the `Network & Host Name` to connect to the network and click `Done`
-  select `Software Selection` and choose `Workstation` option from the available one's and click `Done`
-  select `Time & Date` to change the time zone and click `Done`
- now click `Begin Installation` it takes some time to install
- now at `CONFIGURATION` to setup the password for thr `root`

4. Finally the installation is done!!

Issue: If you can't see RedHat 64bit, kindly follow these steps:
-  restart (shutdown and start).
-  enter the bios (press f12). 
-  advance settings / CPU configurations.
-  find `Enable Virtualization` and enable it.
-  save the settings (press f10) and start the system.

Note: check the function keys for your device and use it (they may vary from device to device).     
Note: Still any issues can raise a question at [channel](https://discord.com/channels/740913042413584425/741900875043438710) 


![a](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.a.session.png)      
![b](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.b.session.png)      
![c](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.c.session.png)      
![d](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.d.session.png)      
![e](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.e.session.png)      
![f](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.f.session.png)      
![g](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.g.session.png)      
![h](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.h.session.png)      
![i](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.i.session.png)      
![j](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.j.session.png)      
![k](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/2.k.session.png)      
testing file
```
while : ; do echo -n -e "`date +%T``sleep 1`\b\b\b\b\b\b\b\b" ; done &
```
[3. Basic linux networking Unique tip about IP address](https://youtu.be/lpZysBJ2CRA)     
**Summary**
-  `ifconfig` shows all the ip address, the first one of all is actual `ether` ip address.
-  mobile number cloning
-  valid ip address is of 4 bytes (representation can be any)
-  neospace (shows ip routing)
-  use `nslookup site-name`
```
$ nslookup youtube.com

Server:		127.0.0.53
Address:	127.0.0.53#53  (actual ip)

Non-authoritative answer:
Name:	youtube.com
Address: 216.58.196.78
Name:	youtube.com
Address: 2404:6800:4009:809::200e
```
-  how do ip get stored in ram? 4 bytes
```
will be updated soon!
```
[4. Linux n'Python basic ](https://youtu.be/aPyJQVC6R9E) 

**Summary**     
-  `gnome-terminal` command can create a terminal.

```
# its a bash script
for((i = 0; i<10; i++))
do
gnome-terminal
done
# note: It creates 10 terminals at the instance of executing the code.
# and manually closing them will be hectic if the no of terminals are more.
```
-  `which <command-name>` gives the path of the command.
-  `ps -aux` is used to view all the commands in running state.
-  `ps -aux | grep <command-name>/<keyword>` to search it.
-  To close a command we can do `manually`, or `clt+c` , or `kill <process-id>`
-  To close the huge no of terminals we can use the `kill <process-id>` command and the process id can be obtained using `ps -aux | grep <gnome-terminal>`
-  `cat > <filename.extension>` to see the data directly on prompt/terminal, it can also used to create file and write data from CLI. It even replaces the new data
using a slight change in syntax `cat >> <filename.extension>`, which appends the data to exsisting file.
-  `touch <filename.extension>` is also used  to create the file (only).
-  To add a new user,`useradd  <user-name>` and set password `passwd  <password>`.
-  To verify the account created or not `id <user-name>`, it return few details if exist, else  gives `no such user`.
-  `whoami` gives the username / use `tty`.   
-  [Can we switch the console, with out logging out from one?]()
```
will be updated soon!
```
-  Mutiple terminals == virtual terminals
-  To switch terminals use `clt + alt + fi`, where f refers to function key i th terminal , or use `chvt <terminal-number>` (change terminal). 
-  At max redhat has we can have 6 termianls default, 2 GUI (f1/f2), 4 CLI(f3-f6).
-  Can you enable the mouse interation in linuc CLI? if yes. how?
-  `CLI`--> `GUI`, for this use `startx` command.
-  [How to create more than 6 virtual teminals in redhat8?]()
```
will be updated soon!
```
-  [How to create a file without command?]()
```
will be updated soon!
```
-  `>  <filename.extension>` it creates a file ( `>` is a symbol), here we dont use any command. But [how its possible to create file with out a command?]()
```
will be updated soon!
```

[5. Remote login - ssh Putty ](https://youtu.be/23u8LKt6uSw) 
    
**Summary** 
-  
-  

[6. Configure webserver](https://youtu.be/nXJEe8WoBmg)       
**Summary** 
-  
-  
