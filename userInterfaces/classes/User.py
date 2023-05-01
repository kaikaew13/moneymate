import bcrypt
import persistent


class User(persistent.Persistent):
    salt = bcrypt.gensalt()
    # salt = 'hogriderisgigachad'
    # salt = 'mahnunitsnotevenoneminute'

    def __init__(self, username, password):

        self.__username = username
        b = password.encode('utf-8')
        self.__hashedpass = bcrypt.hashpw(b, User.salt)
        self.__transactions = []
        self.__goal = []
        # start session and assign session id?
        # store user info into database
        print('User created')

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getHashedpass(self):
        return self.__hashedpass

    def addTransaction(self, transaction):
        self.__transactions.append(transaction)

    def addGoal(self, goal):
        self.__goal.append(goal)

# if __name__ == "__main__":
#     user = "test"
#     password = "12345"
#     user = User(user, password)
#     print(user.getUsername())
