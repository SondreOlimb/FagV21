import numpy as np
nrand = int (1e4 )


### Constants ####
C = 343 #c is the speed of sound


#######
#
m = np.ones(nrand)




d = np.random.uniform(low=3, high=3, size=nrand) # den ideele d verdien
tau = np.random.uniform(low=0.1, high=1.0, size=nrand) #den ideele tau verdien
tauvec = (1 + 2*0.01*( np . random . rand ( nrand ) - 0.5)) # delta d
dvec = (1 + 2*0.02*( np . random . rand ( nrand ) - 0.5)) # telta tau

"""
oppgave 2c

"""


f_ideell = tau/d
f_feil = tau*tauvec/(d*dvec)



relativ_feil = f_feil/f_ideell








print("Max error:",np.max(relativ_feil))




