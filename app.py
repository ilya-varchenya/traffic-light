import os
import subprocess
from matrix_lite import led
from time import sleep


def get_container_id(container_name):
 	command = "ssh ubuntu@demo.qaprosoft.com docker ps -aqf 'name={}'".format(container_name)
 	return os.popen(command).read()


def get_container_status(container_name):
	container_id = get_container_id(container_name)
	command = 'ssh ubuntu@demo.qaprosoft.com docker inspect --format={{.State.Status}} ' + container_id
	return os.popen(command).read()


def set_led_status(container_status):
	# container status can be: created, restatring, running, removing, pused, exited, dead
	if container_status == 'running':
		led.set('green')
	else:
		led.set('red')


if __name__=="__main__":
	container_name = 'jenkins-master'

	try:
		while True:
			container_status = get_container_status(container_name).strip()
			set_led_status(container_status)
			print(container_status)
			sleep(5)
	except KeyboardInterrupt:
		led.set()
		exit()	
