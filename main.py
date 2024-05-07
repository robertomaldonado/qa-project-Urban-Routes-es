import data
import time
from selenium import webdriver
import UrbanRoutesPage as urban_routes_pom


class TestUrbanRoutes:

  driver = None

  @classmethod
  def setup_class(cls):
    # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    cls.driver = webdriver.Chrome(options=chrome_options)
    cls.driver.maximize_window()
    cls.driver.delete_all_cookies()

  def test_complete_workflow_cab_request(self):
    test_driver = urban_routes_pom.UrbanRoutesPage(self.driver)
    test_driver.driver.get(data.urban_routes_url)
    time.sleep(0.5)

    test_driver.set_route(data.address_from, data.address_to)
    time.sleep(0.5)
    assert test_driver.get_from() == data.address_from
    assert test_driver.get_to() == data.address_to
    time.sleep(0.5)

    test_driver.request_comfort_cab()
    time.sleep(0.5)
    assert test_driver.get_selected_tariff() == "Comfort"
    time.sleep(0.5)

    test_driver.set_phone_number()
    time.sleep(0.5)
    assert test_driver.get_phone() == data.phone_number
    time.sleep(0.5)

    test_driver.set_credit_card_number()
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)

    test_driver.fill_extra_options(data.message_for_driver)
    time.sleep(0.5)
    assert test_driver.get_icecream_count_value() == "2"
    time.sleep(0.5)

    test_driver.book_trip()
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
