import requests
import 

indeed_result = requests.get("https://jp.indeed.com/%E6%B1%82%E4%BA%BA?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result.text)