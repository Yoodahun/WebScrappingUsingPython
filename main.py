from indeed import get_jobs as get_indeed_jobs
from stackOverflow import get_jobs as get_stack_overflow_jobs
from exportToCsv import save_to_file

indeed_jobs = get_indeed_jobs()
stackOverflow_jobs = get_stack_overflow_jobs()
jobs = indeed_jobs + stackOverflow_jobs
save_to_file(jobs)


