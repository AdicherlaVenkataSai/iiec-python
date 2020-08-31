## WEEK 3
### DAY 5 | 23 August | [5. Python 3 API and CGI](https://www.youtube.com/watch?v=vBUx9KZyoZM&feature=youtu.be)  

[Q/A: What is the difference between Radio(Option) button and CheckBox used in HTML form?](https://www.linkedin.com/posts/iiec-rise_what-is-the-difference-between-radiooption-activity-6704649237650530305-rHAL)
```
will be updated soon
```     

**[Summary](https://www.linkedin.com/posts/iiec-rise_iiec-iiecabrrise-iiecabrconnect-activity-6703352555637899264-OF6y)**
-  CGI - Common Gate Interface: here on be-half of requesting(user) system, the host(server) system executes it for requesting one and shares the output, so it feels like requesting system itself is runnning the service and getting results. 
```
The CGI --> web services provided by host(server) system
setup webserver -- enable web services -- configure it
```
-  not found error -- clients (due to different directories) | internal server error -- server (3 types)
```
0. put code in /var/ww/cgi-bin
1. program should be executable (chomd to change the permissions) chomd +x filename
2. how webserver come to know, which compiler/interpreter to call
edit the file and write in first line which interpreter you want to use
#! she bang/ hash bang
#!python3 
.........
..........
 or

#!/usr/bin/python3   here were giving the path for it
.............
.................

note: this file can run using ./filename (only if has she bang and executable)

3. we run the python code, where to print the output in terminal? no
it should be printed on clients browser

client gets confused, how to print it? what is the type of content <content type>

server has to present the content type for the client

we should mention in the pythoncode

#!/usr/bin/python3 
print("content-type: text/html")  #its the header for the client
print()  # this new line will differentiate header with body part

...........   #body part
.............. #body part
```
-  instead of os.system we can use subprocess.getoutput
```
import subprocess
subprocess.getoutput("command")
# works similar as os.system
```

-  CGI directory is where we place our code/services, so that client request them and access (execute)
-  Content type acts as a header for the requesting system(user/client), this help to display the response from the host(server)
-  system(), subprocess() the functionality is same in some of the cases and are from different modules OS, SUBPROCESS resptively
-  file can be made executable using the chmod, which is used to change the permissions intead of chmod +x we can also use chmod 4
-  she bang/ hash bang (!#....) is used to show/explain which interpreter/complier is used to run the program/file
-  the new will play a major role in CGI, because it differentiates the header and the body, if not mentioned results in Internal error, because it assumes all of the lines are headers

```
will be implementing the steps and provide the ip link to try out yourself. (comming soon)
```
