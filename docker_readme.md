[Docker Installation Documentation](https://docs.docker.com/engine/install/ubuntu/)

### docker sessions     

[1. Session](https://www.youtube.com/watch?v=-lpDRE3Fcj0&feature=youtu.be)      
**Summary** 
-  Operating System Provisioning `Bare Metal`, `Cloud Computing`, `Virtualization` and `Docker`.
Note: We use docker because it has less provinsion time like `1 sec` to completely install and load the os, while others take `30-60 mins`.
-  `systemctl status docker` - docker status.
-  `systemctl start docker` - starts the docker but as soon as the system is restarted it gets stop.
-  `systemctl enable docker` - these help to enable the docker services on even after the system restart.
-  `systemctl stop docker` - stops the docker.
-  `docker info`- To have more information about docker.
-  `docker ps` - gives the os(how many) are running inside the docker.
-  `docker images` - gives the no.of images we have.
-  `docker pull <os-required>:<version>` - downloads the os image from the docker community (which has all the os images at public repository `hub.docker.com`),  we can create our own public and private repositories too.
-  `docker run <os-name>:<os-version>` launches new os.
-  `docker run -t <os-name>:<os-version>` launches the new os and opens the terminal `-t` (doesnt repsond to the commands).
-  `docker run -t -i <os-name>:<os-version>` launches the new os and opens the terminal(with the docker id) and makes it interactive `-i` (responds to the commands), to check whether it got launched or not, we can check with `docker ps` command. To shutdown the terminal and os we can use `exit` command.
-  **Ever wondered how docker can do in such less time?**
-  In general we need ram and memory to host another os, but docker consumes very less ram(space) about `10mb to 20mb`. You can validate the statement using these commands  `free -m` (memory), `watch -n <time in sec> free -m` (we dynamically check the ram using these commands with 1sec time), now note down the ram available and try to launch new container(os) using docker and observe the difference in the ram available.
-  The `docker services`(commands) run only inside the `host OS` where docker is installed. When we lauch a new container(os), and try to launch docker services, commands wont work inside the contianer.
-  `docker ps -a` - gives the all os, that are currently being running or stopped. Using these command you can get the containers `id` and `names`.
-  `docker start <containere-id>/<container-name>` -  will restart the conatiner(os) in background.
-  `docker attach <containere-id>/<container-name>` -  we can go into the container(os), press `enter` twice to get into it.
-  `docker images` - gives the images list, you had.
-  `docker run -it --name <any-name-you-wish-to-give>  <os-name>:<os-version>` -  we can give the desired name to it (can assign some meaningful name as per work). `-it` command is replace of `-i -t` (interactive terminal). If we launch the container again and again with same os-name, os-version we need to specify `different names every time`. Instead we can use the already created container using `attach` command.
-  `exit` -  to shutdown the container(assuming were inside the contianer), `docker stop` -  to stop the docker contianer(assuming were in host os).
-  **How docker launches the container in 10 to 20mb memory?**
-  `which <command>` - gives the location of that particular command. `rpm -q -f <location>` - gives the software which is providing that command. If any command isn't working in the container(os), check the command in host os and its software. The software might be missing in the docker container(os), so the command isn't working. Install the software, and check again(it works).
-  The data store in the docker container is permanent until we delete the docker container. `docker rm <container-id>` - will removes/ deletes the containers.
-  Docker containers provides the `isolation` (if we affected with any bug/virus) it cant affect the outside the container. In general we can lauch `one container` for `one program` (python - os1, firefox - os2 ...).
-  Inside the docker program gives output as CLI/text - can be displayed on terminal, but when it gives output as GUI(Chrome, firefox, other GUI applications) - it gives error `no DISPLAY environment variable specified`.
-  **Does it mean can't we lauch a GUI pogram in docker contianer? YES but how?** 
-  `docker rmi <os-name>:<os-version>` -  to remove the image os, if its shown any error we can force it remove using `-f` (in end).
-  old:`docker --help`, new: `docker <management-commands> --help` - all commands of docker is available.
-  `docker <special-commands> <other-options>` -  it's more specific each type special-commands/management-commands (container, image, volume, swarm). old:`docker <command> options`, new: `docker <management-commands> <command> options`.
-  `echo date` - treats date as a string, `echo $(date)` - treats it as command and returns the output.
-  `docker container ls -a -q` - gives the complete Id list of the containers.
-  In order to remove all the containers, instead of doing one by one we can use `docker container rm $(docker container ls -a -q)` as it gives back all the container Id's, `rm` will remove one by one. As we know `rm` container doesn't remove the running containers, so we force it to do using `docker container rm -f $()`.
-  When we launch the docker container will get into the container, but when you want to lauch multiple container we need to use different terminals. In order to avoid it we can exit the present container and launch another (but the container will get shutdown), so we can apply this trick **detach container** using `left-ctl+p+q`, these makes we come out of container by detaching it rather than shutdown. If you want to go in (back to previous container) use `docker attach <os-name>`.
-  `docker run -it  --name <abc>  <os-name>:<os-version>  <program-name>` - will the program and gives the output, programs can be ml models/python/linux commands, what ever it might be. (note the program should be in the container <os-name>)      
-  **Pipeline : install --> boot --> program --> shutdown --> teminate**, we apply this in docker too `docker run -it  --name <abc> --rm <os-name>:<os-version>  <program-name>` - will execute the program and teminates the container.


[2. Session](https://www.youtube.com/watch?v=YCIf4Aj7Uoc&feature=youtu.be)      
**Summary**  
-  
-  


[3. Session](https://www.youtube.com/watch?v=wmGgmaMmPEQ&feature=youtu.be)      
**Summary**  
-  
-  