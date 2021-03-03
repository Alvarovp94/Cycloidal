# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:34:24 2021

@author: AlvaroVasquez
"""
import math 



import streamlit as st
import pandas as pd
import numpy as np


from bokeh.plotting import figure, output_file, show

inp1 = float(st.sidebar.text_input('R:', '21.5'))
inp2 = float(st.sidebar.text_input('r:', '1.5'))
inp3 = float(st.sidebar.text_input('n:', '27'))
inp4 = float(st.sidebar.text_input('E:', '0.5'))




p = figure(plot_width=700, plot_height=700)



st.title('Cycloidal reducer generator')
st.write('*Developed by ALLMATIC-Jakob Spannsysteme GmbH*')





R = inp1
r = inp2
n = inp3
E = inp4

rela = R/(E*n)


st.sidebar.write("R/(E*n) = ", rela)



cp1x = []
cp1y = []

cp12x = []
cp12y = []

cp2x = []
cp2y = []

cp3x = []
cp3y = []

cp32x = []
cp32y = []

cp33x = []
cp33y = []

cp34x = []
cp34y = []

cp4x = []
cp4y = []


for x in np.arange(0, 361, 0.1):  
    
    zi = math.radians(x)
    a1 = math.sin((1-n)*zi)
    a2 = (R/(E*n)) - math.cos((1-n)*zi)

    om = -math.atan(a1/a2)


    cx = R*math.cos(zi) - r*math.cos(zi - om) - E*math.cos(n*zi) 
    cy = -R*math.sin(zi) + r*math.sin(zi - om) + E*math.sin(n*zi)
    

    
    cp1x.append(cx)
    cp1y.append(cy)
    
for x in range(0, 361, 1): 
    
    f1 = math.radians(x)
    
    c13 = (R)*math.cos(f1) - E
    c23 = (R)*math.sin(f1)
    
    cp3x.append(c13)
    cp3y.append(c23)
    
    
for x in range(0, 360, 1): 
    
    f1 = math.radians(x)
    
    c13 = R*math.cos(f1)
    c23 = R*math.sin(f1)
    
    cp32x.append(c13)
    cp32y.append(c23)    

    
#plt.plot(cp3x, cp3y, 'b')

B1 = 360/n
    
for x in np.arange(0, 360, B1): 
    
    f1 = math.radians(x)
    
    g1 = (R)*math.cos(f1) - E
    g2 = (R)*math.sin(f1) 
        

    for x in range(0, 360, 1):  
        
        f1 = math.radians(x)
        
        c14 = r*math.cos(f1) + g1
        c24 = r*math.sin(f1) + g2
    
        cp4x.append(c14)
        cp4y.append(c24)
        
for x in np.arange(0, 360, (360/n)):  
    
    #x = x + (380/n)
    
    zi = math.radians(x)
    a1 = math.sin((1-n)*zi)
    a2 = (R/(E*n)) - math.cos((1-n)*zi)

    om = -math.atan(a1/a2)


    cx = R*math.cos(zi) - r*math.cos(zi - om) - E*math.cos(n*zi)
    cy = -R*math.sin(zi) + r*math.sin(zi - om) + E*math.sin(n*zi)
    
    cp12x.append(cx)
    cp12y.append(cy)
    



# add a line renderer
#p.line(cp32x, cp32y, color='green', line_width=4)

p.circle(cp12x, cp12y, color='red', size= 5)


p.circle(cp4x, cp4y, color='green', size= 0.5)

p.multi_line([cp1x, cp3x], [cp1y, cp3y],
             color=["blue", "navy"], alpha=[0.8, 0.3], line_width=3)

p.circle(cp12x, cp12y, color='red', size= 5)

st.bokeh_chart(p)


st.text('Victor Chuman,Alvaro Vasquez, 03.03.2021')

#chart_data = pd.DataFrame(cp1x, cp1y)
