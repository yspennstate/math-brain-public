#!/usr/bin/env python3
"""Outward interval evaluation of Harangi (2025), Thm 1.2/Table 2.

No optimization: use exactly the printed decimal parameters. Sum symmetric
star terms by multisets, independently of the author's implementation.
"""
import itertools, json, math, pathlib
from mpmath import iv
iv.dps=50
ROOT=pathlib.Path(__file__).resolve().parents[1]
PARAMS={
3:('0.20304','0.27824','0.20662','0.48970','0.14372','0.93831','0.02348'),
4:('0.29823','0.34695','0.24571','0.68439','0.29092','0.95728','0.03657'),
5:('0.28496','0.29369','0.17626','0.54693','0.21655','0.94913','0.02047')}
def star(args,z):
    dp={(0,0):iv.mpf(1)}
    for a in args:
        new={}
        for (neg,pos),v in dp.items():
            for sign,p in enumerate(a):
                key=(neg+(sign==0),pos+(sign==2));new[key]=new.get(key,iv.mpf(0))+v*p
        dp=new
    return sum(v*z**min(neg,pos) for (neg,pos),v in dp.items())
def evaluate(d,parameters):
    z,m,p1,a,b,c,e=map(iv.mpf,parameters)
    p=[p1,p1,iv.mpf('.5')-p1,iv.mpf('.5')-p1]
    q=[(a,1-a-b,b),(b,1-a-b,a),(c,1-c-e,e),(e,1-c-e,c)]
    assert all(float(x.a)>0 for a in q for x in a)
    st=iv.mpf(0)
    for indices in itertools.combinations_with_replacement(range(4),d):
        counts=[indices.count(i) for i in range(4)];multiplicity=math.factorial(d)
        for count in counts:multiplicity//=math.factorial(count)
        weight=iv.mpf(multiplicity)
        for idx in indices:weight*=p[idx]
        st+=weight*star([q[idx] for idx in indices],z)**m
    ed=iv.mpf(0)
    for i in range(4):
        for j in range(4):
            f=1+(z-1)*(q[i][0]*q[j][0]+q[i][2]*q[j][2])
            ed+=p[i]*p[j]*f**m
    phi=(iv.log(st)-iv.mpf(d)/2*iv.log(ed))/(m*iv.log(1/z))
    gamma=1+iv.mpf(2)/d*phi
    # Strings retain directed endpoints; floats are display conveniences only.
    assert gamma < iv.mpf({3:'0.923868',4:'0.867902',5:'0.834638'}[d])
    return {'d':d,'parameters':parameters,'gamma_interval':str(gamma),'per_vertex_interval':str(gamma*d/2),'gamma_low_display':float(gamma.a),'gamma_high_display':float(gamma.b)}
rows=[evaluate(d,p) for d,p in PARAMS.items()]
for r in rows:
    safe={3:.923868,4:.867902,5:.834638}[r['d']]
    assert r['gamma_high_display']<safe
    print(json.dumps(r))
(ROOT/'data'/'harangi_intervals.json').write_text(json.dumps(rows,indent=2)+'\n')
