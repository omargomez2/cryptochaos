#--------------------
# 
# Authors: OG, RR, DP, MR
# Description: 
# url: https://omargomez2-cryptochaos-streamlit-app-hw3hh9.streamlit.app/
#-----------

import streamlit as st
import streamlit.components.v1 as components

st.title('Enfoque de cifrado de objetos JSON utilizando sincronización caótica a partir del análisis' +
                ' de un conjunto de atractores IDIPI-28')

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="text-align: justify">
      Resumen. En la actualidad en mayor o menor medida los productos software desarrollados
      se encuentran expuestos al Internet.  Internamente estos productos están conformados 
      por componentes software los cuales, muchos de ellos, se intercomunican a través del
      Internet, enviando y recibiendo información. Un formato común para el intercambio de
      información entre estos componentes es el formato JSON, Sin bien existen algunos enfoque
      para asegurar la información en este formato, se ha observado algunas amenazas que implican 
      el acceso no autorizado a la información contenida en los objetos JSON. Con el fin de ofrecer
      una alternativa al actual enfoque de cifrado de objetos JSON en la presente investigación se 
      propone el desarrollo de un enfoque de cifrado de objetos JSON utilizando sincronización caótica
      a partir de la selección de un conjunto de atractores. El enfoque a desarrollar se pretende pueda
      ser utilizado en el ámbito académico por docentes e investigadores, así como por profesionales en la 
      industria de software.
    </div>
    """,
    height=600,
)

r'''
$$\dot{x} = -(y+z)$$
$$\dot{y} = x+ay$$
$$\dot{z} = b+z(x-c)$$
'''


