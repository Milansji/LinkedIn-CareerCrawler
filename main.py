from selenium import webdriver

from linkedin import Linkedin
import time
from constants import filters
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')

def main():
    
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    linkedin_interface = Linkedin(driver)
    linkedin_interface.login(email=email,password=password)
    linkedin_interface.switch_tab(target="job")
    linkedin_interface.search("Software engineering inter","Germany")
    linkedin_interface.set_filter("experience",filters.Type.INTERNSHIP)
    linkedin_interface.set_filter("date",filters.Date.LAST_24_HOURS)
    linkedin_interface.find_jobs()
    time.sleep(3)

    # Close the browser
    driver.quit()
if __name__ == "__main__":
    main()