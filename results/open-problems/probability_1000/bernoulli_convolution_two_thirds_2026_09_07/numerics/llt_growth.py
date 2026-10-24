import math
from collections import defaultdict
def h(u):
    if abs(u)<1e-15: return 1.0
    return math.cos(3*math.pi*u)*math.sin(math.pi*u)/(math.pi*u)
for K in range(2,13):
    d={0:1.0}
    for i in range(K+1):
        c=(2**i)*(3**(K-i)); nd=defaultdict(float)
        for m,w in d.items():
            nd[m]+=w*0.5; nd[m+c]+=w*0.25; nd[m-c]+=w*0.25
        d=nd
    S=2.0**(K+1)*sum(w*h(m/2**K) for m,w in d.items())
    S1=2.0**(K+1)*sum(w*h(m/2**K) for m,w in d.items() if m>0)
    print(K, len(d), "full=%.6f"%S, "m>0 part=%.6f"%S1)
