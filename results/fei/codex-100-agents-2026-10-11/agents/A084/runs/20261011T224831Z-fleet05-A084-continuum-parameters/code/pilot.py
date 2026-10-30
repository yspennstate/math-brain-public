import math,json
def h(x):
    return -x*math.log2(x)-(1-x)*math.log2(1-x) if 0<x<1 else 0.
def F(p,q):
    r=4*q*(1-q)
    m=[(1-2*p*q)**2,4*p*(1-p)*q*q,p*p*r,p*(1-p)*r]
    return 2*h(p*r)-p*h(r)+sum(x*math.log2(x) for x in m if x)
for p in [.01,.125,.25,.49,.5,.51,.75,.99]:
    print(p,[(q,round(F(p,q),7)) for q in [.001,.1,.25,.4,.49,.5,.51,.6,.75,.9,.999]])
