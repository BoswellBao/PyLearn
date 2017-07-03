import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def autogeneration():
    driver = webdriver.Ie("C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe")
    driver.maximize_window()
    driver.get("http://192.168.1.201/Pages/Login/Login.php?")
    #登录
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_class_name("but").click()

    #进入保安管理
    time.sleep(5)
    mouse = driver.find_element_by_id("actionAlarmManage")
    ActionChains(driver).move_to_element(mouse)
    # driver.find_element_by_link_text("保安管理").click()
    driver.find_element_by_xpath("//a[contains(@href,SecurityManagement)]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//tr[0]/td[1]/tr[0]/td[1]")

if __name__ == "__main__":
    autogeneration()



