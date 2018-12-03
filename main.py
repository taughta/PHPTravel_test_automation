from current_browser import current_browser
from home_hotels import enter_random_hotel_or_city, checkin_datepicker_select_today, checkin_datepicker_select_random_future_date, \
     checkin_manual_input_today, checkin_manual_input_random_future, checkout_manual_input_random_future, travellers_select_random, \
     select_search_button, checkin_manual_input_custom, checkout_manual_input_custom, enter_custom_hotel_or_city, travellers_select_custom


current_browser.get("https://www.phptravels.net/")
enter_random_hotel_or_city()
#checkin_datepicker_select_today()
checkin_datepicker_select_random_future_date()
#checkin_manualInput_random_future()
checkout_manual_input_random_future()
#enter_custom_hotel_or_city('malaga')
#checkin_manualInput_custom('12/20/2020')
#checkout_manualInput_custom('11/23/2021')
#travellers_select_random()
#travellers_select_custom()
#select_search_button()