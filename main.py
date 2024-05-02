import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
  """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
  Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
  El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

  import json
  import time
  from selenium.common import WebDriverException
  code = None
  for i in range(10):
    try:
      logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
              and 'api/v1/number?number' in log.get("message")]
      for log in reversed(logs):
        message_data = json.loads(log)["message"]
        body = driver.execute_cdp_cmd('Network.getResponseBody',
                                      {'requestId': message_data["params"]["requestId"]})
        code = ''.join([x for x in body['body'] if x.isdigit()])
    except WebDriverException:
      time.sleep(1)
      continue
    if not code:
      raise Exception("No se encontró el código de confirmación del teléfono.\n"
                      "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return code


class UrbanRoutesPage:
  from_field = (By.ID, 'from')
  to_field = (By.ID, 'to')
  request_cab_btn = (By.XPATH, "//*[contains(text(),'Pedir un taxi')]")
  comfort_optn = (By.XPATH, "//*[contains(text(),'Comfort')]")
#   phone_btn = (By.XPATH, "//*[contains(text(),'Número de teléfono')]")
  phone_btn = (By.CLASS_NAME, "np-button")
  add_phone_dialog = (By.ID, "phone")
  confirm_phone = (By.XPATH, "//*[contains(text(),'Siguiente')]")

  def __init__(self, driver):
    self.driver = driver

  def set_from(self, from_address):
    self.driver.find_element(*self.from_field).send_keys(from_address)

  def set_to(self, to_address):
    self.driver.find_element(*self.to_field).send_keys(to_address)

  def get_from(self):
    return self.driver.find_element(*self.from_field).get_property('value')

  def get_to(self):
    return self.driver.find_element(*self.to_field).get_property('value')

  def request_cab_btn_click(self):
    self.driver.find_element(*self.request_cab_btn).click()

  def comfort_optn_click(self):
    self.driver.find_element(*self.comfort_optn).click()

  def phone_btn_click(self):
    self.driver.find_element(*self.phone_btn).click()

  def add_phone_to_dialog(self, phone_number):
    self.driver.find_element(*self.add_phone_dialog).send_keys(phone_number)

  def add_phone_confirm_click(self):
    self.driver.find_element(*self.confirm_phone).click()

  def set_route(self, address_from, address_to):
    self.set_from(address_from)
    self.set_to(address_to)
    time.sleep(2)
  # Espera a que aparezca el campo de direccion to

  def wait_for_load_home_page(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.visibility_of_element_located(self.to_field))


class TestUrbanRoutes:

  driver = None

  @classmethod
  def setup_class(cls):
    # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
    # from selenium.webdriver import DesiredCapabilities
    # capabilities = DesiredCapabilities.CHROME
    # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    # cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    options = ChromeOptions()
    cloud_options = {}
    cloud_options["goog:loggingPrefs"] = {'performance': 'ALL'}
    options.set_capability('cloud:options', cloud_options)
    cls.driver = webdriver.Chrome(options=options)

  def test_set_route(self):
    self.driver.get(data.urban_routes_url)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.wait_for_load_home_page()
    address_from = data.address_from
    address_to = data.address_to
    routes_page.set_route(address_from, address_to)
    assert routes_page.get_from() == address_from
    assert routes_page.get_to() == address_to

  def test_cab_request(self):
    self.driver.get(data.urban_routes_url)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.wait_for_load_home_page()
    routes_page.set_route(data.address_from, data.address_to)
    routes_page.request_cab_btn_click()
    time.sleep(1)
    routes_page.comfort_optn_click()
    time.sleep(1)
    routes_page.phone_btn_click()
    time.sleep(1)
    routes_page.add_phone_to_dialog(data.phone_number)
    time.sleep(1)
    routes_page.add_phone_confirm_click()
    time.sleep(1)
    code = retrieve_phone_code(self.driver.get(data.urban_routes_url))
    assert code != None

  @classmethod
  def teardown_class(cls):
    cls.driver.quit()
