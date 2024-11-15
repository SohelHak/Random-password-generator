# Importing Modules
import random
import os 

from time import sleep
from colorama import Fore, Style

# Pre Defined Variables
# 1. colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN

resetColor = Style.RESET_ALL

options = f"""
[{red}1{resetColor}] Generate Password
[{red}2{resetColor}] About 
[{red}0{resetColor}] exit
"""

generatePass_options = f"""{cyan}- Select Type of the Password -{resetColor}
[{red}1{resetColor}] Generate Random String Password
[{red}2{resetColor}] Generate Random PIN Password
[{red}3{resetColor}] Generate Random Password With Symbols, Integer, String
[{red}0{resetColor}] exit
"""

PIN_Length = f"""{cyan}- Select Length of the Password -{resetColor}
[{red}1{resetColor}] 4 Digit PIN
[{red}2{resetColor}] 6 Digit PIN
[{red}3{resetColor}] 8 Digit PIN
[{red}4{resetColor}] 10 Digit PIN
[{red}0{resetColor}] exit
"""

Length = f"""{cyan}- Select Length of the Password -{resetColor}
[{red}1{resetColor}] 6
[{red}2{resetColor}] 8
[{red}3{resetColor}] 12
[{red}4{resetColor}] 16
[{red}0{resetColor}] exit
"""

Numbers = [1,2,3,4,5,6,7,8,9,0]

runningSystem = True

# Functions
def clear():
	os.system("clear")

def generate_password_str(length):
	# Generate a String Password of the specified length
    Password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=length))
    clear()
    print(f"{resetColor}Generated Password: {green}{Password}{resetColor}")
    print(f"{red}\n\nNote once you press ENTER this Password will clear so note this Password before press ENTER!{resetColor}")
    input()
    clear()

def generate_password_PIN(length):
    # Generate a PIN of the specified length
    pin = ''.join(random.choices("0123456789", k=length))
    clear()
    print(f"{resetColor}Generated PIN: {green}{pin}{resetColor}")
    print(f"{red}\n\nNote once you press ENTER this PIN will clear so note this PIN before press ENTER!{resetColor}")
    input()
    clear()
def generate_password_with_symbol_int_str(length):
	# Generate a String Password of the specified length
    Password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@$(){}[]#&^", k=length))
    clear()
    print(f"{resetColor}Generated Password: {green}{Password}{resetColor}")
    print(f"{red}\n\nNote once you press ENTER this Password will clear so note this Password before press ENTER!{resetColor}")
    input()
    clear()

def main():
	clear()
	while runningSystem:
		try:
			print(f"{yellow}Welcome to Password Generator{resetColor}")
			print(f"By - {cyan}CodeWithSohel{resetColor}")
			print(options)
			home_user = int(input(f"Select: {cyan}"))
			print(Style.RESET_ALL)
			if home_user == 1:
				clear()
				print(generatePass_options)
				GeneratePass_user = int(input(f"Select: {cyan}"))
				if GeneratePass_user == 1:
					clear()
					print(Length)
					length = int(input(f"Select: {cyan}"))
					if length == 1:
						generate_password_str(6)
					
					elif length == 2:
						generate_password_str(8)
					
					elif length == 3:
						generate_password_str(12)
					
					elif length == 4:
						generate_password_str(16)
					
					elif length == 0:
						main()
						
					else:
						clear()
						print(f"{red}Option Not Available!{resetColor}")
						sleep(1)
						clear()
				
				elif GeneratePass_user == 2:
					clear()
					print(PIN_Length)
					length = int(input(f"Select: {cyan}"))
					if length == 1:
						generate_password_PIN(4)
					
					elif length == 2:
						generate_password_PIN(6)
					
					elif length == 3:
						generate_password_PIN(8)
					
					elif length == 4:
						generate_password_PIN(10)
					
					elif length == 0:
						main()
						
					else:
						clear()
						print(f"{red}Option Not Available!{resetColor}")
						sleep(1)
						clear()
					
				elif GeneratePass_user == 3:
					clear()
					print(Length)
					length = int(input(f"Select: {cyan}"))
					if length == 1:
						generate_password_with_symbol_int_str(6)
					
					elif length == 2:
						generate_password_with_symbol_int_str(8)
					
					elif length == 3:
						generate_password_with_symbol_int_str(12)
					
					elif length == 4:
						generate_password_with_symbol_int_str(16)
					
					elif length == 0:
						main()
				
				elif GeneratePass_user == 0:
					main()
					
				else:
					clear()
					print(f"{red}Option Not Available!{resetColor}")
					sleep(1)
					clear()
					
			elif home_user == 2:
				clear()
				print(f"{cyan}This program generate random passwords there are 3 categories in this this program to create password{resetColor}\n[{red}1{resetColor}] Generate Random String Password\n[{red}2{resetColor}] Generate Random PIN Password\n[{red}3{resetColor}] Generate Random Password With Symbols, Integer, String\nTry this program and give feedback on my github page if you\n\n\n{cyan}\t\t\t\t\t!!!NOTE!!!!\n{red}If your phone will lock by using my program's PIN/Password then I am not responsible for that, first you note the PIN/Password the use this, because there is no backup of the generated PIN/Password{resetColor}")
				input(f"\nPress {cyan}ENTER{resetColor} to back....")
				clear()

			elif home_user == 0:
				clear()
				for i in range(1, 4):
					print(f"Program close in 3 seconds.... {red}{i}{resetColor}")
					sleep(1)
					clear()
				clear()
				print(f"{cyan}THANK YOU FOR USING THIS PROJECT...{resetColor}")
				exit(0)
			else:
				print(f"{red}Option Not Available!{resetColor}")
				sleep(1)
				clear()
			
		except ValueError:
			clear()
			print(f"{red}Invalid Enter!{yellow}\nPlease Enter only in number!{resetColor}")
			sleep(2)
			clear()
main()	
		
