
import string
import matplotlib
import matplotlib.pyplot as pyplot  
import numpy as np
 
if __name__ == '__main__':    
    file = open('1.txt', 'r')
    linesList = file.readlines()
#     print(linesList)
    linesList = [line.strip().split(',') for line in linesList]
    file.close()    
    print(linesList)
#     years = [string.atof(x[0]) for x in linesList]
    years = [x[0] for x in linesList]
    print(years)
    price = [x[1] for x in linesList]
    print(price)
    pyplot.plot(years, price, 'b*')#,label=$cos(x^2)$)
    pyplot.plot(years, price, 'r')
    pyplot.xlabel(years(+2000))
    #pyplot.ylabel(housing average price(*2000 yuan))
    pyplot.ylim(0, 15)
    pyplot.title('line_regression & gradient decrease')
    pyplot.legend()
    pyplot.show()