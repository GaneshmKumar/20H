import sys
import time
import os
import json
import getpass
import platform
from termcolor import colored


platform = platform.system()
def cls():
	if platform == 'Linux':
		os.system('clear')
	elif platform == 'Windows':
		os.system('cls')
		
def read_file(file_name):
	with open(file_name, 'r') as json_file:
		return json.load(json_file)

def write_file(file_name, tasks):
	with open(file_name, 'w') as json_file:
		json.dump(tasks, json_file)

def load_task_time(task):
	tasks = read_file(task_json)
	if task not in tasks:
		print colored("This task is not yet created", 'red')
		sys.exit()
	last_time = tasks[task]
	return last_time

def update_task(task, new_time):
	tasks = read_file(task_json)
	tasks[task] = new_time
	write_file(task_json, tasks)


def display_tasks():
	tasks = read_file(task_json)
	if tasks == {}:
		print colored("No tasks available", "red")
		return
	i = 1
	for key in tasks:
		print colored(str(i), 'yellow') + " " + colored(key, 'green') + " " + colored(tasks[key], 'blue')
		i += 1

def completed_task(task):
	tasks = read_file(task_json)
	del tasks[task]
	write_file(task_json, tasks)

def twenty_hours(hr, mi, sec, task):
	while(1):
		try:
			sys.stdout.write("\r")

			if(sec == '60'):
				sec = '00'
				mi = str(int(mi) + 1)

			if(mi == '60'):
				mi = '00'
				hr = str(int(hr) + 1)
				#print hr
			if(hr == '20'):
				print 'You have completed learning ' +colored(task, 'green')+ ' for ' + colored(hr+' hours '+mi+' minutes and '+sec+' seconds', 'green')
				completed_task(task)
				sys.exit()
			sec = str(int(sec) + 1)
			if len(hr) == 1:
				hr = '0' + hr
			if len(mi) == 1:
				mi = '0' + mi
			if len(sec) == 1:
				sec = '0' + sec
			sys.stdout.write(colored(colored(task, 'yellow') + ' ' + hr+':'+mi+':'+sec, 'green'))
			sys.stdout.flush()
			time.sleep(1)
		except KeyboardInterrupt:
			try:
				cls()
				print colored("Press CTRL+C to Pause and Press C to Continue", 'cyan')
				print colored('Paused', 'yellow')
				x = raw_input()
				if(x == 'c'):
					cls()
					print colored("Press CTRL+C to Pause and Press C to Continue", 'cyan')
					print colored('\nResuming...', 'yellow')
					time.sleep(1)
					cls()
					print colored("Press CTRL+C to Pause and Press C to Continue", 'cyan')
					continue
			except KeyboardInterrupt:
				cls()
				print 'You have learned ' + colored(task, 'yellow')+ ' for ' + colored(hr+' hours '+mi+' minutes and '+sec+' seconds', 'yellow')
				print colored('Bye...', 'green')
				new_time = hr + ':' + mi + ':' + sec
				update_task(task, new_time)
				break


def initial_screen():
	cls()
	print colored("Press CTRL+C to Pause and Press C to Continue", 'cyan')

def createJSON(task_json, task_folder):
	'''user = getpass.getuser()
	json_path = '/home/'+user+'/20H/task.json'''
	if not os.path.exists(task_json):
		os.system('mkdir ' + task_folder)
		with open(task_json, 'w') as json_file:
			json.dump({}, json_file)

def main():
	flag = sys.argv[1]
	if flag == '-d':
		display_tasks()

	elif flag == '-n':
		task = sys.argv[2]
		initial_screen()
		tasks = read_file(task_json)
		if task in tasks:
			print colored("You already have a task named " + colored(task, "yellow"), "red")
			option = raw_input(colored("Do you want to overwrite (y/n): "))
			if option == 'y' or option == 'Y':
				tasks[task] = '00:00:00'
				write_file(task_json, tasks)
			elif option == 'n' or option == 'N':
				sys.exit()
			else:
				print colored("Invalid Option", "red")
				sys.exit()
		else:
			tasks = read_file(task_json)
			tasks[task] = '00:00:00'
			write_file(task_json, tasks)
		initial_screen()
		twenty_hours('00', '00', '00', task)

	elif flag == '-l':
		task = sys.argv[2]
		last_time = load_task_time(task)
		hms = last_time.split(':')
		cls()
		print colored("Press CTRL+C to Pause and Press C to Continue", 'cyan')
		twenty_hours(hms[0], hms[1], hms[2], task)

if platform == 'Linux':
	task_folder =  '/home/' + getpass.getuser() + '/20H'
	task_json = task_folder + '/task.json'
elif platform == 'Windows':
	task_folder = 'C:\\Users\\' + getpass.getuser() + '\\20H'
	task_json = task_folder + '/task.json'
createJSON(task_json, task_folder)
#main()
