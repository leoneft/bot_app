import shelve

db = shelve.open('db', writeback=True)
with open('numbers.txt', 'w') as f:
    for user in db:
        f.write(db[user]['phone'] + '\n')
db.close()
