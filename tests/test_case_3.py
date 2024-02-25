import allure
from pageobjects.provider import PobjectProvider


@allure.suite("Тест-кейс 'Удаление клиента'")
@allure.title("Тест-кейс 'Удаление клиента'")
def test_case_3(provider: PobjectProvider):
    page = provider.page_actions
    m_p = provider.manager_page
    c_t = provider.customers_table
    with allure.step("Подготовка, Тестовые данные"):
        m_p.navigate()
        page.click(m_p.btn_show_cust)

    with allure.step("1) Получить из таблицы 'Customers' список имен"):
        names = c_t.get_customers_names()

    with allure.step("2) Вычислить длину каждого имени"):
        lens = c_t.get_names_lengths(names)

    with allure.step("3) Определить среднеарифметическое получившихся длин"):
        avg = c_t.get_average(lens)

    with allure.step(
        "4) Определить клиента с именем, длина которого будет ближе к среднему арифметическому"
    ):
        diffs = c_t.get_differences(avg, lens)
        closest_index = c_t.get_closest_index(diffs)

    with allure.step("5) Нажать на кнопку 'Delete' и удалить клиента"):
        c_t.click_delete_by_index(closest_index)

    with allure.step(
        "6) Убедиться, что удаленный клиент отсутствует в списке клиентов"
    ):
        c_t.check_name_not_in_customers_names(closest_index, names)
