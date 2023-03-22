import matplotlib.pyplot as plt
from scipy import stats

x = [394.69,394.49,394.78,394.93,395.13,395.96,396.31,396.56,396.80,396.84,396.36,
     396.37,396.25,396.66,396.40,396.02,395.65,396.02,395.88,395.67]
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
