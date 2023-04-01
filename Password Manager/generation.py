
from tkinter import *
from tkinter.ttk import *
import random

def low(entry, var1, var): 
	entry.delete(0, END) 

	# Get the length of passowrd 
	length = var1.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 


	if var.get() == 1: # Low strength
		for i in range(0, length): password = password + random.choice(lower) 
		return password 

	elif var.get() == 0: # Medium srength
		for i in range(0, length): password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	elif var.get() == 3: # High strength
		for i in range(0, length): password = password + random.choice(digits) 
		return password
	else: 
		print("Wrong option selected")