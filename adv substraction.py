#scripted by sincryptaayush
from colorama import Fore
from os import system 
system(' clear ')

banner=Fore.LIGHTBLUE_EX+'''                 __     ___    _  _____ _    _ 
     /\        /\\ \   / / |  | |/ ____| |  | |
    /  \      /  \\ \_/ /| |  | | (___ | |__| |
   / /\ \    / /\ \\   / | |  | |\___ \|  __  |
  / ____ \  / ____ \| |  | |__| |____) | |  | |
 /_/    \_\/_/    \_\_|   \____/|_____/|_|  |_|
                                               
                                               '''

print(banner)


def formula(sum1,sum2):
	return sum1 - sum2

aayush=int(input(Fore.YELLOW+' enter the count number of your question substraction ======> '))
print('\n')

op=[]
for i in range(1, aayush+1):
	samay=int(input(Fore.LIGHTMAGENTA_EX+f' enter your number {i} ----->  '))
	print('\n')
	shark=int(input(Fore.LIGHTMAGENTA_EX+f' enter your number {i} -----> '))
	print('\n')
	op.append(formula(samay,shark))
	print('\n')
	
sum=1
for i in op:
	print(Fore.RED+f' the numberset of your  {sum} answer is ----------> {i} \n')
	sum= sum+1