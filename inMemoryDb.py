#implementing in memory key value database w transaction support
class InMemoryDB:
   def __init__(self):
      self.db = {}
      self.temp = None

   def begin_transaction(self):
      #start a new transaction
      if self.temp is not None:
         raise Exception("transaction already in progress")
      #make a shallow copy of the current db
      self.temp = self.db.copy()

   def put(self, key, val):
      #store/update key value pair in the transaction
      if self.temp is None:
         raise Exception("no transaction in progress")
      self.temp[key] = val

   def get(self, key):
      #get value from main db if no transaction else from temp
      if self.temp is None:
         return self.db.get(key, None)
      return self.temp.get(key, None)

   def commit(self):
      #commit changes to main db
      if self.temp is None:
         raise Exception("no transaction in progress")
      self.db = self.temp
      self.temp = None

   def rollback(self):
      #discard transaction changes
      if self.temp is None:
         raise Exception("no transaction in progress")
      self.temp = None
