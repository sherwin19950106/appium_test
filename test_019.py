from appium import webdriver

desired_caps = {
    'platformName' : 'Android',
    'platformVersion': '5.1.1',
    'deviceName':'test',
    'appPackage' : 'com.sqauto',
    'appActivity': '.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset' : True,
    'newCommandTimeout': 6000
                }
list1 = []
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


first = driver.find_element_by_accessibility_id('songqin recommend')
second = driver.find_element_by_accessibility_id('cramp fast')

y1 = first.location['y']
y2 = second.location['y']
while True:
    driver.swipe(getSize()[0] / 2, y1 + 500, getSize()[0] / 2, y1)
    like = driver.find_elements_by_accessibility_id('best reputation')
    if like:
        driver.swipe(getSize()[0] / 2, like[0].location['y'], getSize()[0] / 2, y1,5000)
        break
eles = driver.find_elements_by_class_name('android.widget.TextView')
for i in range(len(eles)):
    if eles[i].text == '口碑最佳':
        print(eles[i].text+':')
        for x in range(1,10,2):
            print(eles[i+x].text)
