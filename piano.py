# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:59:00 2019

@author: ftrub
"""

import numpy as np 
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt


def sine_wave(t,f) : 
    """valeur ton pur 
    de fréquence f en hertz en fonction du temps t en seconde"""
    return(np.sin(2*np.pi*t*f))
 


x=[i/299 for i in range(300)]
y=[sine_wave(i,4) for i in x]
plt.plot(x,y)    

def square_wave(t,f):
    """valeur onde en créneau 
    de fréquence f en herts en fonction du temps t en seconde"""
    return(1.0-2*((int(t*2*f))%2))

x=[i/299 for i in range(300)]
y=[square_wave(i,4) for i in x]
plt.plot(x,y)    

def sawtooth_wave (t,f):
    """valeur onde en dents de scie 
    de fréquence f en herts en fonction du temps t en seconde"""
    return(-1+((t*2*f)%2))

x=[i/299 for i in range(300)]
y=[sawtooth_wave(i,4) for i in x]
plt.plot(x,y)  

def triangle_wave(t,f):
   """valeur onde en triangle 
   de fréquence f en herts en fonction du temps t en seconde"""
   return 1

x=[i/299 for i in range(300)]
y=[triangle_wave(i,4) for i in x]
plt.plot(x,y) 

sample_rate=44100 #nombre d'échantillons par seconde
la440=440

def frequence_note(nb_demis_tons): 
    """fréquence en hertz en fonction de la distance en demis-tons du la440"""
    return la440*2**(nb_demis_tons/12)

data=[sine_wave(i/sample_rate,frequence_note(0)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(2)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(4)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(0)) for i in range (sample_rate-5000)]\
    +[0 for i in range (5000)]\
    +[sine_wave(i/sample_rate,frequence_note(0)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(2)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(4)) for i in range (sample_rate)]\
    +[sine_wave(i/sample_rate,frequence_note(0)) for i in range (sample_rate)]
wav.write('frère_jacques.wav',sample_rate,np.array(data))

def jouer_note(nb_demis_tons,duree,forme_d_onde):
    """crée une onde échantillonnée 
    nb_demis_tons : écarts au la 440 en demis-tons
    duree : en secondes"""
    return [forme_d_onde(i/sample_rate,frequence_note(nb_demis_tons))
            for i in range (int(sample_rate*duree))]

def partition(notes,forme_d_onde):
    """échantillonne une suite de notes
    notes : liste de tuples (couples) demis-tons du la, duree 
    forme d'onde : fonction d'onde choisie"""
    data=[]
    for nb_demis_tons,duree in notes : 
        data+=jouer_note(nb_demis_tons,duree,forme_d_onde)
    return data
    
def export_partition(data,nom) : 
    """exporte une suite de note en fichier wave"""
    return wav.write(nom+'.wav',sample_rate,np.array(data))


        




