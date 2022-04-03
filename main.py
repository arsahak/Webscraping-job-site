import time
from bs4 import BeautifulSoup
import requests

print('Put some skill that your are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&gadLink=Python').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate (jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open('posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')


#Run this program after every 10 minutes

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
