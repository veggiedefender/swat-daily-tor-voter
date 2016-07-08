from selenium import webdriver
from stem import Signal
from stem.control import Controller
import sys

root = "http://daily.swarthmore.edu/"
url = root + raw_input("URL:     " + root)
comment_id = raw_input("ID:      ")
limit =  int(raw_input("Number:  "))


service_args = [
    '--proxy=127.0.0.1:9050',
    '--proxy-type=socks5',
]

def newIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

driver = webdriver.PhantomJS()
driver.get(url)
updoots = driver.find_element_by_id("comment-weight-value-%s" % comment_id).text
print "Hold on a sec..."
print "Starting updoots:  %s\r" % updoots

for i in range(limit):
    newIP()

    driver = webdriver.PhantomJS(service_args=service_args)

    driver.get(url)
    elem = driver.find_element_by_css_selector('a[data-comment-id="%s"]' % comment_id)
    elem.click()

    updoots = driver.find_element_by_id("comment-weight-value-%s" % comment_id).text
    print "Current updoots:   %s\r" % updoots,
    sys.stdout.flush()
    driver.quit();
print ""