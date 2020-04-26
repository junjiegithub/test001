#coding =utf-8
from  selenium import webdriver
import time


#网址《西城派出所》
url = 'http://183.196.128.194:9091/#"'

#用户名
account ='admin'
#密码
pwd ='x123456'



def login_test():     #登录测试
    d =webdriver.Chrome()           #打开浏览器
    d.get(url)                      #打开网址

    d.maximize_window()                 #浏览器最大化
    time.sleep(2)

    account_ele =d.find_element_by_name("UserName")
    account_ele.send_keys(account)

    pwd_ele=d.find_element_by_name("Password")
    pwd_ele.send_keys(pwd)
    time.sleep(2)
    d.find_element_by_xpath("/html/body/div[2]/div[2]/form/button").click()

    try:
        d.find_element_by_link_text("用户不存在")
        print("登录失败")

    except:
        print("登录成功")







if __name__ == '__main__':
    login_test()


