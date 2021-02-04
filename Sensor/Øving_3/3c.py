import numpy as np
nrand = int (1e5 )


### Constants ####
C = 343 #c is the speed of sound
#####



# uniformt fordelte verdier mellom 0.0 og 1.0

m = np.ones(nrand)




d=2*m
#tau=m

#d = np.random.uniform(low=3, high=4, size=nrand) # den ideele d verdien
tau = np.random.uniform(low=0.1, high=1.0, size=nrand) #den ideele tau verdien
tauvec = (1 + 2*0.01*( np . random . rand ( nrand ) - 0.5)) # delta d
dvec = (1 + 2*0.02*( np . random . rand ( nrand ) - 0.5)) # telta tau

teta_ideell = np.arccos(tau/d)
teta_feil = np.arccos((tau*tauvec/(d*dvec)))



relativ_feil = teta_feil/teta_ideell








print("Max error:",np.max(relativ_feil))
