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
    """, height=300
)

st.subheader('Sincronización Caótica')
components.html(
    """
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
      <div style="text-align: justify">
      La sincronización caótica es un fenómeno en el que dos o más sistemas caóticos pueden ajustar su dinámica para 
      volverse idénticos o similares. Esto puede suceder cuando los sistemas están acoplados por alguna forma de 
      interacción o comunicación, como una fuerza impulsora común, una señal de retroalimentación o un entorno compartido. 
      La sincronización caótica tiene aplicaciones en varios campos, como la comunicación segura, las redes neuronales y 
      las redes complejas.
      </div>
    """, height=200
)

st.subheader('Atractor de Rossler')
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="text-align: justify">
      El atractor de Rössler describe el comportamiento de un sistema dinámico de tres ecuaciones 
      diferenciales ordinarias no lineales. Fue estudiado originalmente por Otto Rössler en la década de 1970 y 
      exhibe dinámicas caóticas y propiedades fractales. El atractor de Rössler se puede utilizar para 
      modelar el equilibrio en reacciones químicas y otros fenómenos. Las ecuaciones que definen el atractor de Rössler son:
      donde A, B y C son los parametros de equilibrio. El atractor de Rössler tiene forma de espiral que se tuerce y gira 
      en tres dimensiones. Tiene algunas similitudes con el atractor de Lorenz, pero es más simple y tiene solo una variedad.
    </div>
    """, height=200
)

r'''
$$\dot{x} = -(y+z)$$
'''
r'''
$$\dot{y} = x+ay$$
'''
r'''
$$\dot{z} = b+z(x-c)$$
'''
http_chen = 'https://omargomez2.github.io/cryptochaos/plot_rossler.png'
st.image(http_chen, caption= 'Rossler Attractor', width=500)


st.subheader('Atractor de Lorenz')
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="text-align: justify">
    El atractor de Lorenz es un modelo matemático de un sistema dinámico (caótico) que exhibe una dependencia sensible de 
    las condiciones iniciales. Fue introducido por primera vez por Edward Lorenz en 1963 como una representación 
    simplificada de la convección atmosférica. El atractor de Lorenz consta de tres ecuaciones diferenciales 
    acopladas que describen la evolución de tres variables: x, y y z. Las ecuaciones tienen tres parámetros: sigma, rho y beta, 
    que controlan la forma y el comportamiento del atractor. El atractor de Lorenz es uno de los ejemplos más 
    famosos de un atractor extraño, un conjunto de puntos en el espacio de fase que tiene una estructura fractal 
    y atrae trayectorias cercanas.
    </div>
    """, height=200
)

r'''
$$\dot{x} = \sigma(-x+y)$$
'''
r'''
$$\dot{y} = -xz+\rho x-y$$
'''
r'''
$$\dot{z} = xy-\beta z$$
'''

http_chen = 'https://omargomez2.github.io/cryptochaos/plot_lorenz.png'
st.image(http_chen, caption= 'Lorenz Attractor', width=500)


st.subheader('Atractor de Chen')
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="text-align: justify">
    El atractor de Chen es un tipo de atractor de desplazamiento múltiple propuesto por Guanrong Chen, un 
    matemático chino e investigador del caos. El atractor de Chen es un sistema dinámico tridimensional 
    que exhibe un comportamiento caótico y tiene una estructura geométrica compleja. El atractor de Chen 
    se puede describir mediante un sistema de tres ecuaciones diferenciales ordinarias no lineales con tres 
    parámetros. El atractor de Chen tiene algunas similitudes con el atractor de Lorenz, pero también algunas 
    diferencias, como la forma y el número de puntos de equilibrio.
    </div>
    """, height=200
)
r'''
$$\dot{x} = a(y-x)$$
'''
r'''
$$\dot{y} = (c-a)x-xz+cy$$
'''
r'''
$$\dot{z} = xy-bz$$
'''

http_chen = 'https://omargomez2.github.io/cryptochaos/plot_chen.png'
st.image(http_chen, caption= 'Chen Attractor', width=500)



st.subheader('Atractor de Sprott')
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="text-align: justify">
    El atractor de Sprott es un tipo de atractor caótico que tiene forma de mariposa y dimensión fraccionaria. 
    Fue descubierto por Julien C. Sprott, físico e investigador del caos de la Universidad de Wisconsin-Madison. 
    El atractor de Sprott se puede generar mediante un mapa cuadrático tridimensional con términos no lineales. 
    El atractor de Sprott tiene propiedades interesantes como la multiestabilidad, la coexistencia de múltiples 
    atractores y la sensibilidad a las condiciones iniciales. El atractor Sprott se puede utilizar para modelar 
    fenómenos complejos como redes neuronales, sistemas láser y percepción.
    </div>
    """, height=200
)

r'''
$$\dot{x} = a(y-x)$$
'''
r'''
$$\dot{y} = bxz$$
'''
r'''
$$\dot{z} = c-xy$$
'''

http_chen = 'https://omargomez2.github.io/cryptochaos/plot_sprott.png'
st.image(http_chen, caption= 'Sprott Attractor', width=500)
