import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
#import scipy
from scipy.stats import skew, kurtosis

def mygame():
    for i in range(run):
        random_walk = [0]#array to count the no of dice thrown in each simulation
        count=0
        flag=True
        while flag:
            #untill a 6 comes, the game cannot start
            start=np.random.randint(1, 7)
            random_walk.append(start)
            if start==6:
                flag=False
        while count is not 100:
            dice = np.random.randint(1, 7)
            random_walk.append(dice)
            ship=count
            count+=dice
            if dice == 6: #if 6 comes then we need to throw a dice once again
                temp1 = np.random.randint(1, 7)
                random_walk.append(temp1)
                if temp1==6:
                    temp2=np.random.randint(1, 7)
                    random_walk.append(temp2)
                    if temp2==6: #if there is 3 times continuos 6, then there is a null i.e. all the 3 sixes goes in vanish
                        temp3=np.random.randint(1, 6) #to reduce the complexity we have chosen that there can't be 4 times continuos six occuring on dice
                        random_walk.append(temp3)
                        count -=dice
                        count+=temp3
                    else:
                        count+=6
                        count+=temp2
                else:
                    count+=temp1
            if count in a1: #checking the snakes
                temp=a1.index(count)
                #a3.append(temp+1)
                a3[temp]+=1
                count=a2[temp]
            if count in b1: #checking the ladders
                temp=b1.index(count)
                #b3.append(temp+1)
                b3[temp]+=1
                count=b2[temp]
            if count>100: #the score can't go more than 100, because if we are 98 then we must get 2 in order to win
                count=ship
        #print(len(random_walk))
        #print(sum(random_walk))
        #print(count)pr
        all_walks.append(len(random_walk)) #adding the no. of dice thrown in each simulation to the array all_walks

def histogram_data():
    a = plt.hist(all_walks, bins=400, color="red")
    plt.xlabel('Number of dice thrown')
    plt.ylabel('Frequency')
    plt.title('Random Walk Result - '+ str(run) +' Simulations')
    plt.axvline(statistics.mean(all_walks) - 1*statistics.stdev(all_walks))
    plt.axvline(statistics.mean(all_walks) - 2*statistics.stdev(all_walks))
    plt.axvline(statistics.mean(all_walks) - 3*statistics.stdev(all_walks))
    plt.axvline(statistics.mean(all_walks) + statistics.stdev(all_walks))
    plt.axvline(statistics.mean(all_walks) + 2*statistics.stdev(all_walks))
    plt.axvline(statistics.mean(all_walks) + 3*statistics.stdev(all_walks))
    plt.show(a)

def cummulative_probability_dist():
    m=statistics.mean(all_walks)
    s=statistics.stdev(all_walks)
    prob=[]
    cumm=[]
    x = np.array(all_walks) 
    v=np.unique(x)
    v.sort()
    for i in v:
        cumm.append(sum(prob))
        x=((i-m)**2)/(2*s*s)
        y=1/(s*math.sqrt(2*math.pi))
        z=y*math.exp(-x)
        prob.append(z)

    t=list(range(1,len(v)+1))
    c=plt.plot(v, cumm, color="red")
    plt.xlabel('Number of dice thrown')
    plt.ylabel('Probabilty of winning')
    plt.title('Cumulative Distribution Curve')
    plt.show(c)

def scatter_plot():
    r=list(range(1,run+1))
    c=plt.scatter(r, all_walks, label= "stars", color= "red", marker= "*", s=2)
    plt.xlabel('Simulation Number')
    plt.ylabel('Number of dice thrown')
    plt.title('Random Walk Process ' + str(run) + ' Simulations(Scatter Plot)')
    plt.show(c)

def count_ladder_and_snake():
    x=list(range(1,8))
    ax=plt.bar(x,a3)
    plt.xlabel('Snake Number')
    plt.ylabel('Frequency (Number of times used)')
    plt.title('Number of times each snake is used')
    plt.show(ax)
    y=list(range(1,9))
    ay=plt.bar(y,b3)
    plt.xlabel('Ladder Number')
    plt.ylabel('Frequency (Number of times used)')
    plt.title('Number of times each ladder is used')
    plt.show(ay)

def statistical_properties():
    print("Mean: " + str(statistics.mean(all_walks)))
    print("Median: " + str(statistics.median(all_walks)))
    print("Mode: " + str(statistics.mode(all_walks)))
    print("Standard Deviation: " + str(statistics.stdev(all_walks)))
    print("Variance: " + str(statistics.variance(all_walks)))
    print("Coefficient of Variation: " + str(statistics.stdev(all_walks)/statistics.mean(all_walks)))
    print("Skewness: " + str(skew(all_walks)))
    print("Kurtosis: " + str(kurtosis(all_walks)))
    print("66% of data lies between " + str(statistics.mean(all_walks) - statistics.stdev(all_walks)) + " and " + str(statistics.mean(all_walks) + statistics.stdev(all_walks)))
    print("96% of data lies between " + str(statistics.mean(all_walks) - 2 * statistics.stdev(all_walks)) + " and " + str(statistics.mean(all_walks) + 2 * statistics.stdev(all_walks)))
    print("99% of data lies between " + str(statistics.mean(all_walks) - 3 * statistics.stdev(all_walks)) + " and " + str(statistics.mean(all_walks) + 3 * statistics.stdev(all_walks)))

if __name__ == "__main__":
    run = 1000000 #simulations
    all_walks = [] #array to store the no. of dice thrown in each simulation
    #snakes
    a1=[17,54,62,64,93,95,98]
    a2=[7,34,25,60,73,75,79]
    a3=[0]*7
    #ladders
    b1=[2,4,9,21,28,51,72,80]
    b2=[38,23,31,58,84,67,91,99]
    b3=[0]*8
    mygame()
    plt.style.use("ggplot")
    histogram_data()
    cummulative_probability_dist()
    scatter_plot()
    count_ladder_and_snake()
    statistical_properties()