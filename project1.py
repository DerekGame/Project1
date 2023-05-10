#Importing Pandas package 
import pandas as pd


#Creating a Dictionary
print("Points Per Season")
data = {'Curry': [17.5, 18.6, 14.7, 22.9, 24, 23.8, 30.1, 25.3, 26.4, 27.3, 20.8, 32, 25.5, 29.4],
        'Thompson': [12.5, 16.6, 18.4, 21.7, 22.1, 22.3, 20, 21.5, 20.4, 22.1, None, None, None, None],
        'Green': [2.9, 6.2, 11.7, 14, 10.2, 11, 7.4, 8, 7, 7.5, 8.1, None, None, None],
        'Payton': [3.3, 2.5, 3.5, 3.7, 3.9, 2.5, 7.1, 4.1, None, None, None, None, None, None],
        'Poole': [8.8, 12, 18.5, 20.8, None, None, None, None, None, None, None, None, None, None]
        }

# create a pandas DataFrame from the dictionary
player_stats = pd.DataFrame(data)

# calculate the average points per game for each player over their career
player_averages = player_stats.mean()

# display the DataFrame
print(player_stats)

# display the average points per game for each player
print("Career Average")
print(player_averages)



#Create a dataframe
#df = pd.DataFrame(d)

# Display Original dataframe
#print("Created Dataframe:\n",df,"\n")

# Calculating mean
#df['Mean'] = df.mean(axis=1)

# Display modified DataFrame
#print("Modified DataFrame:\n",df)


#people = pd.DataFrame(data, index=['Curry', 'Thompson', 'Green', '2000s'])
#print(people)

#nba = pd.DataFrame(pd.read_csv('Book1.csv.numbers'))
#print(nba)