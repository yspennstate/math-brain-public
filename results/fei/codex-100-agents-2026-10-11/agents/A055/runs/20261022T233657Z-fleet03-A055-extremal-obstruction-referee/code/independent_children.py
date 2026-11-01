"""Direct characters and physical edge counts; no primary checker imports."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;cases=[]
def ck(p):
 global checks
 assert p;checks+=1
for swap in [False,True]:
 C=[0,1,3,6,12,24,48,32]
 if swap:C[3],C[4]=C[4],C[3]
 root=[-1 if ((x&63)&C[x>>6]).bit_count()%2 else 1 for x in range(512)]
 I=Q(sum(root[x]!=root[x^(1<<j)] for x in range(512) for j in range(9)),512);ck(I==3)
 kids=[]
 for z in range(4):
  retained=[0,1,4,5,6,7,8];vals=[]
  for y in range(128):
   x=((z&1)<<2)+((z>>1)<<3)+sum(((y>>k)&1)<<j for k,j in enumerate(retained));vals.append(root[x])
  w=[sum(vals[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(128)) for s in range(128)]
  c=Counter(q*q for q in w if q);ck(c=={256:48,1024:4});ck(sum(q*q for q in w)==128**2)
  ii=Q(sum(vals[x]!=vals[x^(1<<j)] for x in range(128) for j in range(7)),128)
  ck(ii==Q(5,2) if swap else ii==Q(19 if z in [0,3] else 21,8))
  kids.append(str(ii))
 ck(sum(Q(x) for x in kids)/4==Q(5,2))
 cases.append({'weight_two_address':swap,'child_influences':kids,'each_child_spectrum_squared_numerator_counts':{'256':48,'1024':4},'denominator':16384,'entropy_bits':'11/2'})
out={'status':'PASS','assertions':checks,'actual_roots':2,'actual_pair_children':8,'method':'direct character sums of128-entry actual children plus physical edge counts; unequal child negative control at natural address4','cases':cases,'elapsed_seconds':time.perf_counter()-start}
(R/'out/INDEPENDENT_CHILDREN.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
