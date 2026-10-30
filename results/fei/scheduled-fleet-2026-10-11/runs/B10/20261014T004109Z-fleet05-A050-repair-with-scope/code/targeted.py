from pathlib import Path
import json
SCRIPT=Path(__file__).resolve()
# Read definitions only, so importing does not launch the exhaustive search.
source=(SCRIPT.parent/'check.py').read_text(encoding='utf-8').split('fixtures=[];roots=0')[0]
exec(compile(source,str(SCRIPT.parent/'check.py'),'exec'),globals())
LIMIT=60
fixtures=[]
t=tuple((-1)**x.bit_count() for x in range(8))
q=evaluate(t,'adaptive',range(3),'three-bit-parity-adaptive')
ck(q['active_injection_vector']=={'2':'1'} and q['R']=='2' and q['a']=='3')
fixtures.append(q)
t=[]
for x in range(32):
    s,a,b=x&1,x>>1&1,x>>2&1;y=x>>3
    t.append(1 if not s else 1-2*(6>>y&1) if a else 1-2*(8>>y&1) if b else 1)
q=evaluate(tuple(t),'ctrl',range(3),'shared-data-positive-terminal-entropy')
ACTIVE=set(range(3));v=build(tuple(t),tuple(range(5)),'ctrl')
def leafentropy(v):
    if not v['children']:return ent(v['P'].values())
    return scale(add(*(leafentropy(c) for c in v['children'])),F(1,2))
le=leafentropy(v)
ck(le=={2:F(1,4)})
q['retained_terminal_fourier_entropy_vector']=serial(le)
fixtures.append(q)
r,k=2,3;INDEXED=(r,k);n=r*k+(1<<r);t=[]
for x in range(1<<n):
    sign=(-1)**((x>>(r*k)).bit_count())
    for j in range(r):
        if (x>>(j*k))&((1<<k)-1)==(1<<k)-1:sign=-sign
    t.append(sign)
active=list(range(0,r*k,k))+list(range(r*k,n))
q=evaluate(tuple(t),'indexed',active,'indexed-positive-injection-r2-k3')
p=F(1,2**(k-1));v=4*p*(1-p)
jk=add(ent((v/2,1-v/2)),scale(ent((v,1-v)),F(-1,2)))
expect=add({2:F(r)},scale(jk,-r))
ck(q['active_injection_vector']==serial(expect));nonneg(expect)
ck(bounds(expect)[0]>0)
ACTIVE=set(active);tree=build(tuple(t),tuple(range(n)),'indexed')
le=leafentropy(tree)
ck(le=={2:F(2)})
q['retained_terminal_fourier_entropy_vector']=serial(le)
fixtures.append(q)
out={'status':'PASS','cases':CASES,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,
     'fixtures':fixtures,'arithmetic':'exact coherent joints, rational probabilities, integer-log vectors and certified bounds'}
ck(CASES==3)
(ROOT/'out'/'TARGETED_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
