# 20H
A simple python app based on the 20 Hour Rule

## Description
Before seeing about this app, let us understand something about the <a href="https://first20hours.com/">**20 HOUR RULE**</a>

This app let you to manage the learning task for 20 Hours

## Requirements ##
* python2
* termcolor

## Installation ##
``sudo python setup.py install``
[Make sure you are using python2]

## Usage ##
### To view all your tasks ###
``20H -d``

### To add new task ###
``20H -n new_task_name``

### To load an old task ###
``20H -l old_task_name``

## Example ##
``20H -n learn_angular_js``

``20H -l learn_node_js``

**If the task name has more than one word, you can separate them by '_' (underscore)**

## Uninstall ##
To uninstall 20H, execute the following line in your terminal

``sudo rm -rf /usr/local/bin/20H``


**NOTE:** Works on Linux only.
