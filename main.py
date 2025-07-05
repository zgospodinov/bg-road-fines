import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

ID_CARD = os.getenv("ID_CARD")
DRIVING_LICENSE = os.getenv("DRIVING_LICENSE")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

def fetch_ticket_html():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Ensures full rendering in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://e-uslugi.mvr.bg/services/obligations")

        # Handle cookie consent if present
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                lambda d: d.find_element(By.XPATH, '//aside[@id="cookieInfo"]//button')
            )
            cookie_btn.click()
        except Exception:
            pass  # Ignore if not present

        driver.find_element(By.ID, "obligedPersonIdent").send_keys(ID_CARD)
        driver.find_element(By.ID, "drivingLicenceNumber").send_keys(DRIVING_LICENSE)
        driver.find_element(By.XPATH, '//*[@id="ARTICLE-CONTENT"]/div/div[2]/div[1]/button').click()

        # Wait for the result to appear
        WebDriverWait(driver, 20).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="ARTICLE-CONTENT"]/div/div[2]/h2').text.strip() != ""
        )
        
        search_result_element = driver.find_element(By.ID, "ARTICLE-CONTENT")
        return search_result_element.get_attribute("outerHTML")  # Return raw HTML for reliability

    except Exception as ex:
        print(ex)
        return None
    finally:
        driver.quit()



def main():
    print("Hello from bg-road-fines!")
    page_html = fetch_ticket_html()
    print(page_html)


if __name__ == "__main__":
    main()
