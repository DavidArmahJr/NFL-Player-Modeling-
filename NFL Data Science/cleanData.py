import pandas as pd



## Removes unnecessary characters from Player names and Fixes abnormal Column names
def cleanPlayerName(df):
    try:
        for i in df['Player']:
            player = i
            #print(player)

            L = False
            R = 0

            while R < len(player):

                if player[R] == ' ' and L == False:
                    L = True
                elif player[R] == '.' and L == True:
                    df['Player'] = df['Player'].replace(player, player[:R])
                    break
                R += 1
        df['Player'] = df['Player'].str[:-1]
        
        #df.index = df['Player']
    except:
        print('Error trying to clean player names')

#Removes unnecessary characters from Team names
def cleanTeamName(df):
    try:
        for i in df['Team']:
            team = i

            L = False
            R =0

            while R < len(team):
                if (team[R].isupper() or team[R].isdigit()) and L == False:
                    L = True    
                elif team[R].isupper() and L == True:
                    df['Team']= df['Team'].replace(team, team[:R])
                    break    
                elif team[R] == " ":
                    L = False
                R += 1  
    except:
        print('Error trying to clean team names')

def cleanPlayerData(df):
    df['Lg'] = df['Lg'].str.replace('[A-Za-z]', '', regex=True)
    df['Lg']=df['Lg'].astype('float64')
    
def cleanTeamData(df):
    df.columns = df.columns.str.replace(u'\xa0', '_')
