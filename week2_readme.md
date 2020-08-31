## WEEK 2
### DAY 3 | 15 August | [3. Python 3 basics to expert](https://youtu.be/ElOJReuu60g)	

[Q/A: How to tell your OS to send a whatsapp message to a particular number using python code?](https://www.linkedin.com/posts/iiec-rise_how-to-tell-your-os-to-send-a-whatsapp-message-activity-6700461293234597888-RJnH/)
```python3
# solution will be updated soon
```
[Q/A: What is the name of the concept or process used by double quotes to process the escape sequence characters?](https://www.linkedin.com/posts/iiec-rise_what-is-the-name-of-the-concept-or-process-activity-6700461662400471041-Ft4K/)
```python3
# solution will be updated soon
```
[Q/A: What is the name of the concept or process used by double quotes to process the escape sequence characters?](https://www.linkedin.com/posts/iiec-rise_how-to-tell-your-os-to-send-a-sms-to-a-particular-activity-6700462001153429504-UiZW/)
```python3
# solution will be updated soon
```
[Q/A: How to tell your OS to send an email to a particular email-id using python code?](https://www.linkedin.com/posts/iiec-rise_how-to-tell-your-os-to-send-an-email-to-a-activity-6700462219622158336-Zmf_/)
```python3
# solution will be updated soon
```
**[Summary](https://www.linkedin.com/posts/iiec-rise_day2-iiec-iiecabrrise-activity-6700446400737501184-xvOx/)**  
-  In general function's are used to perform respective tasks, `speak()` is a function which is available in the `pyttsx3` module. which is used to output the audio from  the system.
```python3
import pyttsx3
pyttsx3.speak('output the audio')
# this snippet makes system to speak out 'output the audio', in general, it speaks what ever the argument is passed to the speak()
```
-  n order to perform some tasks we need respective function to do it, all these function's might not be available in the default module, sometimes we need to import few packages/modules for an special tasks to be done, just like `pyttsx3` module.
```python3
pip list  # this shows what all modules we have
# if the module isn't available then install it.
pip install pyttsx3  # pip install module-name
```
-  IDE - Integrated Development  Enviroment | In jupyter (python + r + julia) | `shift + enter` to run cell | `alt + enter ` to run the cell and create a new cell | `clt + enter` to run the selected cells | `esc + d` will delete the cell 
-  To run the system commands we need to, we need to use operating system functions to communicate with os and make those commands get executed
```python3
import os
os.system('firefox')
# this snippet enables us to run firefox bowser using python code
```
-  In the Menu- Driven program , we trying build the human interactive program, which performs the tasks whcih ever the user asks. Currently we're building it
We a first task to build the as good as interactive model as we can.

-  help() funtion provides us the complete detail of the commands which we wants to use/ which we are using
`print()` command has an argument `end = '\n'` by default it is set to a new, we can modify it and can see the changes in the `print()` function behaviour.

- conditional if and else, the name itself speaks for  it
```python3
if True: do some task
else: dont do the task
# this is naive explaination.
```
simple application 
```python3
# importing required modules

import os  # use to access the os programs
import pyttsx3  # use to make python speak out for us  !pip install pyttsx3
# if the modules aren't available, install them

# code
pyttsx3.speak(" Welcome to my application (here are the services we provide) ")
print("\n Welcome to my application (here are the services we provide)  \n 1. launch firefox \n 2. launch chrome \n 3. launch notepad \n 4. Media Player")

pyttsx3.speak("Option one launch firefox browser")
pyttsx3.speak("Option two launch chrome browser")
pyttsx3.speak("Option three launch notepad")
pyttsx3.speak("Option four launch media player")
pyttsx3.speak("Kindly")
pyttsx3.speak("enter your choice")
user_input = int(input("\n Enter your choice :"))

# note the commands might vary to device to device
if user_input == 1:
	os.system("firefox")
elif user_input == 2:
	os.system("start chrome")
elif user_input == 3:
	os.system("notepad")
elif user_input == 4:
    os.system("wmplayer")
else:
    pyttsx3.speak("Oops, you might have entered invalid input")
	print('Invalid input !!')
    
```
### DAY 4 | 16 August | [4. Python 3 basics to expert](https://youtu.be/2PjfpSgtuE8)  

[Q/A: How to reverse the string using the slicing operator?](https://www.linkedin.com/posts/iiec-rise_how-to-reverse-the-string-using-the-slicing-activity-6700816023345475584-imu6/)
```
will be updating soon
```
**[Summary](https://www.linkedin.com/posts/iiec-rise_iiec-iiecabrrise-iiecabrconnect-activity-6700804279592087552-vjk3)**  
-  we have explored how to run the `juypter notebook` from command promt, also we have seen few shortcuts in it

-  new shortcut `alt + enter` to run the cell and create new cell

-  string datatype holds bunch of characters, each of them can be indexed similar as lists

-  slicing operator is either used in lists/ strings to slice the data
```python3
x = 'this is the summary for day4'
x[0]  # prints t
x[0: 4]  # prints this
# this slicing from 0th pos to (4-1)th pos
x[0:4: 1] # prints this
# here the step size is 1
x[0:: 3] # prints tsshsmyod4
# here the step size is 3
# note: I miss interpreted the output, can check the snap
x[-1]  # prints 4
# this is used to print the last element
x[::-1] # prints the string in reverse
```
![a](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/resources/4.a.session.png)

-  here we got introduced with the `in` keyword of python, which will be a major advantage in developing the human interactive program
-  this will be a part of human interactive program, where we provide a menu for the user to select the option and make them executed using the python program, which do them interacting with os

-  logical opertors either it returns `True` or `False` based on the condition is evaulated
-  `while`loop is similar like `if` statment, it executes as long the condition is satisfied. If the intial condition doesnt satisfy it wont enter into the loop
-  `break` keyword is used to terminate the loop
-  use the concepts we learnt till date, we can input human usable language and extract keywords from it to perform the task which user requested
-  every string is can be accessed similar as list
```python3
x = 'hello'
print(x[0])  # prints out h

# we can even apply slicing operation
# prints starting pos to (5-1)th pos
print(x[:5])  # prints out hello

# in steps
# print(x[0:2:step_size])
# it prints it with step size of 2  
print(x[0:5:2])  # prints out hlo

# to print the last one
print(x[-1])  # prints o

```
-  `shift + enter` to run the cell
-  `alt + enter` to run and create a new cell 
-  to check whether a word/ character present in given strinf we can use `in` keyword

```python3
x = 'this is the example done in jupyter notebook'
print(x)

if 'jupyter' in x:
    print('Hurray!! given statement has juypter in it')
else:
    print('Sorry!!')
```
```python3
import os
x = 'can you launch the chrome browser'
print(x)

if 'chrome' in x:
    os.system("start chrome")
else:
    print('Sorry!!')
    
```
simple application 
```python3
# importing required modules

import os  # use to access the os programs
# import pyttsx3  # use to make python speak out for us  !pip install pyttsx3
# if the modules aren't available, install them

# code
user_input = input('Enter your request :')

if(('launch' in user_input) or ('run' in user_input)) and (('notepad' in user_input) or ('editor' in user_input)):
	# os.system('start chrome') windows
	os.system('google-chrome')  # linux
else:
	print('Invalid choice!')
```

Note: Need's to devlop more interactive system with mutliple tasks (deadline 22 august)	
