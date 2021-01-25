import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get
from datetime import datetime
import re
from twilio.rest import Client

url='https://in.indeed.com/Latest-jobs' #put the urls in this format of .../jobs because when u click on the homepage some other URL description appears. By putting the ./jobs URL also same thing appears so decided to go for it.
job_keyword='transport'
response=get(url) #used for opening URLs and can also access and retrieve data
soup=BeautifulSoup(response.text,'html.parser') #Python library for pulling data out of HTML and XML files
prettyHTML=soup.prettify() # Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document. Tags means like a particular job , i.e. "Transport"
#print(prettyHTML)   # html code for https://www.internsg.com/jobs/

jobInfos=soup.find_all('a',class_='jobtitle turnstileLink')
for x in jobInfos:
    a = re.findall("(.*?)</a>", str(x)) #applying regex for extracting strings between tags.... dont have to put '>' at the start of (.*?)
    str1 = str(''.join(str(e) for e in a)) #to convert list to string or remove the brackets
    print(str1)

# For further actions check
# https://medium.com/@automationfeed/automate-your-job-search-process-with-python-c448c769c8fc

#For further reference
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# For website indeed and webscrapping
# https://chrislovejoy.me/job-scraper/


"""

# initializing tag 
tag = "b"
  
# regex to extract required strings 
reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, test_str) 
  
# printing result 
print("The Strings extracted : " + str(res)) 


"""
