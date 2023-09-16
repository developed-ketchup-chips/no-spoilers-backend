# object that save users information 
# ex Profile that has:  Name and Id. 
class User(object):

    def __init__(self,user_id):
      if user_id is None:
          self.new_user = True
      else:
          self.new_user = False

          #fetch all records from db about user_id
          self._populateUser() 

    # def commit(self):
    #     if self.new_user:
    #         #Do INSERTs
    #     else:
    #         #Do UPDATEs

    # def delete(self):
    #     if self.new_user == False:
    #         return False

    #     #Delete user code here

    # def _populate(self):
    #     #Query self.user_id from database and
    #     #set all instance variables, e.g.
    #     #self.name = row['name']

    # def getFullName(self):
    #     return self.name

