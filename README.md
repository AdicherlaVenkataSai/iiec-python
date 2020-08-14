# IIEC (Indian Innovation & Entrepreneurship Community) - PYTHON 
>  *Specialization in Python (with flask towards Data Science)*   
Instructor [Mr. Vimal Daga](https://www.linkedin.com/in/vimaldaga/) Sir || [IIEC - RISE](https://www.linkedin.com/company/iiec-rise/) || [Google Drive (screen shots)](https://drive.google.com/drive/folders/1RAJNUsdK2TWK94rrByaouXPkKDlR6-vb) || [Telegram (updates)](https://t.me/joinchat/AAAAAFepWVRLIsjqwCO6_w) || [Discord (doubts)](https://discord.com/invite/DqAgTT)

### DAY 1 | 8 August    
Anaconda | [windows](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe) | [mac os](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.pkg
) | [linux](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
) | [other](https://www.anaconda.com/products/individual)   
[1. Session](https://www.youtube.com/watch?v=VW0PUBSxVxg&feature=youtu.be) || [Q. How to read data stored in RAM?](https://www.linkedin.com/posts/iiec-rise_how-to-read-the-entire-data-from-the-ram-activity-6698235562727411712-VhnS)    
Note: deadline 15th August    

**Things learnt**   
1. how to make python to launch notepad/ chrome/ any particular site in chrome
``` python    
import os   
os.system("notepad")
os.system("start chrome")
os.system("start chrome  youtube")
```   
2. how to make python to speak out the argument passed   
``` python
pip install pyttsx3
import pyttsx3
pyttsx3.speak("Welcome world")
pyttsx3.speak("It's good to learn How to learn")
```     
### DAY 2 | 9 August
[2. Session](https://www.youtube.com/watch?v=Mk3HvO3YEl8&feature=youtu.be) || [Q. How to read data stored in RAM?](https://www.linkedin.com/posts/iiec-rise_how-to-read-the-entire-data-from-the-ram-activity-6698235562727411712-VhnS)

**Things learnt**
1. Summary : 
    -  Fundamentals of learning (how to understand things)
    -  exploring what all we can do with command prompt in windows
2. New :
    -  Underhood function of accessing an elements in list
    -  Varibales(at a time can store only one element) has its limitation, so we moved to lists
    -  Limitation of list data type (can only do row operations but not col operations), so we moved to numpy array (can do both row and column operations)
    -  In order to use a package first we need to know about it well rather using for the solving the current situation
    -  whats those `>>>`  in live programming, its called REPL (Read Evaluate Print Loop) | [webiste](https://repl.it/languages/python3)
3. Idea : Take few minutes to go through the core usage/ limitation/ documentation of every module in use
``` python
notepad test.py  # by deafults it is saved with "test.py" .txt extension
notepad "test.py"  # no extension
dir  # to check it

# when we declare a list to hold multiple elements, access them using list_name[index_number], the underhood function is 
list_name.__getitem__(index_number)

# when we import a module, if we wants to what all the functions it provides
dir(module_name)

# what about built-in functions of python, then try this
dir(__builtins__)
```      

### redhat sessions     
[1. Session](https://youtu.be/8Q83qs2MAVA)      
**Summary**      
-  To find out the way to browse a ram. (Suppose when we intialize any variable x=5; in our program than it is taught to us that it gets stored in ram but now how one can proof that it is present in the ram.) 
-  About GUI(Graphical User Interface) and CLI(Command Line Interface) 
-  How to open applications using terminal (eg. Typing Firefox on the radhat and pressing enter will open the browser) 
-  speak-ng command(to speak what O/P it is giving), date cmd, cal command, which command 
-  Saw that the cookies that fb and google send to our systems are very critical and even if someone by any way copies them to his/her system can get a complete acess of our Google and Facebook accounts or and other accounts and will never be asked to enter any username password and no otp verification will be there and also  a 3 level verification will not work

[2. Session](https://youtu.be/JBNvnINsswo)      
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
testing file which is created [file](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/linux%20resources/testing)     
[3. Session](https://youtu.be/lpZysBJ2CRA)      
**Summary**         
[4. Session](https://youtu.be/aPyJQVC6R9E)      
**Summary** 

