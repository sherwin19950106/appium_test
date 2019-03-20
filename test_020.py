from appium import webdriver

desired_caps = {
    'platformName' : 'Android',
    'platformVersion': '5.1.1',
    'deviceName':'test',
    'appPackage' : 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset' : True,
    'newCommandTimeout': 6000
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
ele = driver.find_elements_by_id('tv_title')[0]
title1 = ele.text
ele.click()
title2 = driver.find_element_by_id('tv_title').text
if title2 == title1:
    print('pass')
else:
    print('fail')
driver.press_keycode(4)
print(driver.contexts)
if len(driver.contexts) == 1:
    print('pass')
else:
    print('fail')
