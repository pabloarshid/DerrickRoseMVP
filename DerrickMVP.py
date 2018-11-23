import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def edittable(csvname, name):
    Dataframe = pd.read_csv(csvname)
    Dataframe = Dataframe.rename(columns={"Unnamed: 5": '@', "Unnamed: 7": 'outcome'})
    Dataframe.loc[Dataframe['@'] == "@",'@'] = "away"
    Dataframe['@'] = Dataframe['@'].fillna('home')
    Dataframe['Difference'] = Dataframe['outcome'].map(lambda x: str(x)[1:])
    Dataframe['outcome'] = Dataframe['outcome'].map(lambda x: str(x)[:1])
    Dataframe['PlayerName'] = name
    return Dataframe

dwight = edittable("Dwight.csv", "Dwight")
rose = edittable("Rose.csv", "Rose")
lebron = edittable("Lebron.csv","Lebron")
kobe = edittable("Kobe.csv", "Kobe")
rose20092010 = edittable("rose0910.csv", "Rose")
lebron20092010 = edittable("lebron0910.csv", "lebron")
Kobe20092010 = edittable("kobe0910.csv", "kobe")
Kd20092010 = edittable("kd0910.csv", "kd")
Dwight092010 = edittable("dwight0910.csv", "Dwight")
combined = pd.concat([rose, dwight, lebron, kobe])
combined0910 = pd.concat([rose20092010, Dwight092010, lebron20092010, Kobe20092010, Kd20092010] ) 

sns.set_style("darkgrid")

sns.set(rc={'figure.figsize':(11.7,8.27)})

# # plot boxplot
ax = sns.boxplot(x="PlayerName", y="GmSc",hue = "@", data=combined, 
                 showcaps=False,
                 showfliers=False,palette="muted", whiskerprops={'linewidth':0})

sns.swarmplot(x="PlayerName", y="GmSc",hue = "@", data=combined, zorder=0, dodge=False)

ax1 = ax.get_figure()
ax1.savefig("1011MVPPTsBreakdown.png")



ax = sns.boxplot(x="PlayerName", y="GmSc",hue = "@", data=combined0910, 
                 showcaps=False,
                 showfliers=False,palette="muted", whiskerprops={'linewidth':0})

sns.swarmplot(x="PlayerName", y="GmSc",hue = "@", data=combined0910, zorder=0, dodge=False)

ax1 = ax.get_figure()
ax1.savefig("0910MVPPTsBreakdown.png")

# Get current size
fig_size = plt.rcParams["figure.figsize"]
 
# Prints: [8.0, 6.0]
# Set figure width to 12 and height to 9
fig_size[0] = 18
fig_size[1] = 15
plt.rcParams["figure.figsize"] = fig_size

fig = plt.figure()
ax1 = sns.lmplot(x="G", y="PTS", hue= "outcome", col= "PlayerName", data=combined0910, lowess=True, palette=dict(W="g", L="r"))
ax2 = sns.lmplot(x="G", y="PTS", hue= "outcome",col= "PlayerName", data=combined, lowess = True,palette=dict(W="g", L="r"))

ax1 = sns.lmplot(x="G", y="GmSc", hue= "outcome", col= "PlayerName" , data=combined0910, lowess=True,palette=dict(W="g", L="r"))
ax2 = sns.lmplot(x="G", y="GmSc", hue= "outcome",col= "PlayerName", data=combined, lowess = True,palette=dict(W="g", L="r"))
ax1 = sns.lmplot(x="G", y="+/-", hue= "outcome", col= "PlayerName", data=combined0910, lowess=True,palette=dict(W="g", L="r"))
ax2 = sns.lmplot(x="G", y="+/-", hue= "outcome",col= "PlayerName", data=combined, lowess = True,palette=dict(W="g", L="r"))