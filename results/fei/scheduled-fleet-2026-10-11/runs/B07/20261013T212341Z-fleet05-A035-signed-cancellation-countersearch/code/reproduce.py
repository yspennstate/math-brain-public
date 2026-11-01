from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
def character(s,x):return -1 if (s&x).bit_count()%2 else 1
def direct(v):return [sum(y*character(s,x) for x,y in enumerate(v)) for s in range(len(v))]
def edges(v):
 n=len(v).bit_length()-1
 return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v)) for i in range(n)),len(v))
def b4(x):return (-1)**(((x&3)==3)+(((x>>2)&3)==3))
module=[b4(x)*(-1 if x==0 and z else 1) for z in range(2) for x in range(16)]
amp=direct(module);assert Counter(a*a for a in amp)=={36:10,100:6,4:16}
assert edges(module)==Q(37,16)
f=[]
for a in range(128):
 y=a&3;x=(a>>2)&15;z=(a>>6)&1
 f.append((-1)**((y==3)+(((y.bit_count()%2)==1) and x==0 and z))*b4(x))
af=direct(f);assert edges(f)==Q(101,32)
assert Q(sum(s.bit_count()*v*v for s,v in enumerate(af)),128**2)==edges(f)
g,h=f[:64],f[64:];u=[(a+b)//2 for a,b in zip(direct(g),direct(h))];v=[(a-b)//2 for a,b in zip(direct(g),direct(h))]
assert Counter(zip((a*a for a in u),(a*a for a in v)))=={(64,0):32,(36,4):20,(100,4):12}
for U in range(64):
 assert sum(u[s]*v[s^U] for s in range(64))==0
 assert sum(u[s]*u[s^U]+v[s]*v[s^U] for s in range(64))==(4096 if U==0 else 0)
D=[a*b for a,b in zip(g,h)];assert edges(D)/2==Q(3,16)
# beta>1/4, H(module)<37/8, and all good-order core-query nodes are good.
inequalities=[(2**48*13**39,3**45*5**50,'beta>1/4'),(3**45*5**75,2**216,'Hmodule<37/8'),(3*16**8,5*15**8,'mu_8>1/5'),(2**12,5**5,'h2(1/5)<4/5')]
assert all(left>right for left,right,label in inequalities)
result=dict(helper_version='A035-shared-parity-direct-reproduction-v1',runtime_seconds=time.perf_counter()-start,root_I=str(edges(f)),module_I=str(edges(module)),root_selector_W='3/16',root_selector_d='1/32',root_selector_pair_histogram={'64,0':32,'36,4':20,'100,4':12},all_64_shifts_checked=True,integer_inequalities=[dict(label=label,left=str(left),right=str(right),comparison='>') for left,right,label in inequalities],review_status='different implementation by same author; independent review pending')
assert time.perf_counter()-start<50
(ROOT/'out'/'reproduction.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
