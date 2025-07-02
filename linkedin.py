from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Linkedin:
    def __init__(self,driver):
        self.driver = driver
         
    def login(self,email,password):
        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        login_btn_container = self.driver.find_element(By.CLASS_NAME, "login__form_action_container")
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']")
        login_btn.click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "global-nav__nav")))
    def switch_tab(self,target:str):
        if target == "job":
            self.driver.get("https://www.linkedin.com/jobs/search/")
    def find_jobs(self,limit =10):
        found_jobs = []
        jobs_list = self.driver.find_element(By.CLASS_NAME,"scaffold-layout__list").find_element(By.TAG_NAME,"ul")
        jobs = jobs_list.find_elements(By.TAG_NAME,"li")
        for job in jobs:
            print("job")
            print(job.get_attribute("outerHTML"))
            try:
                job_card = job.find_element(By.CSS_SELECTOR, '[data-view-name="job-card"]')
                job_data = job_card.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[0]
                job_txt_inf_cont = job_data.find_element(By.TAG_NAME,"div").find_elements(By.TAG_NAME,"div")[1].find_elements(By.TAG_NAME,"div")
                job_title = job_txt_inf_cont[0].find_element(By.TAG_NAME,"a").text if len(list(job_txt_inf_cont)) > 0 else None
                job_link = job_txt_inf_cont[0].find_element(By.TAG_NAME,"a").get_attribute("href") if len(list(job_txt_inf_cont)) > 0 else None
                company = job_txt_inf_cont[1].text if len(list(job_txt_inf_cont)) > 1 else None
                location = job_txt_inf_cont[2].text if len(list(job_txt_inf_cont)) > 2 else None
                found_jobs.append({"title":job_title,"link":job_link,"company":company,"location":location})
            except Exception as e:
                print("Error during job data extraction:",e)
                        




    def search(self,keyword:str=None,location:str = None):
        if keyword:
            self.driver.find_element(By.XPATH, "//*[contains(@id, 'jobs-search-box-keyword')]").send_keys(keyword)
        if location:
            self.driver.find_element(By.XPATH, "//*[contains(@id, 'jobs-search-box-location')]").send_keys(location)
        search_btn = self.driver.find_element(By.CLASS_NAME,"jobs-search-box__submit-button")
        search_btn.click()
        search_btn.click()
        time.sleep(10)
        
    def set_filter(self,filter_type:str,value:str):
        if filter_type == "experience":
           # Click experience drop down menu    
           self.driver.find_element(By.ID,"searchFilter_experience").click()
           exp_fltr_opts_container = self.driver.find_element(By.ID,"hoverable-outlet-experience-level-filter-value").find_element(By.TAG_NAME,"form")
           # find available options
           experience_filter_options =exp_fltr_opts_container.find_element(By.TAG_NAME,"ul").find_elements(By.TAG_NAME,"li")
           # if specified value is available in the menu, click it.
           for option in experience_filter_options:
               option_label = option.find_element(By.TAG_NAME, "label")
               opt_label_text = option_label.find_elements(By.TAG_NAME,"span")[0].text.lower().strip()
               if  opt_label_text == value.lower().strip():
                   option_label.click()
                   time.sleep(3)
                   # search with new filters    
                   buttons = exp_fltr_opts_container.find_element(By.CLASS_NAME,"reusable-search-filters-buttons")
                   confirm_btn = buttons.find_element(By.CLASS_NAME,"artdeco-button--primary")
                   confirm_btn.click()
                   break
        if filter_type == "date":
            # Click date drop down menu  
            self.driver.find_element(By.ID,"searchFilter_timePostedRange").click()
            drop_down_menu = self.driver.find_element(By.ID, "hoverable-outlet-date-posted-filter-value")
            # find available options
            date_options = drop_down_menu.find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME,"li")
            # if specified value is available in the menu, click it.
            for option in date_options:
               option_label = option.find_element(By.TAG_NAME, "label")
               opt_label_text = option_label.find_elements(By.TAG_NAME,"span")[0].text.lower().strip() 
               if opt_label_text == value.lower().strip():
                   option_label.click()
                   time.sleep(3)
                   # search with new filters  
                   drop_down_menu.find_element(By.CLASS_NAME,"reusable-search-filters-buttons")
                   confirm_btn = drop_down_menu.find_element(By.CLASS_NAME,"artdeco-button--primary")
                   confirm_btn.click()
                   break
        time.sleep(7)

             

