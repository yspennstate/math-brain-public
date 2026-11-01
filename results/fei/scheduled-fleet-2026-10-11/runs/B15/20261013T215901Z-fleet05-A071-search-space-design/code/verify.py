import json,time
from collections import Counter
from fractions import Fraction as Q
import numpy as np
import search as s

start=time.perf_counter();out={}
rows=[json.loads(x) for x in (s.ROOT/'out/cases.jsonl').read_text().splitlines()]
def saved(n,mask):return next(x for x in rows if x['n']==n and x['mask']==mask)
def interval(data):return tuple(map(Q,data['rational_bounds']))

# Independent representation: actual18-bit truth table and exact integer spectrum.
n=18;N=1<<n;x=np.arange(N,dtype=np.int64);outer_input=np.zeros(N,dtype=np.int64)
for j in range(6):outer_input|=(((127>>((x>>(3*j))&7))&1) << j)
a=np.array([1-2*((s.SEED>>int(t))&1) for t in outer_input],dtype=np.int64)
c=a.copy();step=1
while step<N:
    blocks=c.reshape(-1,2*step);u=blocks[:,:step].copy();v=blocks[:,step:].copy()
    blocks[:,:step]=u+v;blocks[:,step:]=u-v;step*=2
assert int(c@c)==N*N
sq=c*c;Bs=[];Is=[];pair_hashes=[]
for i in range(n):
    base=x[(x&(1<<i))==0];pairs=np.stack((sq[base],sq[base|(1<<i)]),axis=1)
    unique,counts=np.unique(pairs,axis=0,return_counts=True)
    B=(Q(0),Q(0))
    for (aa,bb),count in zip(unique,counts):
        B=s.add(B,s.mul(s.phi_pair(Q(int(aa),N*N),Q(int(bb),N*N)),int(count)))
    I=Q(sum(map(int,sq[x&(1<<i)!=0])),N*N)
    edge=Q(int(np.count_nonzero(a!=a[x^(1<<i)])),N)
    assert I==edge==Q(63,65536)
    predicted=interval(saved(3,127)['coordinates'][i%3]['E_composed_coordinate'])
    actual=s.mul(B,1/I)
    assert max(actual[0],predicted[0])<=min(actual[1],predicted[1])
    assert actual[1]<Q(21,10)
    Bs.append(actual);Is.append(str(I));pair_hashes.append(s.hashlib.sha256(pairs.tobytes()).hexdigest())
assert all(b==Bs[0] for b in Bs)
out['actual18']={'core_negative_mask':127,'truth_table_sha256':s.hashlib.sha256(a.tobytes()).hexdigest(),
 'fourier_int_sha256':s.hashlib.sha256(c.tobytes()).hexdigest(),'all18_influences':Is,
 'all18_E_identical':True,'E':s.pack(Bs[0]),'proved_E_less_than':'21/10',
 'core_E_greater_than':'8/3','pair_hashes':pair_hashes}
assert interval(saved(3,127)['E_core'])[0]>Q(8,3)
(s.ROOT/'out/direct18_certificate.json').write_text(json.dumps(out['actual18'],indent=2),encoding='utf-8')

# Independently sum the two signed conditional sections of h on the other5 bits.
def independent(p,t):
    m=1-2*p;var=p*(1-p);packets=[];M=(Q(0),Q(0));q=Q(0)
    for T in range(32):
        C=B=Q(0)
        for z in range(32):
            h0=Q(1-2*((s.SEED>>(z<<1))&1));h1=Q(1-2*((s.SEED>>((z<<1)|1))&1))
            az=(h0+h1)/2;bz=(h0-h1)/2
            weight=p**z.bit_count()*(1-p)**(5-z.bit_count())
            basis=Q(1)
            for j in range(5):
                if T>>j&1:basis*=Q((z>>j)&1)-p
            C+=weight*basis*(az+m*bz);B+=weight*basis*bz
        d=var**T.bit_count();u=C*C/d;w=B*B/d
        q+=w;M=s.add(M,s.phi_pair(u,t*w));packets.append([str(u),str(t*w)])
    R=s.sub(M,s.mul(s.phi_pair(m*m,t),q))
    return q,R,packets
for name,mask in [('seed',s.SEED),('negative_seed',s.SEED^((1<<64)-1))]:
    row=saved(6,mask);p=Q(row['p']);t=Q(3,16)**2
    q,R,packets=independent(p,t)
    assert q==Q(row['q'])
    pred=interval(row['coordinates'][0]['reserve'])
    assert max(R[0],pred[0])<=min(R[1],pred[1])
    eratio=interval(row['E_composed'])
    assert all(r['singleton'] in ('-3/16','3/16') and r['influence_core']=='3/16' for r in row['coordinates'])
    if name=='seed':assert eratio[0]>Q(323,100) and eratio[1]<Q(324,100)
    else:assert eratio[1]<Q(8,3)
    out[name]={'p':str(p),'q':str(q),'reserve':s.pack(R),'E':row['E_composed'],
               'outer32_packets':packets,'all36_coordinates_equal_by_transitivity':True}
out['runtime_seconds']=time.perf_counter()-start
assert out['runtime_seconds']<55
(s.ROOT/'out/verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk in ('p','q','reserve','E','proved_E_less_than','all18_E_identical')} if isinstance(v,dict) else v for k,v in out.items()},indent=2))
