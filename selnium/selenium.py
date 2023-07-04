from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Launch Chrome browser
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open Tinder website
driver.get('https://tinder.com')

# Wait for the sign-in button to appear and click it
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in with Google')]"))
)
sign_in_button.click()

# Switch to the Google sign-in window
driver.switch_to.window(driver.window_handles[1])

# Provide your Google account credentials
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'identifierId'))
)
email_input.send_keys('your_google_email@gmail.com')

next_button = driver.find_element(By.ID, 'identifierNext')
next_button.click()

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
password_input.send_keys('your_google_password')

password_next_button = driver.find_element(By.ID, 'passwordNext')
password_next_button.click()

# Switch back to the Tinder window
driver.switch_to.window(driver.window_handles[0])

# Wait for the Tinder main page to load (adjust the timeout if needed)
WebDriverWait(driver, 10).until(
    EC.title_contains('Tinder')
)

# Perform further actions on the Tinder website
# ...

# Remember to quit the browser when you're done
driver.quit()
