import csv

def save_to_file(jobs):
  # open > 파일이 없으면 생성해줌.
  # mode > write mode
  file = open("jobs.csv", mode="w", encoding='shift_jis')
  writer = csv.writer(file)
  # firstrow. header
  writer.writerow(["title", "company", "location", "link"])
  print ("Start Exporting to CSV !")
  for job in jobs:
    writer.writerow(list(job.values()))
  
  print ("It's done !")
  return