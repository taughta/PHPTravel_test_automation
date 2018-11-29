from current_browser import current_browser
from random import randint

# Defining buttons locator values. Attribute type is in comment, keep it up to date!
buttons = {
    'hotel/city': 'select2-choice',  # class
    'hotel/city_clicked': 'select2-input',  # class
    'checkin': 'checkin',  # name
    'checkout': 'checkout',  # name
    'travellersInput': 'travellersInput',  # id
    'search': "//button[@type='submit']"  # xpath
}

# Test locations input values
locations_hotels = ('urm', 'sey', 'okl', 'Aspen', 'black', 'white ', 'ugh', 'great ')

# Defining buttons. This uses the 'select_button' function and the button locator arrays so it is future proof.
hp_hotels_hotel_city_unclicked = current_browser.find_element_by_class_name(buttons['hotel/city'])
hp_hotels_hotel_city_clicked = current_browser.find_element_by_class_name(buttons['hotel/city_clicked'])
hp_hotels_checkin = current_browser.find_element_by_name(buttons['checkin'])
hp_hotels_checkout = current_browser.find_element_by_name(buttons['checkout'])
hp_hotels_travellersInput = current_browser.find_element_by_id(buttons['travellersInput'])
hp_hotels_search = current_browser.find_element_by_xpath(buttons['search'])


def enter_hotel_or_city():
    hp_hotels_hotel_city_unclicked.click()
    hp_hotels_hotel_city_clicked.send_keys(locations_hotels[randint(0,len(locations_hotels)-1)])
    hp_hotels_search_result = current_browser.find_element_by_xpath("//span[@class='select2-match']")
    hp_hotels_search_result.click()


def checkin_datepicker_select_today():


def checkin_datepicker_select_random_day_actual_month():


def checkin_datepicker_select_random_future_date():


def checkin_manualInput_today():


def



# Home/Hotels/Check in
hp_hotels_checkin.click()