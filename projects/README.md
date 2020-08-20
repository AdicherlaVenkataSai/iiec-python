# Projects
## 1. Menu-Driven program (command based)   
Approach | [code](https://github.com/AdicherlaVenkataSai/iiec-python/blob/master/projects/1.%20Menu-Driven(commands%20based)/app.py) | [snaps](https://github.com/AdicherlaVenkataSai/iiec-python/tree/master/projects/1.%20Menu-Driven(commands%20based)/snaps) | [LinkedIn post](https://www.linkedin.com/posts/activity-6702170190412705792-55cH)    

-  As we're using the infinite loop, firstly we focus on developing appropriate conditions to terminate the loop.`exit/end/shudown` - terminate the program, `not exit` - shouldn't terminate the program.
-  Sometimes we end up searching random stuff which aren't available pre-definedly, if we encounter such case, program automatically asks permission to google it `(Y/n)`, acts according to the input.
-  Commands like `help` - list out all the possible commands with few suggesstions and `clear` - it acts similar as clear function (clears the prompt) will be helpful throught the program.
-  By default we're implementing few web sites like `facebook`, `linkedin`, `github`, `wikipedia`.. so on.
-  There  might be a situation where we end up typing nothing(empty input), program encounters it and suggest to try `help`
-  Even when we search for `do not launch camera` it works, mean it wont launch the camera as user requested, but the program can't handle `do not start chrome but start firefox` this type of situtation (currently working)    

Note: In this entire program we're only using `os.system` module , `nested-if else` statements, `while` and `print`  to achieve the desried output. This program is the basic step to achieve the major one.    



