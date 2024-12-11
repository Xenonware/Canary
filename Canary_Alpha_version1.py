import sys
import psutil
import keyboard
import logging
import time
import subprocess

#outline the read function later
#The idea is for the code to monitor system strain
#when strain exceeds 70% alert user
#When strain exceeds 90% ask user if they wish to continue
#If yes continue monitoring, if no, restrart system
#When strain exceeds 95% alert user that the canary has died and shutdown system
#Intended to protect system from longterm damage, also just a gimmick program

def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])

def typewrite(text):
    for char in text:
        print(char, end="", flush=True)  # Print the character without a newline
        time.sleep(0.09)  # Adjust the delay as desired

typewrite("Welcome to Canary, Press and Hold ESC key to quit as soon as boot is complete.")
time.sleep(2)
typewrite("\nPlease wait")
typewrite("....................................")
typewrite("\nProgram boot complete, monitoring system.")


cpu_percent = psutil.cpu_percent(interval=1)

# Range for first warning
low_range = range(1,10) #actual is 1,70
# Range for Second warning and possible restart
mid_range = range(11,20) #actual is 70,90
# Range for complete shutdown
high_range = range(21,30) #actual is 91,100

if cpu_percent in low_range:
    low_range = True

running = True #this keeps the code from shitting the bed

def CPU_usage():
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    


def lc(): #stands for low check
    if cpu_percent >= 100: #checks to see is CPU usage is a less than safe amount, and notifies user
        time.sleep(5)
        print("CPU strain is high, Please be nice to your PC!")
    else:
        pass

def mc(): #stands for mid check
    if cpu_percent >= 10:
        typewrite("\nCPU usage reaching dangerous levels, do you want to restart?")
        answer = input("Y or N?")
        if answer == "Y":
            restart_computer()
        elif answer == "N":
            pass

        else:
            print("Please answer with Y or N")

# Memory usage
mem = psutil.virtual_memory()

while running:
    cpu_percent in low_range


    CPU_usage()

    lc()

    mc()
    
    if cpu_percent >= 10: #checks to see is CPU usage is a less than safe amount, and notifies user
        time.sleep(1)
        print("CPU strain is high, Please be nice to your PC!")

    if keyboard.is_pressed('esc'): #allows the user to end the program
        typewrite("\nEnding program, Thank you for using Canary.")
        sys.exit()











