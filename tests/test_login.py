from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #selenium에서 expected_condition 도입하여 EC로 정의
from selenium.webdriver.support.wait import WebDriverWait as wait

from utils.auth import clean_session

base_url = "http://127.0.0.1:5000/"

def test_login_success(browser):
    clean_session(browser)

    browser.get(f"{base_url}/login") #로그인 화면 열기
    browser.find_element(By.NAME, "username").send_keys("test-user") #username란에 'test-user' 입력
    browser.find_element(By.NAME, "password").send_keys("1234") # password란에 '1234'입력
    browser.find_element(By.XPATH, "//button[text()='Login']").click() #login 버튼 추적하여 클릭

    success_text = browser.find_element(By.CSS_SELECTOR, ".alert-success").text
    assert "로그인 성공!" in success_text # 로그인 성공 후 index 페이지에서 '로그인 성공!' 표시 확인

def test_login_fail(browser):
    clean_session(browser)

    browser.get(f"{base_url}/login")
    browser.find_element(By.NAME, "username").send_keys("wrong_user")
    browser.find_element(By.NAME, "password").send_keys("wrong_pass")
    browser.find_element(By.XPATH, "//button[text()='Login']").click()
    wait(browser, 10).until(EC.url_to_be(f"{base_url}/login"))
    
    fail_text = browser.find_element(By.CSS_SELECTOR, ".alert-danger").text
    assert '아이디 또는 비밀번호가 올바르지 않습니다.' == fail_text # 실패 시 여전히 login 페이지에 머무름
