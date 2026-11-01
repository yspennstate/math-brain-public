import exact as e
from exact import Q,ck,cutoff,save,Lv,add,scalar,vint,fwht,inf,entropy,cross
from collections import Counter
import time
profiles=[(Q(1),)+(Q(0),)*7,(Q(1,2),)*3+(Q(-1,2),)+(Q(0),)*4,(Q(3,4),)+(Q(1,4),)*4+(Q(-1,4),)*3,(Q(-3,4),)+(Q(1,4),)*7]
def packet(A,B):return add((1,Lv(A)),(1,Lv(B)),(-1,Lv(A+B)))
certs=[];min_lower=None
for pi,profile in enumerate(profiles):
    for i in range(256):
        cutoff();lo=Q(1,32)+Q(3*i,8192);hi=Q(1,32)+Q(3*(i+1),8192)
        upper={}
        for c in profile:
            Amax=max((c-lo)**2,(c-hi)**2);upper=add((1,upper),(1,packet(Amax,hi*hi)))
        gap=add((1,scalar(2*lo+16*lo*lo)),(-1,upper));I=vint(gap);ck(I[0]>0)
        rounded=Q((I[0]*(1<<48)).numerator//(I[0]*(1<<48)).denominator,1<<48);ck(rounded>0 and rounded<=I[0])
        certs.append({'profile':pi,'lo':str(lo),'hi':str(hi),'gap_lower':str(rounded)})
        min_lower=rounded if min_lower is None else min(min_lower,rounded)
    save('CONTINUUM_PARTIAL.json',{'status':'PASS_COMPLETED_PROFILES_ONLY','completed_profiles':pi+1,'certificates':certs})
counts=Counter();representatives={}
for mask in range(256):
    c=[1 if mask>>s&1 else -1 for s in range(8)];hat=fwht(c)
    for w in range(8):
        rel=tuple(sorted(hat[t]*c[w]*((-1)**((t&w).bit_count())) for t in range(8)))
        pi=[tuple(sorted(x)) for x in profiles].index(rel);ck(pi>=0);counts[pi]+=1;representatives.setdefault(pi,(c,w))
save('CONTINUUM_CERTIFICATES.json',{'status':'PASS','box_count':len(certs),'uniform_positive_lower':str(min_lower),'profiles':[[str(x) for x in p] for p in profiles],'classification_counts':dict(counts),'certificates':certs,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start})
save('REPRESENTATIVES.json',{str(k):{'c':c,'w':w} for k,(c,w) in representatives.items()})
print({'status':'PASS','boxes':len(certs),'min_gap':str(min_lower),'assertions':e.checks,'seconds':time.perf_counter()-e.start})
