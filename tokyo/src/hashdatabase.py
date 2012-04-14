from tokyo.cabinet import *

hdb = HDB()

hdb.open("db/hashdatabase.tch", HDBOWRITER | HDBOCREAT)

for key, value in [("foo", "hop"), ("bar", "step"), ("baz", "jump")]:
    hdb[key] = value

for key in hdb:
    print(key, hdb[key])

hdb.close()
