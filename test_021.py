from appium import webdriver

desired_caps = {
    'platformName' : 'Android',
    'platformVersion': '5.1.1',
    'deviceName':'test',
    'appPackage' : 'com.example.jcy.wvtest',
    'appActivity': '.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset' : True,
    'newCommandTimeout': 6000
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
print(driver.contexts)
driver.switch_to.content('WEBVIEW_com.example.jcy.wvtest')
