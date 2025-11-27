import time #시간 모듈
import uuid #유일한 표시 부호 생성
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #selenium에서 expected_condition 도입하여 EC로 정의

def test_signup_success(browser, base_url, wait):
    username = f"user_{uuid.uuid4().hex[:6]}" #테스트 ID 생성
    password = "securePass123" #해당 패스워드 생성

    browser.get(f"{base_url}/signup") #회원가입 페이지 진입
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username) #생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password) #생성한 패스워드를 Password란에 입력
    browser.find_element(By.NAME, "confirm password").send_keys(password) #생성한 패스워드를 Confirm Password란에 입력
    browser.find_element(By.XPATH, "//button[text()='Signup']").click() #sign up 버튼 클릭
    time.sleep(1) #1초 대기

    assert "signup" not in browser.current_url.lower() #회원가입 성공 시 URL이 signup이 아니어야 함

def test_signup_then_login(browser, base_url, wait):
    username = f"user_{uuid.uuid4().hex[:6]}" #테스트 ID 생성
    password = "securePass123" #해당 패스워드 생성

    browser.get(f"{base_url}/signup") #회원가입 페이지 진입
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username) #생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password) #생성한 패스워드를 Password란에 입력
    browser.find_element(By.NAME, "confirm password").send_keys(password) #생성한 패스워드를 Confirm Password란에 입력
    browser.find_element(By.XPATH, "//button[text()='Signup']").click() #sign up 버튼 클릭
    time.sleep(1) #1초 대기

    browser.get(f"{base_url}/login") #로그인  화면으로 전환
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username) #생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password) #생성한 패스워드를 Password란에 입력
    browser.find_element(By.XPATH, "//button[text()='Login']").click() #login 버튼 클릭

    success_text = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '로그인 성공')]"))).text
    assert f"로그인 성공!" in welcome_text #로그인 성공후 화면에서 '로그인 성공!' 표시