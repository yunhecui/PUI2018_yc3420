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
