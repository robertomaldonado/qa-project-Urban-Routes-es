import time
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
  phone_btn = (By.CLASS_NAME, "np-button")
  add_phone_dialog = (By.ID, "phone")
  confirm_phone = (By.XPATH, "//*[contains(text(),'Siguiente')]")
  confirmation_code_area = (By.ID, "code")
  confirm_code = (By.XPATH, "//*[contains(text(),'Confirmar')]")

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

  def begin_cab_request_procedure(self):
    self.driver.find_element(*self.request_cab_btn).click()

  def select_comfort_opt(self):
    self.driver.find_element(*self.comfort_optn).click()

  def enable_phone_input_dialog(self):
    self.driver.find_element(*self.phone_btn).click()

  def insert_phone_to_dialog(self, phone_number):
    self.driver.find_element(*self.add_phone_dialog).send_keys(phone_number)

  def confirm_phone_click(self):
    self.driver.find_element(*self.confirm_phone).click()

  def insert_confirmation_code_to_dialog(self, confirmation_code):
    self.driver.find_element(
        *self.confirmation_code_area).send_keys(confirmation_code)

  def confirm_comfirmation_code_click(self):
    self.driver.find_element(*self.confirm_code).click()

  def set_route(self, address_from, address_to):
    self.set_from(address_from)
    self.set_to(address_to)
    time.sleep(1)

  def request_comfort_cab(self):
    self.wait_for_load_address_input_field()
    self.set_route(data.address_from, data.address_to)
    self.begin_cab_request_procedure()
    self.select_comfort_opt()

  def set_phone_number(self):
    self.enable_phone_input_dialog()
    time.sleep(0.5)
    self.insert_phone_to_dialog(data.phone_number)
    time.sleep(0.5)
    self.confirm_phone_click()
    time.sleep(0.5)
    code = retrieve_phone_code(self.driver)
    self.insert_confirmation_code_to_dialog(code)
    time.sleep(0.5)
    self.confirm_comfirmation_code_click()

  # Espera a que aparezca el campo de direccion hasta

  def wait_for_load_address_input_field(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.visibility_of_element_located(self.to_field))