# Projects
## 1. Menu-Driven program (command based)   
Approach [Demo execution](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/1.%20Menu-Driven(commands%20based)/Demo%20execution.mp4) | [requirements](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/1.%20Menu-Driven(commands%20based)/requirements.txt) | [code](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/1.%20Menu-Driven(commands%20based)/tau.py) | [snaps](https://github.com/AdicherlaVenkataSai/iiec-python/tree/master/projects/1.%20Menu-Driven(commands%20based)/snaps) | [LinkedIn post](https://www.linkedin.com/posts/activity-6702170190412705792-55cH)    

-  As we're using the infinite loop, firstly we focus on developing appropriate conditions to terminate the loop.`exit/end/shudown` - terminate the program, `not exit` - shouldn't terminate the program.
-  Sometimes we end up searching random stuff which aren't available pre-definedly, if we encounter such case, program automatically asks permission to google it `(Y/n)`, acts according to the input.
-  Commands like `help` - list out all the possible commands with few suggesstions and `clear` - it acts similar as clear function (clears the prompt) will be helpful throught the program.
-  By default we're implementing few web sites like `facebook`, `linkedin`, `github`, `wikipedia`.. so on.
-  There  might be a situation where we end up typing nothing(empty input), program encounters it and suggest to try `help`
-  Even when we search for `do not launch camera` it works, mean it wont launch the camera as user requested, but the program can't handle `do not start chrome but start firefox` this type of situtation (currently working)    

Note: In this entire program we're only using `os.system` module , `nested-if else` statements, `while` and `print`  to achieve the desried output. This program is the basic step to achieve the major one.

[Updated]
-  added `speak` function for better interaction (command in speech out type)
-  added `pyjokes` to have some fun.

Note: If you want to execute the code, kindly ensure all the [requirements](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/1.%20Menu-Driven(commands%20based)/requirements.txt) are satisifed.   
Note: As we used `speak` function, [snaps](https://github.com/AdicherlaVenkataSai/iiec-python/tree/master/projects/1.%20Menu-Driven(commands%20based)/snaps) cant prove its beauty, so try it (I haven't updated the sanps, kindly go through Demo execution).

## 2. CGI- Menu-Driven program (simple linux commands)		
[Demo execution](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/2.%20CGI-MenuDriven/task2.mp4) | [code](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/2.%20CGI-MenuDriven/test) | [LinkedIn post](https://www.linkedin.com/posts/activity-6716418547117109248-cfR7)  
