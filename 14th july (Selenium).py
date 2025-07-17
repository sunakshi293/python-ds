# from selenium import webdriver
# from selenium.webdriver.common.by  import By

# driver = webdriver.Firefox()
# driver.get("https://google.com")
 
# drive.close()
 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://quotes.toscrape.com/")

#Selectors 

'''
Class Name 

ID
NAME

Tag Name
Link Text 
Partial Link Text
CSS Selector
XPATH



'''


q = driver.find_element(By.CLASS_NAME,"author")
print( q.text)


# time.sleep(3)


# username = driver.find_element(By.NAME,"username")  # Google's search bar
# username.send_keys("Admin")  # Type in input
 

# password = driver.find_element(By.NAME,"password")  
# password.send_keys("admin@123")



# submit = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button")
# submit.click()




