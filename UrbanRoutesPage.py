import utilities as utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UrbanRoutesPage:
  from_field = (By.ID, 'from')
  to_field = (By.ID, 'to')
  request_cab_btn = (
      By.XPATH, "//div[@class='results-text']//button[@type='button']")
  comfort_optn = (By.XPATH, "//*[contains(text(),'Comfort')]")
  selected_tariff = (
      By.XPATH, "//div[@class='tariff-picker shown']//div[@class='tariff-cards']//div[@class='tcard active']//div[@class='tcard-title']")

  phone_btn = (By.CLASS_NAME, "np-button")
  phone_field = (By.CLASS_NAME, "np-text")
  add_phone_dialog = (By.ID, "phone")
  confirm_phone = (
      By.XPATH, "//div[@class='section active']//form//div[@class='buttons']//button[@type='submit']")
  confirmation_code_area = (By.ID, "code")
  confirm_code = (
      By.XPATH, "//div[@class='section active']//form//div[@class='buttons']//button[@type='submit']")

  payment_btn = (By.CLASS_NAME, "pp-button")
  credit_card_optn = (By.CLASS_NAME, "pp-plus")
  credit_card_number_field = (By.ID, "number")
  credit_card_code_field = (
      By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
  confirm_credit_card = (
      By.XPATH, "//div[@class='pp-buttons']//button[@type='submit']")
  close_payment_modal_btn = (
      By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//div[@class='section active']//button[@class='close-button section-close']")
  card_element_verify_if_exists = (
      By.XPATH, "//div[@class='pp-button filled']//img[@alt='card']")

  requirements_form_open = (
      By.XPATH, "//div[@class='form']//div[@class='reqs open']")
  comment_to_driver_field = (By.ID, "comment")
  blanket_and_handkerchief_slider = (
      By.XPATH, "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']")
  icecream_counter_plus = (
      By.XPATH, "//div[contains(text(),'Helado')]/..//div[@class='counter-plus']")
  icecream_counter_value = (
      By.XPATH, "//div[contains(text(),'Helado')]/..//div[@class='counter-value']")

  order_wait_screen = (
      By.XPATH, "//div[@class='order shown']")
  order_wait_screen_title = (
      By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-header-title']")
  trip_confirmation = (
      By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-number']")
  book_cab_btn = (By.CLASS_NAME, 'smart-button-main')

  def __init__(self, driver):
    self.driver = driver

  # Setter and getter for addresses fields
  def set_from(self, from_address):
    self.driver.find_element(*self.from_field).send_keys(from_address)

  def set_to(self, to_address):
    self.driver.find_element(*self.to_field).send_keys(to_address)

  def get_from(self):
    return self.driver.find_element(*self.from_field).get_property('value')

  def get_to(self):
    return self.driver.find_element(*self.to_field).get_property('value')

  def get_phone(self):
    return self.driver.find_element(*self.phone_field).text

  def get_card_optn(self):
    return self.driver.find_element(*self.card_element_verify_if_exists)

  def get_selected_tariff(self):
    return self.driver.find_element(*self.selected_tariff).get_attribute('innerHTML')

  def get_icecream_count_value(self):
    return self.driver.find_element(*self.icecream_counter_value).get_attribute('innerHTML')

  def get_comment_for_driver(self):
    return self.driver.find_element(*self.comment_to_driver_field).get_attribute('value')

  def get_order_screen_title(self):
    return self.driver.find_element(*self.order_wait_screen_title).get_attribute('innerText')

  # Selections related to cab selection
  def begin_cab_request_procedure(self):
    self.driver.find_element(*self.request_cab_btn).click()

  def select_comfort_opt(self):
    self.driver.find_element(*self.comfort_optn).click()

  # Enables a secondary window where users input data
  def enable_phone_input_dialog(self):
    self.driver.find_element(*self.phone_btn).click()

  def enable_payment_input_dialog(self):
    self.driver.find_element(*self.payment_btn).click()

  def enable_credit_card_input_dialog(self):
    self.driver.find_element(*self.credit_card_optn).click()

  # Fields interactions
  def insert_phone_to_dialog(self, phone_number):
    self.driver.find_element(*self.add_phone_dialog).send_keys(phone_number)

  def confirm_phone_click(self):
    self.driver.find_element(*self.confirm_phone).click()

  def insert_confirmation_code_to_dialog(self, confirmation_code):
    self.driver.find_element(
        *self.confirmation_code_area).send_keys(confirmation_code)

  def confirm_comfirmation_code_click(self):
    self.driver.find_element(*self.confirm_code).click()

  def insert_credit_card_number_to_field(self, cc_number):
    self.driver.find_element(
        *self.credit_card_number_field).send_keys(cc_number)

  def insert_credit_card_code_to_field(self, cc_code):
    self.driver.find_element(
        *self.credit_card_code_field).send_keys(cc_code)
    self.driver.find_element(
        *self.credit_card_code_field).send_keys(Keys.TAB)

  def click_confirm_credit_card(self):
    self.driver.find_element(
        *self.confirm_credit_card).click()

  def click_close_payment_modal(self):
    self.driver.find_element(*self.close_payment_modal_btn).click()

  def insert_comment_for_driver(self, message_for_driver):
    self.driver.find_element(
        *self.comment_to_driver_field).send_keys(message_for_driver)

  def select_cloth_and_napkins(self):
    self.driver.find_element(
        *self.blanket_and_handkerchief_slider).click()

  def select_add_icecream(self):
    self.driver.find_element(
        *self.icecream_counter_plus).click()

  def click_book_trip(self):
    self.driver.find_element(
        *self.book_cab_btn).click()

  # Combined steps to acomplish a user interaction

  def set_route(self, address_from, address_to):
    self.wait_for_load_address_input_field()
    self.set_from(address_from)
    self.set_to(address_to)

  def request_comfort_cab(self):
    self.wait_for_load_cab_btn()
    self.begin_cab_request_procedure()
    self.wait_for_load_comfort_optn()
    self.select_comfort_opt()

  def set_phone_number(self, phone_number):
    self.wait_for_load_phone_btn()
    self.enable_phone_input_dialog()
    self.wait_for_load_add_phone_dialog()
    self.insert_phone_to_dialog(phone_number)
    self.wait_for_load_confirm_phone()
    self.confirm_phone_click()

    code = utils.retrieve_phone_code(self.driver)
    self.wait_for_load_confirmation_code_area()
    self.insert_confirmation_code_to_dialog(code)
    self.wait_for_load_confirm_code()
    self.confirm_comfirmation_code_click()

  def set_credit_card_number(self, card_number, card_code):
    self.wait_for_load_payment_btn()
    self.enable_payment_input_dialog()
    self.wait_for_load_credit_card_optn()
    self.enable_credit_card_input_dialog()
    self.wait_for_load_credit_card_number_field()
    self.insert_credit_card_number_to_field(card_number)
    self.insert_credit_card_code_to_field(card_code)
    self.wait_for_load_confirm_credit_card()
    self.click_confirm_credit_card()
    self.wait_for_load_close_payment_modal_btn()
    self.click_close_payment_modal()

  def fill_extra_options(self, message_for_driver):
    self.wait_for_load_requirements_form_open()
    self.insert_comment_for_driver(message_for_driver)
    self.select_cloth_and_napkins()
    self.select_add_icecream()
    self.select_add_icecream()

  def book_trip(self):
    self.click_book_trip()

  #  Wait for fields to appear on page

  def wait_for_load_address_input_field(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.visibility_of_element_located(self.to_field))

  def wait_for_load_cab_btn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.request_cab_btn))

  def wait_for_load_comfort_optn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.comfort_optn))

  def wait_for_load_phone_btn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.phone_btn))

  def wait_for_load_add_phone_dialog(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.presence_of_element_located(self.add_phone_dialog))

  def wait_for_load_confirm_phone(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.confirm_phone))

  def wait_for_load_confirmation_code_area(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.presence_of_element_located(self.confirmation_code_area))

  def wait_for_load_confirm_code(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.confirm_code))

  def wait_for_load_payment_btn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.payment_btn))

  def wait_for_load_credit_card_optn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.credit_card_optn))

  def wait_for_load_credit_card_number_field(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.presence_of_element_located(self.credit_card_number_field))

  def wait_for_load_confirm_credit_card(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.confirm_credit_card))

  def wait_for_load_close_payment_modal_btn(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(self.close_payment_modal_btn))

  def wait_for_load_requirements_form_open(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.presence_of_element_located(self.requirements_form_open))

  def wait_for_load_order_wait_screen(self):
    WebDriverWait(self.driver, 3).until(
        expected_conditions.visibility_of_element_located(self.order_wait_screen))

  def wait_for_trip_confirmation(self):
    WebDriverWait(self.driver, 45).until(
        expected_conditions.visibility_of_element_located(self.trip_confirmation))
