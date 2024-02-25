from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from data.objects import Customer
import random
from faker import Faker
from allure import step


class AddCustomerForm(BasePage):
    tbody = (By.XPATH, "//tbody")
    inp_first_name = (
        By.XPATH,
        '//label[text()="First Name :"]/following-sibling::input',
    )
    inp_last_name = (By.XPATH, '//label[text()="Last Name :"]/following-sibling::input')
    inp_post_code = (By.XPATH, '//label[text()="Post Code :"]/following-sibling::input')
    btn_add_customer = (By.XPATH, '//button[@value][text()="Add Customer"]')

    def root(self):
        return self._actions.find_element(self.tbody)

    def generate_digits(self, length) -> str:
        return "".join([str(random.randint(0, 9)) for _ in range(length)])

    def get_char(self, num: str) -> str:
        num = int(num) % 26
        return chr(num + 97)

    def get_first_name(self, post_code: str):
        pairs = ["".join(e) for e in zip(post_code[::2], post_code[1::2])]
        return "".join([self.get_char(p) for p in pairs])

    @step("generate_test_user")
    def generate_test_user(self) -> Customer:
        post_code = self.generate_digits(10)
        first_name = self.get_first_name(post_code)
        last_name = Faker(["En-Us"]).last_name()
        return self.add_result_to_allure(Customer(first_name, last_name, post_code))
