from appium import webdriver


# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
desired_caps['appActivity'] = '.activities.NavigationActivity'
# toast
desired_caps['automationName'] = 'Uiautomator2'
# 不要重置应用
desired_caps['noReset'] = True

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 返回
driver.press_keycode(4)

# 获取toast
# 再次点击即可退出
def find_toast():
    return driver.find_element_by_xpath("//*[contains(@text,'再次')]").text

print(find_toast())

