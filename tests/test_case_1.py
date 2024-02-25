import allure
from pageobjects.provider import PobjectProvider


@allure.suite("Тест-кейс 'Добавить клиента'")
@allure.title("Тест-кейс 'Добавить клиента'")
def test_case_1(provider: PobjectProvider):
    page = provider.page_actions
    mp = provider.manager_page
    ad = provider.add_customer_form
    cs = provider.customers_table

    with allure.step("Подготовка, Тестовые данные"):
        customer = ad.generate_test_user()
        mp.navigate()

    with allure.step("1) Нажать на кнопку 'Add Customer'"):
        page.click(mp.btn_add_cust)

    with allure.step("2) Ввести номер из тестовых данных в поле 'First Name'"):
        page.send_keys(ad.inp_first_name, customer.first_name)

    with allure.step("3) Ввести номер из тестовых данных в поле 'Last Name'"):
        page.send_keys(ad.inp_last_name, customer.last_name)

    with allure.step("4) Ввести номер из тестовых данных в поле 'Post Code'"):
        page.send_keys(ad.inp_post_code, customer.post_code)

    with allure.step("5) Нажать кнопку 'Add Customer'"):
        page.click(ad.btn_add_customer)

    with allure.step("6) Получить всплывающее окно с видимой кнопкой 'OK'"):
        page.accept_alert()

    with allure.step("7) Нажать на кноку 'Show Customers'"):
        page.click(mp.btn_show_cust)

    with allure.step("8) Проверить, что клиента нет в таблице клиентов"):
        names_after = cs.get_customers_names()
        assert customer.first_name in names_after, "Клиент остался в списке клиентов"
