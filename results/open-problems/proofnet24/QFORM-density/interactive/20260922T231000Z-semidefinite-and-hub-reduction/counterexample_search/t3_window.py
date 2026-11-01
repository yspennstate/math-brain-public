import numpy as np
from lib import *
# check hub_window_values against brute force for random a,T,R and a 2-interval hub law
rng=np.random.default_rng(0)
fh=PWLaw([-0.7,0.1],[-0.3,0.7])
for a in [0.0,0.3,-0.5]:
    T=rng.normal(0,0.3,5); R=rng.normal(0,0.3,5); sv=np.array([-0.2,0.0,0.15]); d=0.05
    ex=hub_window_values(a,T,R,sv,fh,d)
    xs=np.linspace(-1,1,2000001); fx=fh.pdf(xs); dx=xs[1]-xs[0]
    bf=np.array([[np.sum(fx*(np.abs(a*xs**2+2*t*xs+r-s)<=d))*dx for s in sv] for t,r in zip(T,R)])
    print(a, np.abs(ex-bf).max())
