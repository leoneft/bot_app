import time
import shelve

while True:
    time.sleep(24 * 60 * 60)
    db = shelve.open('db', writeback=True)
    for user in db:
        db[user]['balance'] += db[user]['num_of_apps'] * 25
        db[user]['num_of_apps'] = 0
    db.close()
