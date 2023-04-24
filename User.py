import bcrypt


class User:
    salt = bcrypt.gensalt()
    # salt = 'hogriderisgigachad'
    # salt = 'mahnunitsnotevenoneminute'



    def __init__(self, username, password):
        
        self.__username = username
        b = password.encode('utf-8')
        self.__hashedpass = bcrypt.hashpw(b, User.salt)
        self.__transactions = []
        # start session and assign session id?
        # store user info into database

        

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def addTransaction(self, transaction):
        self.__transactions.append(transaction)
    
# if __name__ == "__main__":
#     user = "test"
#     password = "12345"
#     user = User(user, password)
#     print(user.getUsername())
