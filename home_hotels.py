from current_browser import current_browser
from random import randint
from datetime import datetime, timedelta
import time

# Defining buttons locator values. Attribute type is in comment, keep it up to date!
buttons = {
    'hotel/city': 'select2-choice',  # CLASS
    'hotel/city_clicked': 'select2-input',  # CLASS
    'checkin': 'checkin',  # NAME
    'checkout': 'checkout',  # NAME
    'travellersInput': 'travellersInput',  # ID
    'search': "//button[@type='submit']"  # XPATH
}

# Test locations input values
locations_hotels = ('urm', 'sey', 'okl', 'Aspen', 'black', 'white ', 'ugh', 'great ')

# Month values as defined in DOM
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


# Enters a random destination
def enter_random_hotel_or_city():
    current_browser.find_element_by_class_name(buttons['hotel/city']).click()
    current_browser.find_element_by_class_name(buttons['hotel/city_clicked']).send_keys(
        locations_hotels[randint(0, len(locations_hotels)-1)]
    )
    search_result = current_browser.find_element_by_xpath("//span[@class='select2-match']")
    search_result.click()


def enter_custom_hotel_or_city(custom_destination):
    current_browser.find_element_by_class_name(buttons['hotel/city']).click()
    current_browser.find_element_by_class_name(buttons['hotel/city_clicked']).send_keys(custom_destination)
    search_result = current_browser.find_element_by_xpath("//span[@class='select2-match']")
    search_result.click()


def checkin_datepicker_select_today():
    current_browser.find_element_by_name(buttons['checkin']).click()
    today_button = current_browser.find_element_by_xpath("//td[@class='day  active']")
    today_button.click()


def checkin_datepicker_select_tomorrow():
    current_browser.find_element_by_name(buttons['checkin']).click()
    if current_browser.find_element_by_xpath("//td[@class='day ']").size() != 0:
        future_day_button = current_browser.find_element_by_xpath("//td[@class='day ']")
        future_day_button.click()
    else:
        today_button = current_browser.find_element_by_xpath("//td[@class='day  active']")
        today_button.click()


def checkin_datepicker_select_random_future_date():
    current_browser.find_element_by_name(buttons['checkin']).click()
    date_range_switcher = current_browser.find_element_by_xpath(
        "//div[@class='datepicker dropdown-menu'][1]/div[@class='datepicker-days']//th[@class='switch']"
    )
    date_range_switcher.click()
    next_button = current_browser.find_element_by_xpath(
        "//div[@class='datepicker dropdown-menu'][1]/div[@class='datepicker-months']//th[@class='next']"
    )
    for i in range(randint(1, 6)):
        next_button.click()
    random_month = current_browser.find_element_by_xpath(
        "//div[@class='datepicker dropdown-menu']/div[@class='datepicker-months']//span[@class='month']"
    )
    random_month.click()


def checkin_manual_input_today():
    current_browser.find_element_by_name(buttons['checkin']).click()
    current_browser.find_element_by_name(buttons['checkin']).send_keys(datetime.today().strftime('%m/%d/%Y'))


def checkin_manual_input_custom(checkin_custom_date):
    current_browser.find_element_by_name(buttons['checkin']).click()
    current_browser.find_element_by_name(buttons['checkin']).send_keys(checkin_custom_date)


def checkin_manual_input_random_future():
    random_future_date = (datetime.today()+timedelta(days=randint(1, 1000))).strftime('%m/%d/%Y')
    current_browser.find_element_by_name(buttons['checkin']).click()
    current_browser.find_element_by_name(buttons['checkin']).send_keys(random_future_date)


# Checks the entered
def checkout_manual_input_random_future():
    entered_checkin_date = datetime.strptime(current_browser.find_element_by_name(
        buttons['checkin']).get_attribute('value'), '%m/%d/%Y'
    )
    current_browser.find_element_by_name(buttons['checkout']).click()
    current_browser.find_element_by_name(buttons['checkout']).send_keys(
        datetime.strftime(entered_checkin_date + timedelta(days=(randint(1, 1825))), '%m/%d/%Y')
    )


def checkout_manual_input_custom(checkout_custom_date):
    current_browser.find_element_by_name(buttons['checkout']).click()
    current_browser.find_element_by_name(buttons['checkout']).send_keys(checkout_custom_date)


def travellers_select_random():
    current_browser.find_element_by_id(buttons['travellersInput']).click()
    for adlts in range(randint(1, 10)):
        current_browser.find_element_by_id('adultPlusBtn').click()
    for chldrn in range(randint(1, 10)):
        current_browser.find_element_by_id('childPlusBtn').click()


def travellers_select_custom(adults, children):
    current_browser.find_element_by_id(buttons['travellersInput']).click()
    for adlts in range(adults):
        current_browser.find_element_by_id('adultPlusBtn').click()
    for chldrn in range(children):
        current_browser.find_element_by_id('childPlusBtn').click()


def select_search_button():
    current_browser.find_element_by_xpath(buttons['search']).click()
