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
1. how to make python to launch notepad/ chrome/ any particular site in chrome.
``` python    
import os   
os.system("notepad")
os.system("start chrome")
os.system("start chrome  youtube")
```   
2. how to make python to speak out the argument passed.   
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
    -  exploring what all we can do with command prompt in windows.
2. New :
    -  Underhood function of accessing an elements in list
    -  Varibales(at a time can store only one element) has its limitation, so we moved to lists
    -  Limitation of list data type (can only do row operations but not col operations), so we moved to numpy array (can do both row and column operations)
    -  In order to use a package first we need to know about it well rather using for the solving the current situation.
    -  whats those `>>>`  in live programming, its called REPL (Read Evaluate Print Loop) | [webiste](https://repl.it/languages/python3)
3. Idea : Take few minutes to go through the core usage/ limitation/ documentation of every module in use.
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
