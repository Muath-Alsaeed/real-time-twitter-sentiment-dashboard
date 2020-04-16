'''from subprocess import *
import time
Popen('first_dat.py')
'''''

import subprocess
path = r"C:\Users\Gamer\Documents\tetst123"

tasks = ['oman_database.py','Kuwait_database.py',"saudi_database.py", 'Qatar_database.py','Emirates_database.py','Bahrain_database.py']
task_processes = [
    subprocess.Popen(r'python %s\%s' % (path, task), shell=True)
    for task
    in tasks
]
for task in task_processes:
    task.wait()