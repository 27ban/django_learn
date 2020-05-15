from django_learn import celery_app as app


@app.task
def add_task(x, y):
    import time
    time.sleep(10)
    return x + y
