"""All two-point edits of padded Maj3 at N=7, exact independent FWHT."""
import itertools, json, time
from fractions import Fraction as F
import validate as v

began=time.perf_counter()
N=7
size=1<<N
main=v.maj_tree(0,1)
tree=(main,v.binary_tree(list(range(3,N))))
base=[v.value(main,x) for x in range(size)]
a=v.fwht(base)
lengths=[len(v.encode(tree,s)) for s in range(size)]
den=size*size
Lg=sum(a[s]**2*lengths[s] for s in range(size))
cases=0
for x,y in itertools.combinations(range(size),2):
    table=base[:]
    table[x]*=-1
    table[y]*=-1
    z=v.fwht(table)
    for s in range(size):
        def delta(t):
            return -2*base[t]*(-1 if (s&t).bit_count()%2 else 1)
        v.ck(z[s]==a[s]+delta(x)+delta(y))
    v.ck(sum((z[s]-a[s])**2 for s in range(size))==8*size)
    I=sum(s.bit_count()*z[s]**2 for s in range(size))
    v.ck(F(v.direct_influence(table,N),size)==F(I,den))
    L=sum(lengths[s]*z[s]**2 for s in range(size))
    v.ck(F(L,den)<=12*F(I,den))
    v.ck(L<=2*Lg+2*sum(lengths[s]*(z[s]-a[s])**2 for s in range(size)))
    cases+=1
result={'helper_version':'A069-pairs-v1','N':N,'edit_count':2,'cases':cases,'assertions':v.checks,'seconds':time.perf_counter()-began,'arithmetic':'integer FWHT and exact rationals','result':'PASS'}
(v.RUN/'out'/'pairs_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
