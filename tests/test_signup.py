import time #시간 모듈
import uuid #유일한 표시 부호 생성
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #selenium에서 expected_condition 도입하여 EC로 정의
from selenium.webdriver.support.wait import WebDriverWait as wait

from utils.auth import clean_session

base_url = "http://127.0.0.1:5000"

def test_signup_success(browser):
    clean_session(browser)

    username = f"user_{uuid.uuid4().hex[:6]}" #테스트 ID 생성
    password = "securePass123" #해당 패스워드 생성

    browser.get(f"{base_url}/register") #회원가입 페이지 진입
    wait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username) #생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password) #생성한 패스워드를 Password란에 입력
    browser.find_element(By.NAME, "confirm").send_keys(password) #생성한 패스워드를 Confirm Password란에 입력
    browser.find_element(By.XPATH, "/html/body/main/div/div/form/button").click() #sign up 버튼 클릭
    wait(browser, 10).until(EC.url_changes(f"{base_url}/register")) #잠깐 대기
    
    assert "register" not in browser.current_url.lower() #회원가입 성공 시 URL이 signup이 아니어야 함

def test_signup_then_login(browser):
    clean_session(browser)

    username = f"user_{uuid.uuid4().hex[:6]}" #테스트 ID 생성
    password = "securePass123" #해당 패스워드 생성

    browser.get(f"{base_url}/register")  # 회원가입 페이지 진입
    wait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)  # 생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password)  # 생성한 패스워드를 Password란에 입력
    browser.find_element(By.NAME, "confirm").send_keys(password)  # 생성한 패스워드를 Confirm Password란에 입력
    browser.find_element(By.XPATH, "/html/body/main/div/div/form/button").click()  # sign up 버튼 클릭
    wait(browser, 10).until(EC.url_to_be(f"{base_url}/login" )) #잠깐 대기

    browser.get(f"{base_url}/login") #로그인  화면으로 전환
    wait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username) #생성한 ID를 Username란에 입력
    browser.find_element(By.NAME, "password").send_keys(password) #생성한 패스워드를 Password란에 입력
    browser.find_element(By.XPATH, "//button[text()='Login']").click() #login 버튼 클릭

    success_text = browser.find_element(By.CSS_SELECTOR, ".alert-success").text
    assert f"로그인 성공!" in success_text #로그인 성공후 화면에서 '로그인 성공!' 표시
