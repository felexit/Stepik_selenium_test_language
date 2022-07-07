import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    time.sleep(30)
    ans = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert ans.is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'