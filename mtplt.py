from numpy import *
import plotly as py
from plotly.graph_objs import *

#just a sphere
theta = linspace(0,2*pi,100)
phi = linspace(0,pi,100)
x = outer(cos(theta),sin(phi))
y = outer(sin(theta),sin(phi))
z = outer(ones(100),cos(phi))  # note this is 2d now

data = Data([
    Surface(
        x=x,
        y=y,
        z=z
    )
])
layout = Layout(
    title='Bloch sphere',
    autosize=False,
    width=500,
    height=500,
    margin=Margin(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = Figure(data=data, layout=layout)
print (py.plot(fig, filename='bloch-sphere-surface'))