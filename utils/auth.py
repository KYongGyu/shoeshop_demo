from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clean_session(browser):
    browser.get("http://127.0.0.1:5000/")
    wait = WebDriverWait(browser, 5)

    try:
        logout_btn = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        )

        logout_btn.click()
        print("\n[INFO] 이전 세션이 감지되어 로그아웃을 수행했습니다.")

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-info")))

    except:
        print("\n[INFO] 이미 로그아웃 상태이거나 'Logout' 링크를 찾을 수 없습니다.")
        pass

def user_login(browser):
    menu_login = browser.find_element(By.LINK_TEXT, "Login")
    wait = WebDriverWait(browser, 5)

    menu_login.click()
    browser.find_element(By.ID, "username").send_keys("test-user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))