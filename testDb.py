from inMemoryDb import InMemoryDB

db = InMemoryDB()

#should print None
print(db.get("A"))

#should raise exception
try:
    db.put("A", 5)
except Exception as e:
    print(e)

#start a new transaction
db.begin_transaction()

#set value of A to 5 within transaction
db.put("A", 5)

#should print 5 (visible inside transaction)
print(db.get("A"))

#update A to 6 within transaction
db.put("A", 6)

#commit the transaction
db.commit()

#should print 6 (now visible in main state)
print(db.get("A"))

#should raise exception (no open transaction)
try:
    db.commit()
except Exception as e:
    print(e)

#should raise exception (no open transaction)
try:
    db.rollback()
except Exception as e:
    print(e)

#should print None (B doesn't exist yet)
print(db.get("B"))

#start a new transaction
db.begin_transaction()

#set B to 10 within transaction
db.put("B", 10)

#rollback the transaction
db.rollback()

#should print None (B was never committed)
print(db.get("B"))
