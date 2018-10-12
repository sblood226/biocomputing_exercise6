# Problem 1
filename = '/Users/ryanblood/IntroBioComp/toHead.txt' # 'home/AD/user/BioComputing/needsHead.txt'
headLength = 10
header = ""
f = open(filename,'r')
for i in range(headLength):
    header += f.readline()
f.close
print header

#Problem 2
import pandas as pd
import numpy as np
data = pd.read_csv('./iris.csv', header =0 )
print 'Pring last rows in last two columns ',data.iloc[-2:,-2:]
speciesList = []
for i in range(len(data.iloc[:,4])):
    if data.iloc[i,4] not in speciesList:

        speciesList.append(data.iloc[i,4])
likeArray = np.zeros(len(speciesList))

for i in range(len(data.iloc[:,4])):
    for species in range(len(likeArray)):
        if data.iloc[i,4] == speciesList[species]:
                likeArray[species] +=1

print 'Number of counts for each of the species: ', likeArray

#Getting sepal width rows
rowsBig = data.loc[data['Sepal.Width']>3.5]

#Writing setosa file
rowSetosa = data.loc[data['Species']=='setosa']
rowSetosa.to_csv('setosa.csv', sep=',')


#Petal length stats
rowV = data.loc[data['Species']=='virginica']
petalLengths_mean=np.mean(rowV.iloc[:,2])
petalLengths_max=np.max(rowV.iloc[:,2])
petalLengths_min=np.min(rowV.iloc[:,2])


