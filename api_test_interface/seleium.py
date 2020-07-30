#coding=utf-8
#select下拉框处理
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#导入select方法
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
#隐式等待10秒
driver.implicitly_wait(10)
#鼠标移动到"设置"按钮
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
#点击"搜索设置"
driver.find_element_by_link_text("搜索设置").click()
#强制等待4秒，注意：这里使用隐式等待或显式等待都将无法获取元素
time.sleep(4)
#分两步，先定位下拉框，再点击选项
choice = driver.find_element_by_name("NR")
Select(choice).select_by_index(2)
time.sleep(2)
driver.find_element_by_xpath("//div[@id='gxszButton']/a[1]").click()
time.sleep(2)
driver.switch_to.alert.accept()
#跳转到百度首页后，进行搜索表
driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id('su').click()