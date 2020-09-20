## WEEK 6
### DAY 9 | 12 September | [9. Python 3 API and CGI](https://youtu.be/OFzbAn0IAfQ)

**[Summary](https://www.linkedin.com/posts/iiec-rise_iiec-iiecabrrise-iiecabrconnect-activity-6710600904183173120-6dYb/)**

-  In general when we type/give  `keystroke`  the system/ software `echo back` the storke, so that it will be displayed/visible on the screen. In order to hide the `echo back` we use `getpass` function from `getpass` module. 

```python
import getpass()
x = getpass.getpass()
# o/p: Password = *****

x = getpass.getpass("Enter your secret number: ")
# o/p: Enter your secret number: *****

# note: here ***** will be the respective secret which you have typed.
```

-  `exit code` is used to check whether the command is executed successfully or not. `echo $?` will gives the `exit code` for the last executed command.
- `os` module system function internally use `print` function so if we need to store the output of any command run by system. It will not store it in the variable. `x = os.system("date")`, here the value is not stored in `x`, it directly prints the value. The difference between `system` and `subprocess`, both are used to execute commands. If we run the command through `system`, we'll have `command output` and `exit code`. In `subprocess` it shows the output as a `tuple as ('exit code', 'command output')` when we use `getstatusoutput` in it.
-  lists are `mutable` - values are rewritable. Sets are `immutable` - readonly.
-  To secure the code, we need to use `server side langugae`, we can consider `google` as an example, even though we can see the source code of google search page, but the underlying `search algorithm` is hidden.


### DAY 10 | 13 September | [10. Python 3 API and CGI](https://youtu.be/-3n3ifUDIh8)

**[Summary](https://www.linkedin.com/posts/iiec-rise_iiec-iiecabrrise-iiecabrconnect-activity-6710943431251763200-xTuW/)**
-  Learned about docker technology which is used to deploy and run applications using containers. Uisng docker images we can  host OS libraries and having better performance than VM. Easy to spin up and maintain.        
    `docker run –i –t <osname> <os type>` - to run the docker.       
    `docker ps - a` - to check all running containers.      
    `docker run –i –t –d <osname> <os type>` - to run the docker in background. 
    `docker stop <osname>` -  to stop the docker
- We can create python application with integration of docker by make use of API and docker operations can be performed directly from browser , there is no need to login to system. 
- Placeholder `{ }` concept is used to replace with `format()`, the variables which are available in the `print` function. As we know `print` function considers everything as a `string` which are within the `" "`. To have variable value their we use `string interpolation`.
```python
x = 5
print("The value of x is x")
# o/p: The value of x is x

print("The value of x is {}".format(x))
# o/p: The value of x is 5

y = 10
print(" The value of x is {} and y is {}".format(x,y))
# The value of x is 5 and y is 10

print(" The value of x is {} and y is {}".format(x))
# one index is missing error

print(" The value of x is {0} and y is {1}".format(x,y))
# The value of x is 5 and y is 10

print(" The value of x is {1} and y is {0}".format(x,y))
# The value of x is 10 and y is 5

print(" The value of x is {0} and y is {0}".format(x,y))
# The value of x is 5 and y is 5

print(" The value of x is {0} and y is {0}".format(x))
# The value of x is 5 and y is 5
```
-  To launch docker container with Python and CGI we have followed below steps:
```
Create one form inside /var/www/html path to accept user input and set form action url to cgi-bin python file.
Use ip address of machine where we are sending the request. 
Create one python file in /var/www/cgi-bin path of apache web server.
Import subprocess and cgi module.
Now fetch user inputs from submitted form using cgi.fieldstorage(), Getvalue(<variable name that we passed in form>).
Store docker command along with placeholder and format function to accept user inputs in one variable and pass it into subprocess.getoutput ( ).
Now on submission of form from browser end it will spin up OS container in machine.
```