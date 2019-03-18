from appium import webdriver

desired_caps = {
    'platformName' : 'Android',
    'platformVersion': '5.1.1',
    'deviceName':'test',
    'appPackage' : 'com.ibox.calculators',
    'appActivity': '.CalculatorActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset' : True,
    'newCommandTimeout': 6000
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
try:
    res = driver.find_element_by_id('com.ibox.calculators:id/cv').find_elements_by_class_name('android.widget.TextView')[1].text

    if res != '0':
        driver.find_element_by_id('clear').click()
    driver.find_element_by_id('digit3').click()
    driver.find_element_by_id('plus').click()
    driver.find_element_by_id('digit9').click()
    driver.find_element_by_id('equal').click()
    driver.find_element_by_id('mul').click()
    driver.find_element_by_id('digit5').click()
    driver.find_element_by_id('equal').click()
    assert res == '60'
except:
    print(traceback.format_exc())

driver.quit()
