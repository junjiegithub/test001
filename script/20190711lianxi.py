# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

url = "http://www.maiziedu.com/"
login_text = '登录'
account = 'maizi_test @ 139.com'
pwd = 'abc123456'


def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

def openBrower():
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

def openUrl(handle, url):
    handle.get(url)
    d.maximize_window()


def findElement(d, arg):
    if text_id in arg:
        ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    useEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    return useEle, pwdEle, loginEle


def sendVals(eletuple, arg):
    listkey = ['uname', 'pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear
        eletuple[i].send_keys(arg[key])
        i += 1
    eletuple[2].click()


def checkResult(d, text):
    try:
        d.find_element_by_link_text(text)
        print("Account And Pwd Error!")
    except:
        print("Account And Pwd Right!")


def login_test():
    d = openBrower()
    openUrl(d, url)
    ele_dict = {'text_id': login_text, 'userid': 'id_account_1', \
                'pwdid': 'id_password_1', 'loginid': 'login_btn'}

    account_dict = {'uname': account, 'pwd': pwd}
    ele_tuple = findElement(d, ele_dict)
    sendVals(ele_tuple, account_dict)
    checkResult(d, '该账号格式不正确')


if __name__ == '__main__':
    login_test()
