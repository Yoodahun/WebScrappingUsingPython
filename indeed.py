import requests
from bs4 import BeautifulSoup

LIMIT = 50
ADDRESS = f"https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&limit={LIMIT}&radius=25"

# extract_indeed_pages()
# request를 실행하여 데이터를 받아옴.
# 받아온 텍스트들을 html형태로 parsing함.
# parsing한 html중에 `.pagination` 을 가진 div를 전부 찾음.
# 내부에서 다시 a태그를 가진 모든 것을 찾음.
# 빈 배열을 생성한 후, 첫 요소를 포함하여 마지막 요소를 제외한 모든 요소들에 대해 반복문을 실행
### a태그 안의 span태그 안의 string을 추출하여 빈 배열에 순서대로 추가해줌.
# 빈 배열의 내용을 확인 후, 제일 큰 값을 max_page로 지정
# return

def extract_indeed_pages():
  result = requests.get(ADDRESS)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", {"class":"pagination"})

  # print(pagination.prettify())
  links = pagination.find_all("a")
  # print(links)
  pages = []
  for link in links[0:-1]:
    pages.append(int(link.find("span").string))
  # print(pages[0:-1]) #-1 is not included
  # print(pages[-1])
  max_page = pages[-1]
  return max_page

# extract_indeed_jobs
# last_pages를 parameter로 받아, 해당 크기만큼의 range를 생성한 후
# 그 range만큼 for문을 실행.
### address에 &start=를 추가. 리미트에 페이지 크기를 곱하준 후 Request실행. 각 페이지 추출
### 각 페이지별로 soup을 이용하여 html pasing
### parsing한 페이지에서 jobsearch-SerpJobCard class를 가진 div를 find_all
### find_all한 결과를 대상으로 extract_job실행
### 실행결과를 배열 jobs에 보존
### return
def extract_indeed_jobs(last_pages):
  jobs = []
  for page in range(last_pages):
    print(f"Scrapping page {page}")
    result = requests.get(f"{ADDRESS}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", { "class" : "jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  
  return jobs
  # dictionary list.

# extract_job
# parameter html을 넘겨받아 title, company, location, job_id를 추출함.
# company의 공백을 없애주기 위해 strip
# location의 경우 재택근무를 하는 경우에는 작성되어 있지 않음. attribute를 이용하여 추출.
# 추출된 값들을 dictionary형태로 바꾸어 return
def extract_job(html):
  title = html.find('div',{'class':'title'}).find('a')['title']
  company = html.find("span", {"class" : "company"}).text
  # company_anchor = company.find("a")

  # if company_anchor is not None:
  #   company = company_anchor.string
  # else:
  #   company = company.string
  company = company.strip()
  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  job_id = html['data-jk']
  return {'title': title, 'company': company, 'location' : location,
  'link' : f"https://jp.indeed.com/%E4%BB%95%E4%BA%8B?jk={job_id}"    
  }

  