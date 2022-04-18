#predicting number of new students for nxt year
import string
from turtle import color
import pandas as pd
import statistics
import matplotlib.pyplot as plt
#importing the dataset
dataset = pd.read_csv("PATH")

n = len(dataset.axes[0]) #getting number of rows
yr = dataset["x"].tolist()
Y = dataset["y"].tolist()
md = statistics.median(yr)  #calculating the median of the years
X=[]
XY=[]
XX=[]

#Calculating X, X*Y, X^2
for i in range(len(yr)):
    X.append(yr[i]-md)
    XY.append(X[i]*Y[i])
    XX.append(X[i]**2)

#calculating sum of X, X*Y, X^2
SX = sum(XX)
SXY = sum(XY)
SY = sum(Y)

a = SY/n   #calculating a and b
b = SXY/SX

l = len(X)
c = X[l-1]+1
r = yr[l-1]+1

yr.append(r)

ans = a + b*c  #equation for predicting the number of students for the next academic year

Y.append(ans)

plt.xlabel("year")
plt.ylabel("Number of students")
plt.bar(yr,Y)

for x,y in zip(yr,Y):

    label = "{:.2f}".format(y)

    plt.annotate(label,
                 (x,y), 
                 textcoords="offset points", 
                 xytext=(0,10),
                 ha='center')
                 
plt.show()   #displaying graph

print("predicted number of students for the next academic year("+str(r)+"): "+ str(ans))
