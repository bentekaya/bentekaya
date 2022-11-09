

import json 
import os
# selenium (scrapping module)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# beautifulSoup (pulling data out of HTML)
from bs4 import BeautifulSoup
from datetime import datetime
def save_profile(browser2: webdriver, wait: WebDriverWait, profileElement: WebElement, profiles_link: str, profilesData: list) :
      # initialisation
      skills_profile=[]
      exp_profile=[]
      edu_profile=[]
      experiencee=[]
      profile_page_source=browser2.page_source
      profile_soup1=BeautifulSoup(profile_page_source, "lxml")
      # Get the informations 
      profile_name=""
      if (profile_soup1.find('h1',{ 'class':"text-heading-xlarge inline t-24 v-align-middle break-words"})):
        profile_name = profile_soup1.find('h1',{ 'class':"text-heading-xlarge inline t-24 v-align-middle break-words"}).text.strip()
      profile_title=""
      if(profile_soup1.find('div',{ 'class':"text-body-medium break-words"})):
        profile_title = profile_soup1.find('div',{ 'class':"text-body-medium break-words"}).text.strip()
      loc_name=""
      if(profile_soup1.find('span',{'class': "text-body-small inline t-black--light break-words"})):
        loc_name = profile_soup1.find('span',{'class': "text-body-small inline t-black--light break-words"}).text.strip()
      if profile_soup1.find_all('section',{'class':"artdeco-card"}):
       all_information = profile_soup1.find_all('section',{'class':"artdeco-card"})
       for info_profile in all_information :
        # Skills section
        if info_profile.find('div',{'id':"skills"}) :
          if info_profile.find('div',{'class':'pvs-list__footer-wrapper'}) : # there is a lot of skills (list is long)
            all_skills_button=info_profile.find('div',{'class':'pvs-list__footer-wrapper'})
            if all_skills_button.find('a',{'class':'optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--muted inline-flex justify-center full-width align-items-center artdeco-button--fluid'}):
              more_buttons = browser2.find_elements(By.CLASS_NAME, 'artdeco-button--3')
              for button in more_buttons:
                if(button.get_attribute('href').find("/details/skills") != -1):
                  button.click()
                  break
              wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pvs-entity--padded")))
              # load more button
              try:
                browser2.find_element(By.CLASS_NAME, "scaffold-finite-scroll__load-button")
                browser2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(browser2, 1).until(EC.invisibility_of_element_located((By.CLASS_NAME, "scaffold-finite-scroll__load-button"))) 
              except:
                print("Load more button not found")
              # Save page source 
              skills_page_source = browser2.page_source
              skills_soup = BeautifulSoup(skills_page_source, "lxml")
              # Extract every skill name 
              if skills_soup.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}) :
                all_skills = skills_soup.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'})
                for all_skill in all_skills :
                  skill_name=""
                  if all_skill.find('div',{'class':"display-flex align-items-center"}) != None :
                    skill_name1=all_skill.find('div',{'class':"display-flex align-items-center"})
                    skill_name=skill_name1.find('span',{'class':"visually-hidden"}).text.strip()
                  skills_profile.append(skill_name)
              # Go back
              elem = browser2.find_element(By.CLASS_NAME, 'artdeco-button--3')
              browser2.execute_script("arguments[0].click();", elem)
          else: # there is some skills (list is short)
            if info_profile.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}) :
              all_skills2=info_profile.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'})
              for all_skill2 in all_skills2 : 
                skill_name=""
                if all_skill2.find('div',{'class':"display-flex align-items-center"}) != None :
                  skill_name1=all_skill2.find('div',{'class':"display-flex align-items-center"})
                  skill_name=skill_name1.find('span',{'class':"visually-hidden"}).text.strip()
                skills_profile.append(skill_name)
        # Experience section
        if info_profile.find('div',{'id':"experience"}) :
          if info_profile.find('div',{'class':'pvs-list__footer-wrapper'}) : # there is a lot of experiences (list is long)
           all_exp_button=info_profile.find('div',{'class':'pvs-list__footer-wrapper'})
           if all_exp_button.find('a',{'class':'optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--muted inline-flex justify-center full-width align-items-center artdeco-button--fluid'}):
            more_buttons = browser2.find_elements(By.CLASS_NAME, 'artdeco-button--3')
            for button in more_buttons:
              if(button.get_attribute('href').find("/details/experience") != -1):
                button.click()
                break
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pvs-entity--padded")))
            # load more button
            try:
              browser2.find_element(By.CLASS_NAME, "scaffold-finite-scroll__load-button")
              browser2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
              WebDriverWait(browser2, 1).until(EC.invisibility_of_element_located((By.CLASS_NAME, "scaffold-finite-scroll__load-button")))
            except:
              print("Load more button not found")
            # Save page source 
            experiences_page_source = browser2.page_source
            experiences_soup = BeautifulSoup(experiences_page_source, "lxml")
            # Extract every experience
            if experiences_soup.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}) :
             all_exp = experiences_soup.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'})
             for i in range(len(all_exp)) :
              list_exper=[]
              if all_exp[i].find('span',{'class':"pvs-entity__path-node"}): # multiple posts in the same experience
               if all_exp[i].find('li',{'class':""}):
                 exp2=all_exp[i].find('li',{'class':""})
                 if exp2.find_all('span',{'class':"pvs-entity__path-node"}):
                   if exp2.find_all('li',{'class':"pvs-list__paged-list-item"}):
                     exp3=exp2.find_all('li',{'class':"pvs-list__paged-list-item"})
                     for exp1 in exp3:
                      company_name=""
                      if all_exp[i].find('div',{'class':"display-flex align-items-center"}) != None :
                       company_name11=all_exp[i].find('div',{'class':"display-flex align-items-center"})
                       company_name=company_name11.find('span',{'class':"visually-hidden"}).text.strip()
                      job_title=""
                      if exp1.find('div',{'class':"display-flex align-items-center"}) != None :
                       job_title1=exp1.find('div',{'class':"display-flex align-items-center"})
                       job_title=job_title1.find('span',{'class':"visually-hidden"}).text.strip()
                      job_task=""
                      if exp1.find('div',{'class':"display-flex align-items-center t-14 t-normal t-black"}) != None :
                       job_task1=exp1.find('div',{ 'class':"display-flex align-items-center t-14 t-normal t-black"})
                       job_task=job_task1.find('span',{ 'class':"visually-hidden"}).text.strip()
                      exp_duration=""
                      if exp1.find('span',{'class':"t-14 t-normal t-black--light"}) != None :
                       exp_duration1=exp1.find('span',{'class':"t-14 t-normal t-black--light"})
                       exp_duration=exp_duration1.find('span',{'class':"visually-hidden"}).text.strip()
                      exp_info={'work':job_title,'exp_location':company_name,'exp_duration':exp_duration, 'tasks':job_task}
                      list_exper.append(exp_info)
                      experiencee=list_exper[0:]
                     if len(list_exper ) !=0 :
                      for h in range(len(list_exper)):
                       exp_profile.append(experiencee[h])
              else : # just one post
                job_title=""
                if all_exp[i].find('div',{'class':"display-flex align-items-center"}) != None :
                  job_title1=all_exp[i].find('div',{'class':"display-flex align-items-center"})
                  job_title=job_title1.find('span',{'class':"visually-hidden"}).text.strip()
                company_name=""
                if all_exp[i].find('span',{'class':"t-14 t-normal"}) != None :
                  company_name1=all_exp[i].find('span',{'class':"t-14 t-normal"})
                  company_name=company_name1.find('span',{'class':"visually-hidden"}).text.strip()
                exp_duration=""
                if all_exp[i].find('span',{'class':"t-14 t-normal t-black--light"}) != None :
                  exp_duration1=all_exp[i].find('span',{'class':"t-14 t-normal t-black--light"})
                  exp_duration=exp_duration1.find('span',{'class':"visually-hidden"}).text.strip()
                job_task=""
                if all_exp[i].find('div',{'class':"display-flex align-items-center t-14 t-normal t-black"}) != None :
                 job_task1=all_exp[i].find('div',{'class':"display-flex align-items-center t-14 t-normal t-black"})
                 job_task=job_task1.find('span',{'class':"visually-hidden"}).text.strip()
                experience={'work':job_title,'exp_location':company_name,'exp_duration':exp_duration,'tasks':job_task}
                exp_profile.append(experience)     
            # Go back
            elem = browser2.find_element(By.CLASS_NAME, 'artdeco-button--3')
            browser2.execute_script("arguments[0].click();", elem)
          else: # there is some experience (list is short)
            if info_profile.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'}) :
             all_exp2=info_profile.find_all('div',{'class':'pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested'})
             for i in range(len(all_exp2)) : 
              list_exper=[]
              if all_exp2[i].find('span',{'class':"pvs-entity__path-node"}): # multiple posts in the same experience
               if all_exp2[i].find_all('li',{'class':""}):
                 exp=all_exp2[i].find_all('li',{'class':""})
                 for exp1 in exp:
                  if exp1.find_all('span',{'class':"pvs-entity__path-node"}):
                    exper=exp1
                    company_name=""
                    if all_exp2[i].find('div',{'class':"display-flex align-items-center"}) != None :
                      company_name11=all_exp2[i].find('div',{'class':"display-flex align-items-center"})
                      company_name=company_name11.find('span',{'class':"visually-hidden"}).text.strip()
                    job_title=""
                    if exper.find('div',{'class':"display-flex align-items-center"}) != None :
                      job_title1=exper.find('div',{'class':"display-flex align-items-center"})
                      job_title=job_title1.find('span',{'class':"visually-hidden"}).text.strip()
                    job_task=""
                    if exper.find('div',{'class':"pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center"}) != None :
                      job_task1=exper.find('div',{ 'class':"pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center"})                     
                      job_task=job_task1.find('span',{ 'class':"visually-hidden"}).text.strip()
                    exp_duration=""
                    if exper.find('span',{'class':"t-14 t-normal t-black--light"}) != None :
                      exp_duration1=exper.find('span',{'class':"t-14 t-normal t-black--light"})
                      exp_duration=exp_duration1.find('span',{'class':"visually-hidden"}).text.strip()
                    exp_info={'work':job_title,'exp_location':company_name,'exp_duration':exp_duration, 'tasks':job_task}
                    list_exper.append(exp_info)
                    experiencee=list_exper[0:]

                 if len(list_exper ) !=0 :
                   for h in range(len(list_exper)):
                     exp_profile.append(experiencee[h])
              else : # just one post 
                job_title=""
                if all_exp2[i].find('div',{'class':"display-flex align-items-center"}) != None :
                  job_title1=all_exp2[i].find('div',{'class':"display-flex align-items-center"})
                  job_title=job_title1.find('span',{'class':"visually-hidden"}).text.strip()
                company_name=""
                if all_exp2[i].find('span',{'class':"t-14 t-normal"}) != None :
                  company_name1=all_exp2[i].find('span',{'class':"t-14 t-normal"})
                  company_name=company_name1.find('span',{'class':"visually-hidden"}).text.strip()
                exp_duration="" 
                if all_exp2[i].find('span',{'class':"t-14 t-normal t-black--light"}) != None :
                  exp_duration1=all_exp2[i].find('span',{'class':"t-14 t-normal t-black--light"})
                  exp_duration=exp_duration1.find('span',{'class':"visually-hidden"}).text.strip()
                job_task=""  
                if all_exp2[i].find('div',{'class':"inline-show-more-text"}) != None :
                  job_task1=all_exp2[i].find('div',{'class':"inline-show-more-text"})
                  job_task=job_task1.find('span',{'class':"visually-hidden"}).text.strip()
                experience={'work':job_title,'exp_location':company_name,'exp_duration':exp_duration,'tasks':job_task}
                exp_profile.append(experience)
        # Education section
