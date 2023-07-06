import math
import numpy as np


#Inlet Values from HMI
Q_entrance = 270 #scfm
ch4_percent = 0.614
T_entrance = 90.37 #Farenheit
P_entrance = 5.68 #in WC

#Converting to metric units
Q_entrance = Q_entrance * 1.69 #m^3/hour
T_entrance = (T_entrance-32)/1.8 #Celsius
P_entrance = P_entrance*249.088908333 #Pascals

#RNG density at conditions
molecular_mass = (ch4_percent*16.04)+((1-ch4_percent)*44.01)
molpervol = (P_entrance/1000)/8.314/(273.15+T_entrance)
rho_rng = molecular_mass*molpervol #kg/m^3



def h2s():

    P1 = P_entrance
    g = 9.81
    h = 8*0.3048 #height of the H2S removal (convert 8 feet to meters)

    P2 = rho_rng*g*h+P1
    print(f'For inlet pressure {P_entrance:.5f} pascals, the outlet pressure is {P2:.5f} pascals')
'''
def flt():
    A1 = math.pi*3*3 * 0.00064516 #square meters
    A2 = math.pi*3*3 * 0.00064516 #square meters
    A3 = math.pi*0.75*0.75 * 0.00064516 #square meters
    rho1 = rho_rng
    rho2 = rho_rng
    rho3 = 1000 #kg/m^3

    V1 = Q_entrance/A1/3660 #m/s

'''

#def hx1():
print('new commit 2')