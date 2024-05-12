import data
from selenium import webdriver
import UrbanRoutesPage as urban_routes_pom


class TestUrbanRoutes:

  driver = None

  @classmethod
  def setup_class(cls):
    # Registro adicional habilitado para recuperar el código de confirmación del teléfono
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    cls.driver = webdriver.Chrome(options=chrome_options)
    cls.driver.maximize_window()
    cls.driver.delete_all_cookies()

  # Test insert data into to and from addresses
  def test_set_route(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.driver.get(data.urban_routes_url)
    test_driver.set_route(data.address_from, data.address_to)
    assert test_driver.get_from() == data.address_from
    assert test_driver.get_to() == data.address_to

  # Test select a customized cab, mark the comfort option
  def test_request_comfort_cab(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.request_comfort_cab()
    assert test_driver.get_selected_tariff() == "Comfort"

  # Test add a phone number, verify with received code
  def test_set_phone_number(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.set_phone_number(data.phone_number)
    assert test_driver.get_phone_in_field() == data.phone_number

  # Test add a credit card with it's card code
  def test_set_credit_card_number(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.set_credit_card_number(data.card_number, data.card_code)
    assert test_driver.get_card_optn() != None

  # Test add a message to driver, two icecreams, and enable blanket and handkerchief
  def test_fill_extra_options(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.fill_extra_options(data.message_for_driver)
    assert test_driver.get_current_icecream_count_value() == "2"
    assert test_driver.get_comment_for_driver_in_field() == data.message_for_driver
    assert test_driver.is_blanket_and_handkerchief_checkbox_selected() == True

  # Test book a trip with the specified options
  def test_book_trip(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.book_trip()
    assert test_driver.get_order_screen_title() == "Buscar automóvil"
    test_driver.wait_confirmation()
    assert "El conductor llegará en" in test_driver.get_order_screen_title()

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
