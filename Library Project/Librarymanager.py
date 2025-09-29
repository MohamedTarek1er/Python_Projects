class Library:
    def __init__(self, gameslist, lenders, donors):
        self.gameslist = gameslist
        self.lenders = lenders
        self.donors = donors
        
    def games(self):
        return f"{self.gameslist}"
    
    def lend(self, gamename, name):
        if gamename in self.gameslist:
            self.gameslist.remove(gamename)
            self.lenders[gamename] = name
            print("***Game lended successfully!! Return it within a week :) ***")
        else:
            print("No such game available in the directory!")

    def returnb(self, name, gamename):
        if gamename in self.lenders and self.lenders[gamename] == name:
            self.gameslist.append(gamename)
            self.lenders.pop(gamename)
            print("***Game returned successfully!***")
        else:
            print("Invalid return request! Either the game wasn't borrowed or the name doesn't match.")

    def donate(self, kindname, newgame):
        print("Thanks", kindname, "a lot!!!")
        self.gameslist.append(newgame)
        self.donors.update({kindname: newgame})

