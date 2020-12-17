#Resolution de l'equation differentielle (1 variable): y'+y=x
#Guillaume Vige 11/10/2018

from scipy.integrate import odeint
from pylab import * # pour les courbes


def deriv(y,x):
# renvoie y'
	return y-x

xtab = linspace(0.0,4.0,1000) #integration de 0 a 4 avec 1000 points
yinit = 0.9  # initial value
y =odeint(deriv,yinit,xtab)
figure()
plot(xtab,y)
xlabel("x")
ylabel("y")
show()
