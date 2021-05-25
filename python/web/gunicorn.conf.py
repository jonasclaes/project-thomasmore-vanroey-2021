import multiprocessing

bind = ["0.0.0.0:8080"]
workers = 1
worker_class = "eventlet"

accesslog = '-'
errorlog = '-'

# Debug
reload = True
