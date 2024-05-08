import data
from selenium import webdriver
import UrbanRoutesPage as urban_routes_pom
import utilities as utils


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

  def test_complete_workflow_cab_request(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.driver.get(data.urban_routes_url)

    test_driver.set_route(data.address_from, data.address_to)
    assert test_driver.get_from() == data.address_from
    assert test_driver.get_to() == data.address_to

    test_driver.request_comfort_cab()
    assert test_driver.get_selected_tariff() == "Comfort"

    test_driver.set_phone_number(data.phone_number)
    assert test_driver.get_phone() == data.phone_number

    test_driver.set_credit_card_number(data.card_number, data.card_code)
    assert test_driver.get_card_optn() != None

    test_driver.fill_extra_options(data.message_for_driver)
    assert test_driver.get_icecream_count_value() == "2"
    assert test_driver.get_comment_for_driver() == data.message_for_driver
    assert test_driver.get_blanket_and_handkerchief_checkbox_status() == True

    test_driver.book_trip()
    assert test_driver.get_order_screen_title() == "Buscar automóvil"
    test_driver.wait_confirmation()
    assert "El conductor llegará en" in test_driver.get_order_screen_title()

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
