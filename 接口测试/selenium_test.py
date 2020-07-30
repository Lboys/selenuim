from selenium.webdriver import ActionChains
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.heibaizhibo.com/')
browser.implicitly_wait(5)

browser.find_element_by_xpath("//div[@id='user']/div[1]/span[1]").click()

browser.switch_to_frame("")

browser.find_element_by_class_name("el-input__inner").send_keys("15900482450")

huakuai=browser.find_element_by_id("nc_1_n1z")

browser.find_element_by_xpath("//input[@placeholder='密码']").send_keys("mll121314")

browser.find_element_by_class_name("btn-theme").click()



time.sleep(1)
#browser.find_element_by_xpath('//*[@id="nc_1_n1z"]')

def get_track(distance):      # distance为传入的总距离
    # 移动轨迹
    track=[]
    # 当前位移
    current=0
    # 减速阈值
    mid=distance*4/5
    # 计算间隔
    t=0.2
    # 初速度
    v=1

    while current<distance:
        if current<mid:
            # 加速度为2
            a=4
        else:
            # 加速度为-2
            a=-3
        v0=v
        # 当前速度
        v=v0+a*t
        # 移动距离
        move=v0*t+1/2*a*t*t
        # 当前位移
        current+=move
        # 加入轨迹
        track.append(round(move))
    return track
def move_to_gap(slider,tracks):     # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(xoffset=x,yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(browser).release().perform()

if __name__ == '__main__':
    move_to_gap(huakuai,get_track(340))







#########百度输入框的定位方式##########
#通过id方式定位


'''
#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class name方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过xpath方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
############################################
'''
browser.find_element_by_id("su").click()
time.sleep(10)
browser.quit()