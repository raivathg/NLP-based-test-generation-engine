import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.common.by import By
from os.path import exists

#This will give me the entire string except first word
def reg1(line):
	first_word= line.partition(' ')[0]	
	m = ' '.join(line.split()[1:])
	return m.strip()

#returns first word of sentence
def first_word(line):
	return line.partition(' ')[0]

#This will give me the entire string between two words
def reg_between(line,a,b):
	if b:
		reg = re.escape(a) + r".*" + re.escape(b)
		string = re.findall(reg, line)[0]
		return string[len(a):-len(b)].strip()

#this will give string after String a till end
def reg_after(line,a):
	reg = re.escape(a) + r".*" 
	string = re.findall(reg, line)[0]
	return string[len(a):].strip()



def browse(file):
	chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
	driver = webdriver.Chrome(executable_path=chrome_path)
	driver.get(file[0])
	time.sleep(2)

	def return_label(input):
		try:
			return driver.find_element(By.XPATH, '//button[text()= "'+input+'"]')
		except:
			pass			
		
		try:
			return driver.find_element(By.XPATH, '//span[text()= "'+input+'"]')
		except:
			pass	

		try:
			return driver.find_element(By.XPATH, '//input[@title="'+input+'"]')
		except:
			pass	

		try:
			return driver.find_element(By.XPATH, '//textarea[@placeholder="'+input+'"]')
		except:
			pass

		return

	def click(input):
		print(input)
		param1 = reg1(input)
		# flag = 1
		# # try:
		# # 	label = driver.find_element(By.XPATH, '//button[text()= "'+param1+'"]')
		# # 	flag=0
		# # 	# print('this is 1')
		# # 	# print('flag = '+flag)
		# # except:
		# # 	pass
		# if (driver.find_element(By.XPATH, '//button[text()= "'+param1+'"]')):
		# 	label = driver.find_element(By.XPATH, '//button[text()= "'+param1+'"]')
		# 	flag = 0
		# if flag==1:
		# 	try:
		#   		label = driver.find_element(By.XPATH, '//button/span[text()= "'+param1+'"]')
		#   		flag =0 
		#   		# print('-----------------------------------------------')
		#   		# print('this is working')
		#   		# print(label)
		# 	except:
		#   		pass

	  	# print(label.get_attribute('class'))  
		label = return_label(param1)
		label.click()
		time.sleep(3)
		return

	def type(input):
		print(input)
		param1 = reg_between(input,'Type ',' as ')
		param2 = reg_after(input,' as ')
		# flag = 1
		# if flag == 1:
		# 	try:
		# 		label = driver.find_element(By.XPATH, '//input[@title="'+param1+'"]')
		# 		flag = 0
		# 	except:
		# 		pass

		# # print('in betweeeeeeeennnnnnn')
		# # print(input)
		# if flag == 1:
		# 	try:
		# 		label = driver.find_element(By.XPATH, '//textarea[@placeholder="'+param1+'"]')
		# 		# label = driver.find_element(By.XPATH, '//*[@id="ember553"]/div/div[1]/textarea')
		# 		flag=0
		# 	except Exception as e:
		# 		if hasattr(e, 'message'):
		# 			print(e.message)
		# 		else:
		# 			print(e)
		# 		pass

		label = return_label(param1)
		label.send_keys(param2)
		time.sleep(1)
		return

	def wait(input):
		param1 = first_word(input)
		param2 = reg_after(input,param1)
		time.sleep(int(param2,10))

	for input in file:
		if(input.partition(' ')[0]=='click' or input.partition(' ')[0]=='Click'):
			click(input)
		if(input.partition(' ')[0]=='type' or input.partition(' ')[0]=='Type'):
			type(input)
		if(input.partition(' ')[0]=='wait' or input.partition(' ')[0]=='Wait'):
			wait(input)
  
	# time.sleep(10)
	driver.close()

with open('login', 'r') as reader:
	file= reader.readlines()
browse(file)
