#William Van Leeuwen
#10/03/2021
#COIS 1400
#Lab 8

#import needed packages
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

iris = data('iris') #set the dataset at iris

#create basic scatter plot, sepal
plt.subplot(221)
plt.scatter(iris.iloc[:,0], iris.iloc[:,1],s=8) #set x coord as sepal length and y as sepal width
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()

#create basic scatter plot, petal
plt.subplot(222)
plt.scatter(iris.iloc[:,2], iris.iloc[:,3],s=8) #set x coord as sepal length and y as sepal width
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()




#for loop to count each species type
plt.subplot(223)
setosa = 0
versicolor = 0
virginica = 0
for i in iris.iloc[:, 4]:
    if(i == 'setosa'):
        setosa += 1
    if(i == 'versicolor'):
        versicolor += 1
    if(i == 'virginica'):
        virginica += 1
#plot basic pie chart
sizes = [setosa, versicolor, virginica]
labels = 'setosa', 'versicolor', 'virginica'
plt.pie(sizes, labels=labels, autopct='%1.1f%%')




#histogram
plt.subplot(224)
bins = 25
plt.hist(iris.iloc[:,0], bins)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")


plt.suptitle("William Van Leeuwen \n 0697505")
plt.show()