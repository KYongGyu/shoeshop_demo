import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "http://127.0.0.1:5000" # Flask 서버가 실행되는 주소
DEFAULT_USERNAME = "testuser"
DEFAULT_PASSWORD = "password123"

@pytest.fixture(scope="session")
def setup_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture
def clean_session(setup_driver):
    """
    각 테스트 시작 전/후에 세션을 정리하는 픽스처
    (로그아웃 및 브라우저 캐시 정리 효과)
    """
    driver = setup_driver
    # 1. 홈 페이지로 이동 (테스트 시작점)
    driver.get(BASE_URL)

    # 2. 로그아웃 상태 보장
    if driver.find_elements(By.LINK_TEXT, "Logout"):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    yield driver


@pytest.fixture
def register_and_login(clean_session):
    """
    테스트용 사용자 등록 및 로그인하는 픽스처
    """
    driver = clean_session

    # 1. 회원가입 페이지로 이동
    driver.find_element(By.LINK_TEXT, "Sign Up").click()

    # 2. 회원가입
    driver.find_element(By.ID, "username").send_keys(DEFAULT_USERNAME)
    driver.find_element(By.ID, "password").send_keys(DEFAULT_PASSWORD)
    driver.find_element(By.ID, "confirm").send_keys(DEFAULT_PASSWORD)
    driver.find_element(By.TAG_NAME, "form").submit()

    # 3. 로그인 페이지로 리다이렉션 후 로그인
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/login"))
    driver.find_element(By.ID, "username").send_keys(DEFAULT_USERNAME)
    driver.find_element(By.ID, "password").send_keys(DEFAULT_PASSWORD)
    driver.find_element(By.TAG_NAME, "form").submit()

    # 4. 로그인 성공 후 Home으로 이동했는지 확인
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))
    return driver