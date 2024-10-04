"""
player 1:
id => 1
name => Cristiano Ronaldo
yeraOfBirth => 1985
nationality => Portugal
current_team => Portugal
history => Jventus, Real Madrid, Portugal


player 2:
id => 2
name => Lionel Messi
yearofBirth => 1987
nationality



"""

id = input("please enter the player's id")
"""
player = {
    1 : {
    "name" : "Cristiano Rolando",
    "yearOfBirth" : 1985,
    "nationality" : "Portugal",
    "current_team" : "Portugal",
    "history" : {
        "team1" : "Juventus",
        "team2" : "Real Madrid",
        "team3" : "Portugal"
        }
    },
    2 : {
    "name" : "Lionel Messi",
    "yearOfBirth" : 1985,
    "nationality" : "Portugal",
    "current_team" : "Portugal",
    "history" : {
        "team1" : "Juventus",
        "team2" : "Real Madrid",
        "team3" : "Portugal"
    }

    }
}"""

players = {}

id = input("oyuncu id")
name = input("oyuncu adı")
yearOfBirth = input("doğum yılı")
nationality = input("milliyeti")

current_team = input("şuanki takımı")
history = input("oynadığı yeler")

players.update({
    id :{
        "name" : name,
        "yearfBirth" : yearOfBirth,
        "nationality" : nationality,
        "yearOfBirth" : yearOfBirth,
        "current_team" : current_team,
        "history" : history.split(',')

    }
})