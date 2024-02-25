import allure
from pageobjects.provider import PobjectProvider


@allure.suite("Тест-кейс 'Сортировка'")
@allure.title("Тест-кейс 'Сортировка'")
def test_case_2(provider: PobjectProvider):
    page = provider.page_actions
    m_p = provider.manager_page
    c_s = provider.customers_table

    with allure.step("Подготовка, Тестовые данные"):
        m_p.navigate()

    with allure.step("1) Нажать на кнопку 'Customersэ"):
        page.click(m_p.btn_show_cust)

    with allure.step(
        "2) Открывается таблица клиентов, содержащая поля"
        "(First Name,Last Name,Post Code,Account Number,Delete Customer)"
    ):
        names_before = c_s.get_customers_names()

    with allure.step(
        "3) Нажать на поле 'First Name' и осуществить сортировку по имени"
    ):
        c_s.click_first_name()

    with allure.step("4) Убедиться, что сортировка осуществляется успешно"):
        names_after = c_s.get_customers_names()
        assert names_after == sorted(
            names_after, reverse=True
        ), "Cортировка не соответствует Я-А"
        assert (
            names_before != names_after
        ), "Проверка сортировки не имела смысла, порядок имен не изменился"
