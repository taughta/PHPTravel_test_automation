from selenium import webdriver

# Defining browser. Also setting implicit wait to avoid timeout and maximizing the window.
current_browser = webdriver.Chrome()
current_browser.implicitly_wait(30)
current_browser.maximize_window()
current_browser.get('https://www.phptravels.net/')