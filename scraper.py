from selenium import webdriver
import time

query_keyword = ["Adarsh Jatia", "Ajitsingh Dhingra","Arun Chandrachudan PMP","Dipak Sharma","Monish Ahuja","Nikhil Chaturvedi","Nirav Mehta","Ramesh Ganesan","Sajjan Kedia"] 
print ('Enter the linkedin email')
email= "ayush7506@gmail.com"
print ("Enter the LinkedIn password")
password= "%Babul97"

#Open Chrome web 
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')

#Login bu username/password
email_box = driver.find_element_by_id('login-email')
email_box.send_keys(email)
pass_box = driver.find_element_by_id('login-password')
pass_box.send_keys(password)
submit_button = driver.find_element_by_id('login-submit')
submit_button.click()

time.sleep(1)

#Find Name and return
def getName(driver):
        nameXpath = "//h1[contains(@class, 'pv-top-card-section')]"
        time.sleep(10)
        name = driver.find_element_by_xpath(nameXpath).text
        return name

def getLocation(driver):
	nameXpath = "//h3[contains(@class, 'pv-top-card-section')]"
	loc = driver.find_element_by_xpath(nameXpath).text
	return loc

def getEducation(driver):
	nameXpath = "//span[contains(@class, 'pv-top-card-v2-section__school')]"
	edu = driver.find_element_by_xpath(nameXpath).text
	return edu

def getConnections(driver):
	nameXpath = "//span[contains(@class, 'pv-top-card-v2-section__connections')]"
	conn = driver.find_element_by_xpath(nameXpath).text
	return conn

def saveAsCSV(data):
	fileName = "linkedin_result.csv"
	f = open(fileName, "a")
        headers="Name,Location,Education,Connections\n"
	f.write(data + '\n')

#For each profile name in query_keywords, retrive name, education, experience and number of connections
for query in query_keyword:
	try:
		driver.get(
			'https://www.linkedin.com/search/results/index/?keywords=' + query)
		
		xpath = "(//span[text()='" + query + "'])[1]"
		#print (xpath)
		time.sleep(10)
		driver.find_element_by_xpath(xpath).click()
		data = ''
		try :
			name = getName(driver)
			print (name)
			data += name + ','
		except Exception as ex:
			data += '0,'
	
		try:
			loc = getLocation(driver)
			print(loc)
			data += loc + ','
		except Exception as ex:
			data += '0,'

		try:
			edu = getEducation(driver)
			print(edu)
			data += edu + ','
		except Exception as ex:
			data += '0,'

		try:
			conn = getConnections(driver)
			print(conn)
			data += conn + ','
		except Exception as ex:
			data += '0,'	
			
		print (data)
		saveAsCSV(data)
	except Exception as e:
		print("Exception in retrieving data" + e)



