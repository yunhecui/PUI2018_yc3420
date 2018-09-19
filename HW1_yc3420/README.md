Setting up Environment Variables
===================
Step 1
-----------
create a folder in local machine called PUI2018 through the following command in local terminal
```bash
mkdir PUI2018
```
Step 2
-----------
open the bash profile through
```bash
nano .bash_profile
```
then scroll down to the bottom and add two lines of code there (DO NOT change any existed lines)
```bash
export PUI2018="~/PUI2018"
alias pui2018="cd $PUI2018"
```
your .bashrc should look similar like this
![image](https://github.com/yunhecui/PUI2018_yc3420/raw/master/images/PUI-wk1-1.png)

Step 3
-----------
to test your new environment variables, you can try the new commands in your local terminal 
your result should look as follows
![image](https://github.com/yunhecui/PUI2018_yc3420/raw/master/images/PUI-wk1-2.png)