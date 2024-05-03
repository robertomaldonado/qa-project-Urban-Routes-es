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

  def test_set_route(self):
    self.driver.get(data.urban_routes_url)
    routes_page = urban_routes_pom.UrbanRoutesPage(self.driver)
    routes_page.wait_for_load_address_input_field()
    routes_page.set_route(data.address_from, data.address_to)
    assert routes_page.get_from() == data.address_from
    assert routes_page.get_to() == data.address_to

  def test_cab_request(self):
    self.driver.get(data.urban_routes_url)
    routes_page = urban_routes_pom.UrbanRoutesPage(self.driver)
    routes_page.request_comfort_cab()
    time.sleep(0.5)
    routes_page.set_phone_number()
    time.sleep(0.5)
    pass

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
