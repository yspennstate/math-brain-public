from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json
from bisect import bisect_right
def tops(p):
 t=[]
 for x in p:
  i=bisect_right(t,x)
  if i==len(t):t.append(x)
  else:t[i]=x
 return t
q125=Q(sum(tops(p)[:3]==[1,2,5] for p in permutations(range(1,6))),120)
q145=Q(sum(tops(p)[:3]==[1,4,5] for p in permutations(range(1,6))),120)
assert (q125,q145)==(Q(11,120),Q(1,20))
def bounds(g,h):
 u=g+h
 C=Q(1,6)+(g+h)/8+q145*g*g/2+Q(11,120)*g*h+q125*h*h/2
 F=Q(1,2)+g/3+g*g/16
 Ct=u**3/(6*(1-u/4))
 Ft=g**3/(6*(1-g/4))
 return C/(F+Ft),(C+Ct)/F
lo1,hi1=bounds(Q(1,100),Q(1,100));lo2,hi2=bounds(Q(1,50),Q(1,100))
assert lo2>hi1
res={'q125':str(q125),'q145':str(q145),'h':'1/100','g1':'1/100','g2':'1/50','C_over_F_interval_g1':[str(lo1),str(hi1)],'C_over_F_interval_g2':[str(lo2),str(hi2)],'strict_separation_lower_bound':str(lo2-hi1),'decimal_intervals':[[float(lo1),float(hi1)],[float(lo2),float(hi2)]]}
Path('interior_check.json').write_text(json.dumps(res,indent=2),encoding='utf8')
print(json.dumps(res,indent=2))
