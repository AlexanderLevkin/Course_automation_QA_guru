import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

# WITH OS PATH

current_dir = os.path.dirname(os.path.abspath(__file__))
tmp_dir = os.path.join(current_dir, 'tmp')

prefs = {
    'download.default_directory': tmp_dir,
    'download.prompt_for_download': False
}

'''
prefs = {
    'download.default_directory': 'D:\PycharmProjects\Course_automation_QA_guru\lesson_6_work_with_files',
    'download.prompt_for_download': False
}
'''
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(1)

assert os.path.getsize(os.path.join(tmp_dir, 'sampleFile.jpeg')) == 4096
os.remove(os.path.join(tmp_dir, 'sampleFile.jpeg'))
