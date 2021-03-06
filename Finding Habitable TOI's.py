import requests
url = 'https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv'
r = requests.get(url, allow_redirects=True) 
open('All Rows (CSV)', 'wb').write(r.content) #this downloads and saves the file to wherever this notebook is saved
r.status_code #200 means the request was successful, 404 indicates an unsuccessful request

import pandas as pd
pd.set_option('display.max_columns', 100)
data = pd.read_csv("All Rows (CSV)")
exofop = pd.DataFrame(data)

#Planets with insolation flux 0.5-1.5 earth flux
P_Insol = exofop['Planet Insolation (Earth Flux)']
exofop.loc[(P_Insol >= 0.5) & (P_Insol <= 1.5)]

#Planets with an earth radius of 0.5-2.5
P_Rad = exofop['Planet Radius (R_Earth)']
exofop.loc[(E_Rad >= 0.5) & (E_Rad <= 2.5)]

#Planets with both conditions
exofop.loc[(P_Insol >= 0.5) & (P_Insol <= 1.5) & (P_Rad >= 0.5) & (P_Rad <= 2.5)]

#Zink and Hansen (2019) parameters
Sol_Rad = exofop['Stellar Radius (R_Sun)']
Log = exofop['Stellar log(g) (cm/s^2)']
Depth = exofop['Depth (ppm)']
Temp = exofop['Stellar Eff Temp (K)']
OP = exofop['Period (days)']
#Semimajor axis constraint will be applied via an approximation of Kepller's 3rd law (p**2 = a**3)
#Period: p = (0.95**3)**0.5 = 0.926 years = 338 days, p = (1.68**3)**0.5 = 2.18 years = 795 days
exofop.loc[(Temp >= 4200) & (Temp <= 6100) & (Sol_Rad <= 2) & (Log >= 4) & (Depth <= 1000) & (P_Rad >= 0.72) & (P_Rad <= 1.7) & (OP >= 338) & (OP <= 795)]

#Hsu et al (2020) parameters
exofop.loc[(P_Rad >= 0.75) & (P_Rad <= 1.5) & (Sol_Rad >= 0.75) & (OP >= 237) & (OP <= 500)]
