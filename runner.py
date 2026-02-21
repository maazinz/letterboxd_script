from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time, random

from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USERNAME")
PASS = os.getenv("PASSWORD")
DIR = os.getenv("DIRECTORY")
FILEPATH = f"{DIR}/movies.txt"


def parse_movies(filepath):
    movies = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("- [ ]"):
                continue
            title = stripped.replace("- [x]", "").strip()
            movies.append(title)
    return movies

def login(driver, username, password):
    try:
        driver.get("https://letterboxd.com/sign-in/")
        username_field = driver.find_element(By.ID, "field-username")
        password_field = driver.find_element(By.ID, "field-password")
        time.sleep(2)

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Login successful")
        time.sleep(random.uniform(2,4))
    except NoSuchElementException as e:
        print(f"Login failed: Could not find login elements - {e}")
        raise
    except WebDriverException as e:
        print(f"Login failed: WebDriver error - {e}")
        raise


def mark_as_watched(driver, wait, title):
    original_title = title
    title = title.lower()
    film_url = f"https://letterboxd.com/film/{title.replace(' ', '-')}/"
    
    try:
        driver.get(film_url)
        time.sleep(random.uniform(2,4))
    except WebDriverException as e:
        print(f"✗ Failed to load page for '{original_title}': {e}")
        return False
    
    try:
        watched_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "span.action.-watch.ajax-click-action")
            )
        )
        watched_btn.click()
        time.sleep(random.uniform(1,2))
        print(f"✓ Marked '{original_title}' as watched")
        return True
    except TimeoutException:
        print(f"✗ Failed to mark '{original_title}' as watched: Watch button not found (URL: {film_url})")
        return False
    except NoSuchElementException as e:
        print(f"✗ Failed to mark '{original_title}' as watched: Element not found - {e}")
        return False
    except WebDriverException as e:
        print(f"✗ Failed to click watch button for '{original_title}': {e}")
        return False


if __name__ == "__main__":
    all_movies = parse_movies(FILEPATH)
    failed_movies = []

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    login(driver, USER, PASS)

    for movie in all_movies:
        print(movie)
        success = mark_as_watched(driver, wait, movie)
        if not success:
            failed_movies.append(movie)
    
    if failed_movies:
        print(f"\nFailed movies ({len(failed_movies)}):")
        for movie in failed_movies:
            print(f"  - {movie}")
    else:
        print("\nAll movies successfully marked as watched!")
    
    print("="*50)

    driver.quit()