from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261013T212321Z-account05-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)};exec(OLD.read_text(encoding='utf-8').split('for n in (1,2,3):')[0],ns)
expr,add,const,stats,child,reserve,positive=[ns[k] for k in ('expr','add','const','stats','child','reserve','positive')]
ZERO=();START=time.perf_counter();pilot='--pilot' in sys.argv;LIMIT=55 if pilot else 595
checks=0;counts=dict(roots=0,controller_faces=0,data_faces=0,payload_prices=0,positive_correction_faces=0)
def ck(v):
    global checks
    checks+=1;assert v,checks;assert time.perf_counter()-START<LIMIT,'frozen runtime guard'
def phi(s):
    if not s:return ZERO
    d={}
    for p,e in ns['factors'](s.denominator).items():d[p]=s*e
    for p,e in ns['factors'](s.numerator).items():d[p]=d.get(p,F(0))-s*e
    return expr(d)
def mix(labels,cores):
    return tuple(cores[labels[x&3]][(x>>(2+labels[x&3]))&1] for x in range(32))
def weights(m):
    return tuple((1+m[(j+1)%3]*m[(j+2)%3]-m[j]*(m[(j+1)%3]+m[(j+2)%3]))/4 for j in range(3))
def cuts(labels):return [tuple(-1 if label==j else 1 for label in labels) for j in range(3)]
def payload(labels,m,order,C):
    w=weights(m);t=cuts(labels)
    return add(*((w[j],reserve(t[j],order,C)) for j in range(3)))
def direct_payload(labels,m,order,C):
    values=[]
    for e in product((-1,1),repeat=3):
        prob=F(1)
        for j in range(3):prob*=(1+e[j]*m[j])/2
        t=tuple(e[label] for label in labels)
        values.append((prob,reserve(t,order,C)))
    return add(*values)
def bank(labels,m):
    q=[F(labels.count(j),len(labels)) for j in range(3)]
    return add(*((1-m[j]*m[j],phi(q[j])) for j in range(3)))
def dec(t,i):return add((1,stats(t)[0]),(-F(1,2),stats(child(t,i,0))[0]),(-F(1,2),stats(child(t,i,1))[0]))
best=ZERO;best_record=None
named=[(1,1),(-1,-1),(1,-1)]
maps=list(product(range(3),repeat=4));maps=maps[:3] if pilot else maps
for labels in maps:
    ts=cuts(labels)
    for cores in product(named,repeat=3):
        m=tuple(F(sum(t),2) for t in cores);w=weights(m);f=mix(labels,cores);H,di=stats(f)
        ck(all(x>=0 for x in w));ck(sum(w)<=1)
        for j in range(3):
            for k in range(j+1,3):ck(w[j]+w[k]==(1-m[j]*m[k])/2)
        for i in (0,1):
            ck(di[i]==sum((w[j]*stats(ts[j])[1][i] for j in range(3)),F(0)))
            dc=add(*((w[j],dec(ts[j],i)) for j in range(3)))
            R=bank(labels,m);lc=[child(labels,i,s) for s in (0,1)]
            release=add((1,R),(-F(1,2),bank(lc[0],m)),(-F(1,2),bank(lc[1],m)))
            ck(positive(add((-1,release)))==ZERO)
            E=add((1,dec(f,i)),(-1,dc),(-1,release))
            if not di[i]:ck(E==ZERO)
            else:
                ratio=add((1/di[i],E))
                if positive(ratio):counts['positive_correction_faces']+=1
                if positive(add((1,ratio),(-1,best))):best=ratio;best_record=dict(labels=list(labels),means=[str(x) for x in m],query=i,influence=str(di[i]))
            for C in (0,1,4):
                order=(i,1-i);P=payload(labels,m,order,C)
                pc=[payload(lc[s],m,(0,),C) for s in (0,1)]
                ck(positive(add((1,dc),(-1,const(C*di[i])),(-1,P),(F(1,2),pc[0]),(F(1,2),pc[1])))==ZERO)
            counts['controller_faces']+=1
        for C in (0,1,4):
            P=payload(labels,m,(0,1),C)
            ck(P==direct_payload(labels,m,(0,1),C))
            for j in range(3):
                children=[]
                for sign in (0,1):
                    mm=list(m);mm[j]=F(cores[j][sign]);children.append(payload(labels,tuple(mm),(0,1),C))
                ck(P==add((F(1,2),children[0]),(F(1,2),children[1])))
            counts['payload_prices']+=1
        counts['data_faces']+=3;counts['roots']+=1
    stats.cache_clear();reserve.cache_clear()
# Full raw witness, preserving two control and three data bits.
labels=(0,0,1,2);m=(F(0),)*3;cores=((1,-1),)*3;f=mix(labels,cores);t=cuts(labels)
q=[reserve(t[j],(1,0),1) for j in range(3)]
ck(q==[ZERO,const(F(3,2)),const(F(3,2))]);ck(payload(labels,m,(1,0),1)==const(F(3,4)))
ck(stats(f)[0]==const(3));ck(sum(stats(f)[1][:2])==F(3,4));ck(sum(stats(f)[1][2:])==1)
ck(bank(labels,m)==const(F(3,2)));ck(reserve(f,(1,0,2,3,4),1)==const(F(9,4)))
live=child(f,1,1);ck(reserve(live,(0,1,2,3),1)==const(F(3,2)))
# It is the ACTUAL restricted label map, with unchanged independent core means.
lc=child(labels,1,1);ck(bank(lc,m)==const(1));ck(payload(lc,m,(0,),1)==ZERO)
ck(add((1,dec(live,0)),(-1,const(1)))==const(1));ck(stats(live)[1][0]==F(1,2))
out=dict(status='PASS',pilot=pilot,helper_version='A030-three-cut-payload-v1',checks=checks,counts=counts,maximum_positive_correction_ratio=[(p,str(c)) for p,c in best],maximum_ratio_bounds=[str(x) for x in ns['bounds'](best)],maximizer=best_record,certified_nonzero_signs=ns['signs'],exact_zero_signs=ns['zeros'],elapsed_seconds=time.perf_counter()-START,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest(),arithmetic='Fraction prime-log expressions; exact symbolic comparisons; rational atanh sign intervals')
(ROOT/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
