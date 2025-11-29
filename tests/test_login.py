import time #시간 모듈
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC #selenium에서 expected_condition 도입하여 EC로 정의

def test_login_success(browser, base_url, wait):
    browser.get(f"{base_url}/login") #로그인 화면 열기
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("test_user") #username란에 'test_user' 입력
    browser.find_element(By.NAME, "password").send_keys("1234") # password란에 '1234'입력
    browser.find_element(By.XPATH, "//button[text()='Login']").click() #login 버튼 추적하여 클릭


    success_text = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '로그인 성공')]"))).text
    assert "로그인 성공!" in success_text # 로그인 성공 후 index 페이지에서 '로그인 성공!' 표시 확인

def test_login_fail(browser, base_url, wait):
    browser.get(f"{base_url}/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("wrong_user")
    browser.find_element(By.NAME, "password").send_keys("wrong_pass")
    browser.find_element(By.XPATH, "//button[text()='Login']").click()
    wait.until(EC.url_to_be(f"{base_url}/login" ))
    
    fail_text = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '아이디 또는 비밀번호가 올바르지 않습니다.')]"))).text
    assert browser.current_url == f"{base_url}/login" # 실패 시 여전히 login 페이지에 머무름
