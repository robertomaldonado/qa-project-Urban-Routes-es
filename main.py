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

  def test_set_route(self):
    self.setup_class()
    self.driver.get(data.urban_routes_url)
    driver_test_route = urban_routes_pom.UrbanRoutesPage(self.driver)
    driver_test_route.wait_for_load_address_input_field()
    driver_test_route.set_route(data.address_from, data.address_to)
    assert driver_test_route.get_from() == data.address_from
    assert driver_test_route.get_to() == data.address_to
    self.teardown_class()

  def test_set_extra_options(self):
    self.setup_class()
    driver_test_extra_opts = urban_routes_pom.UrbanRoutesPage(self.driver)
    driver_test_extra_opts.driver.get(data.urban_routes_url)
    time.sleep(0.5)
    driver_test_extra_opts.set_route(data.address_from, data.address_to)
    time.sleep(0.5)
    driver_test_extra_opts.request_comfort_cab()
    time.sleep(0.5)
    driver_test_extra_opts.insert_comment_for_driver(data.message_for_driver)
    time.sleep(0.5)
    driver_test_extra_opts.select_cloth_and_napkins()
    time.sleep(0.5)
    driver_test_extra_opts.select_add_icecream()
    time.sleep(0.5)
    driver_test_extra_opts.select_add_icecream()
    time.sleep(0.5)
    self.teardown_class()

  def test_set_phone(self):
    self.setup_class()
    driver_test_phone = urban_routes_pom.UrbanRoutesPage(self.driver)
    driver_test_phone.driver.get(data.urban_routes_url)
    time.sleep(0.5)
    driver_test_phone.set_route(data.address_from, data.address_to)
    time.sleep(0.5)
    driver_test_phone.request_comfort_cab()
    time.sleep(0.5)
    driver_test_phone.set_phone_number()
    time.sleep(0.5)
    self.teardown_class()

  def test_set_credit_card(self):
    self.setup_class()
    driver_test_credit_card = urban_routes_pom.UrbanRoutesPage(self.driver)
    driver_test_credit_card.driver.get(data.urban_routes_url)
    time.sleep(0.5)
    driver_test_credit_card.set_route(data.address_from, data.address_to)
    time.sleep(0.5)
    driver_test_credit_card.request_comfort_cab()
    time.sleep(0.5)
    driver_test_credit_card.set_credit_card_number()
    time.sleep(0.5)
    self.teardown_class()

  def test_complete_workflow_cab_request(self):
    self.setup_class()
    driver_complete_test = urban_routes_pom.UrbanRoutesPage(self.driver)
    driver_complete_test.driver.get(data.urban_routes_url)
    time.sleep(0.5)
    driver_complete_test.set_route(data.address_from, data.address_to)
    time.sleep(0.5)
    driver_complete_test.request_comfort_cab()
    time.sleep(0.5)
    driver_complete_test.set_phone_number()
    time.sleep(0.5)
    driver_complete_test.set_credit_card_number()
    time.sleep(0.5)
    driver_complete_test.fill_extra_options(data.message_for_driver)
    time.sleep(5)
    driver_complete_test.book_trip()
    time.sleep(5)
    self.teardown_class()

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
