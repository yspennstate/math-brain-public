"""Small geometry search; numerical candidates only, no proof or file writes."""
from audit import guard
import math

guard()
J = math.pi**1.5/(math.sqrt(2)*math.gamma(0.75)**2)
best = None
count = 0
for ai in range(12, 51):
    a = ai/10
    for bi in range(ai+1, 101):
        b = bi/10
        g = 1/(1+a)-b/(b*b+a)
        for vi in range(40, 121):
            v = vi/10
            t = (a-1)**2/v
            p = a*math.erfc(math.sqrt(v/2))
            d = J*math.sqrt(2/(math.pi*t))/math.e
            if b*p >= 1:
                continue
            left, right = 0., 1.
            for _ in range(40):
                theta = (left+right)/2
                if (1-theta)*math.exp(-theta) > b*p:
                    left = theta
                else:
                    right = theta
            theta = (left+right)/2
            s = b*d*math.exp(theta)/theta
            c = theta/s
            gap = g*c/math.log(b)
            count += 1
            if best is None or gap > best[0]:
                best = (gap, a, b, v, t, s, c, p, g, theta)
print("evaluations:", count)
print("best (gap,a,b,v,t,s,c,p,g,theta):", best)
for a, b, v, s, c in [(1.9, 3.4, 7.3, 21.5, 5/121),
                       (2., 3.5, 7., 20., 1/23)]:
    t = (a-1)**2/v
    h = (v*v+9*v+8)/(v*v+10*v+15)
    p_mills = a*math.sqrt(2/(math.pi*v))*math.exp(-v/2)*h
    energy_hi = (21/8)*math.sqrt(2/(math.pi*t))
    moment_hi = p_mills+energy_hi/(math.e*s)
    base = math.exp(s*c)*moment_hi
    g = 1/(1+a)-b/(b*b+a)
    gap = g*c/math.log(b)
    print("candidate a,b,v,s,c:", a,b,v,s,c)
    print("t,p_mills,energy_hi,moment_hi,tail_base,1/b,xi_upper:",
          t,p_mills,energy_hi,moment_hi,base,1/b,1-gap)
