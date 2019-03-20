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
driver.switch_to.context(driver.contexts[1])
driver.find_element_by_id('index-kw').send_keys('松勤\n')
driver.switch_to.context(driver.contexts[0])
driver.find_element_by_accessibility_id('通知').click()
driver.quit()