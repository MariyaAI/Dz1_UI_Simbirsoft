from allure import step
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from data.objects import Customer


class CustomersTable(BasePage):
    tbody = (By.XPATH, "//tbody")

    def root(self):
        return self._actions.find_element(self.tbody)

    @step
    def get_names_lengths(self, names: list) -> list[str]:
        return self.add_result_to_allure([len(e) for e in names])

    @step
    def get_customers(self) -> list[Customer]:
        text_table = list()
        trs = self.root().find_elements(By.XPATH, "//tr")
        for i in range(1, len(trs) + 1):
            tds = list()
            for td in self.root().find_elements(By.XPATH, f"(//tr)[{i}]//td"):
                tds.append(td.text)
            if i == 1:
                self.check_headers(tds)
            else:
                text_table.append(Customer(*tds))
        text_table
        return text_table

    @step
    def get_average(self, lengths: list):
        return self.add_result_to_allure(sum(lengths) / len(lengths))

    @step
    def get_differences(self, avg: float, lens: list) -> list[float]:
        return self.add_result_to_allure([abs(avg - e) for e in lens])

    @step
    def get_closest_index(self, diffs: list[float]) -> int:
        for i, d in enumerate(diffs):
            if d == min(diffs):
                closest_index = i
                return self.add_result_to_allure(closest_index)

    @step
    def get_customers_names(self) -> list[str]:
        return self.add_result_to_allure([e.first_name for e in self.get_customers()])

    @step
    def click_delete_by_index(self, row_index: int):
        self.root().find_element(
            By.XPATH, f"(//tr)[{row_index + 2}]//td[{5}]/button"
        ).click()

    @step
    def click_first_name(self):
        self.root().find_element(By.XPATH, f"(//tr)[{1}]//td[{1}]/a").click()
        self._actions.wait_for_seconds(0.25)

    @step
    def check_headers(self, tds: list):
        assert tds[0] == "First Name", "Заголовки таблицы не соответствуют ожидаемым"
        assert tds[1] == "Last Name", "Заголовки таблицы не соответствуют ожидаемым"
        assert tds[2] == "Post Code", "Заголовки таблицы не соответствуют ожидаемым"
        assert (
            tds[3] == "Account Number"
        ), "Заголовки таблицы не соответствуют ожидаемым"
        assert (
            tds[4] == "Delete Customer"
        ), "Заголовки таблицы не соответствуют ожидаемым"

    @step
    def check_name_not_in_customers_names(self, closest_index: int, names: list[str]):
        assert names[closest_index] not in self.get_customers_names()
