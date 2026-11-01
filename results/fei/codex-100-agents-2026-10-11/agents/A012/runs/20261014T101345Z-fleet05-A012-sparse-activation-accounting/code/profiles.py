import exact as e
from exact import Q,fwht,save,ck
import math
from collections import Counter
def profile(c):
    a=fwht(c);b=fwht([c[s] if s in (0,1,2) else 0 for s in range(8)])
    return tuple(sorted((x,y) if y>0 or (y==0 and x>=0) else (-x,-y) for x,y in zip(a,b)))
counts=Counter();reps={}
for mask in range(256):
    c=[1 if mask>>s&1 else -1 for s in range(8)];p=profile(c);counts[p]+=1;reps.setdefault(p,mask)
ps=sorted(counts)
def phi(a,b):
    return (a+b)*math.log2(a+b)-(a*math.log2(a) if a else 0)-(b*math.log2(b) if b else 0) if a+b else 0
best=(0,None)
for j,p in enumerate(ps):
    for i in range(1,1025):
        t=i/1024;d=3*t/8;delta=3*t*t/8
        B=2*(d-delta)+sum(phi(float(a-t*b)**2,float(t*b)**2) for a,b in p)
        if B/d>best[0]:best=(B/d,(j,t))
save('PROFILES.json',{'status':'PASS','profiles':[[[str(a),str(b)] for a,b in p] for p in ps],'counts':[counts[p] for p in ps],'representatives':[reps[p] for p in ps],'discovery_max_ratio':best,'discovery_not_proof':True})
print(len(ps),best)
