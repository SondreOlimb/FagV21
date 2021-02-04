import numpy as np

###Constants###
N=8
V=240
S = 10
c=343.4

####

T_med = np.array([3.14,3.31,3.47,4.12,3.95,3.36,3.38,3.70])
T_uten = np.array([4.28,4.28,4.13,3.76,4.14,4.33,4.19,4.21])

m_med = np.mean(T_med)
m_uten = np.mean(T_uten)



def StandardDeviation(messurments, mean):
    std = 0

    for i in messurments:
        std += (i - mean)**2
    std = std/(N-1)
    return std

var_T_med = StandardDeviation(T_med, m_med)
var_T_uten = StandardDeviation(T_uten, m_uten)

print("variance by fromula for T_med:",var_T_med)
print("Variance calculated by np.var for T_med:",np.var(T_med,ddof=1))


print("variance by formula for T_uten:",var_T_uten)
print("Variance calculated by np.var for T_med:",np.var(T_uten,ddof=1))


var_alfa = (24*np.log(10*V)/(c*S))**2*(var_T_med+var_T_uten)

std_alfa = np.sqrt(var_alfa)

print("standard deviation for alfa is:",std_alfa)



"""
Oppg 1c
"""

alfa = (24*np.log(10*V)/(c*S))*(1/T_med+1/T_uten)

mean_alfa =np.mean(alfa)


def CondifenceInterval(mean,t_p,S,n):
    """
    Calculates the student t-distribution

    :param mean: The mean of the dataset
    :param t_p: Student-t distribution value from table
    :param S: The observed standard deviation
    :param n: n is length of the dataset
    :return: returns the upper en lower limit of the student t distibution
    """
    lower = mean - t_p*S/np.sqrt(n)
    upper = mean + t_p * S / np.sqrt(n)


    return lower,upper


alfa_Lower,alfa_Upper = CondifenceInterval(mean_alfa,2.365,np.sqrt(std_alfa),8)



print("\n Mean of alfa:",round(mean_alfa,3))
print("Konfidensintervall: [",round(alfa_Lower,3), round(alfa_Upper,3),"]")


