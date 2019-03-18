from appium import webdriver
import traceback,time

desired_caps = {

    'platformName' : 'Android',
    'platformVersion': '9',
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
conunt = driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]').text
print(conunt)
if conunt != '0':
    driver.find_element_by_id('com.ibox.calculators:id/clear').click()
try:
    num3 = driver.find_element_by_id('com.ibox.calculators:id/digit3')
    num9 = driver.find_element_by_id('com.ibox.calculators:id/digit9')
    num5 = driver.find_element_by_id('com.ibox.calculators:id/digit5')
    plus = driver.find_element_by_id('com.ibox.calculators:id/plus')
    equal = driver.find_element_by_id('com.ibox.calculators:id/equal')
    mul = driver.find_element_by_id('com.ibox.calculators:id/mul')
    num3.click()
    plus.click()
    num9.click()
    equal.click()
    mul.click()
    num5.click()
    equal.click()
    time.sleep(2)
    print(conunt)
    if conunt == '60':
        print('pass')
    else:
        print('fail')
except:
    print(traceback.format_exc())

driver.quit()




