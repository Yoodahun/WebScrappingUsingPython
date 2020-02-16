import requests
from bs4 import BeautifulSoup

ADDRESS = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(ADDRESS)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("a", {"class": "s-link"})['title']
    company, location = html.find("h3", {
        "class": "fc-black-700"
    }).find_all("span")
    link = html['data-jobid']
    return {
        'title': title,
        'company': company.string.strip(),
        'location': location.string.strip(),
        'link' : f"https://stackoverflow.com/jobs/{link}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"StackOverflow {page} page")
      result = requests.get(f"{ADDRESS}&pg={0+1}")
      soup = BeautifulSoup(result.text, 'html.parser')
      results = soup.find_all("div", {"class":"-job"})
      for result in results:
          job = extract_job(result)
          jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
