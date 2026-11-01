import exact as e
from exact import Q,fwht,save,ck,cutoff
from collections import Counter
import math
counts=Counter();reps={}
for mask in range(256):
    cutoff();c=[1 if mask>>s&1 else -1 for s in range(8)];a=fwht(c)
    for W in range(256):
        b=fwht([c[s] if W>>s&1 else 0 for s in range(8)])
        p=(W.bit_count(),tuple(sorted((x,y) if y>0 or(y==0 and x>=0) else(-x,-y) for x,y in zip(a,b))))
        counts[p]+=1;reps.setdefault(p,(mask,W))
ps=sorted(counts)
best=(0,None)
def phi(a,b):
    return (a+b)*math.log2(a+b)-(a*math.log2(a) if a else 0)-(b*math.log2(b) if b else 0) if a+b else 0
for j,(m,p) in enumerate(ps):
    for i in range(1,513):
        t=i/512;d=m*t/8;df=min(d,1-d)
        if not df:continue
        B=2*(d-m*t*t/8)+sum(phi(float(a-t*b)**2,float(t*b)**2) for a,b in p)
        if B/df>best[0]:best=(B/df,(j,t))
save('ALL_PROFILES.json',{'status':'PASS','profiles':[{'m':m,'pairs':[[str(a),str(b)]for a,b in p]}for m,p in ps],'counts':[counts[p]for p in ps],'representatives':[reps[p]for p in ps],'discovery_max_ratio':best,'discovery_not_proof':True,'elapsed':__import__('time').perf_counter()-e.start})
print(len(ps),best)
