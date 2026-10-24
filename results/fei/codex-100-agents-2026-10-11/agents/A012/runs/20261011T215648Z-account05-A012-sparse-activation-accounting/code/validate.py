from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def walsh(table):
    a=list(table); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
        h*=2
    return [Q(x,len(a)) for x in a]
def influences(table):
    n=(len(table)-1).bit_length()
    return [Q(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]
def entropy_hist(probabilities):
    c=Counter(probabilities);c.pop(Q(0),None)
    return {str(p):m for p,m in sorted(c.items())}

for mask in range(256):
    g=[1 if mask>>x&1 else -1 for x in range(8)]
    gh=walsh(g);mu=gh[0];a=1-mu;Ig=sum(influences(g))
    ck(sum(x*x for x in gh)==1)
    ck(Ig==sum(i.bit_count()*h*h for i,h in enumerate(gh)))
    for r in (1,2,3):
        p=Q(1,1<<r)
        f=[g[x&7] if x>>3==0 else 1 for x in range(1<<(3+r))]
        fh=walsh(f)
        expected=[1-p*a if s==0 else (-p*a if s&7==0 else p*gh[s&7]) for s in range(len(f))]
        ck(fh==expected)
        ck(sum(x*x for x in fh)==1)
        ck(sum(influences(f))==p*Ig+r*p*a)
        ck(sum(s.bit_count()*h*h for s,h in enumerate(fh))==p*Ig+r*p*a)
        # Exact entropy ledger before any logarithms: identical atom histogram.
        atoms=[(1-p*a)**2]+[(p*a)**2]*((1<<r)-1)
        atoms += [p*p*h*h for h in gh[1:] for u in range(1<<r)]
        ck(entropy_hist(h*h for h in fh)==entropy_hist(atoms))

# Every allowed fan-in reduces to binary associative AND/OR/XOR, so this
# dynamic program enumerates the complete syntactic class, not a depth sample.
full=255
families={0:{0,full}}
for size in range(1,4):
    for ids in combinations(range(3),size):
        support=sum(1<<i for i in ids)
        tables={0,full}
        if size==1:
            i=ids[0];literal=sum(1<<x for x in range(8) if x>>i&1)
            tables.update((literal,full^literal))
        for left in range(1,support):
            if left&support!=left:continue
            right=support^left
            if not right:continue
            for u in families[left]:
                for v in families[right]:
                    for w in (u&v,u|v,u^v):tables.update((w,full^w))
        families[support]=tables
admitted=families[7]
mux=[(1 if x>>1&1 else -1) if x&1 else (1 if x>>2&1 else -1) for x in range(8)]
muxmask=sum(1<<i for i,v in enumerate(mux) if v==1)
ck(muxmask not in admitted)
mh=walsh(mux)
ck(mh[0]==0)
ck(influences(mux)==[Q(1,2)]*3)
ck(sorted(h*h for h in mh if h)==[Q(1,4)]*4)
restriction_checks=0
for mask in admitted:
    for i in range(3):
        for bit in (0,1):
            fixed=sum(1<<x for x in range(8) if mask>>((x&~(1<<i))|(bit<<i))&1)
            ck(fixed in admitted);restriction_checks+=1

def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
save('three_bit_admitted.json',{'count':len(admitted),'masks':sorted(admitted),'truth_table_convention':'mask bit x is Boolean +1; input bit 0 is selector'})
save('mux_certificate.json',{'truth_table':mux,'mask':muxmask,'walsh':[str(x) for x in mh],'influences':[str(x) for x in influences(mux)],'entropy_bits':2,'influence':'3/2','admitted':False})
save('validation.json',{'status':'PASS','assertions':checks,'core_count':256,'activation_count':768,'admitted_three_bit_count':len(admitted),'restriction_checks':restriction_checks,'arithmetic':'integer FWHT and Fraction only','seconds':time.perf_counter()-started,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
print((ROOT/'out'/'validation.json').read_text(encoding='utf-8'))
