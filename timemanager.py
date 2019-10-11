import time
import shelve

while True:
    time.sleep(60)
    db = shelve.open('db', writeback=True)
    for user in db:
        db[user]['balance'] += db[user]['num_of_apps']
        db[user]['num_of_apps'] = 0
    db.close()
