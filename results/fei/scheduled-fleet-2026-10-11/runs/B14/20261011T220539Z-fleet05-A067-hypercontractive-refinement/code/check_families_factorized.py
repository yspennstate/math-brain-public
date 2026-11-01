import json
import time
from fractions import Fraction as Q
from pathlib import Path
from check import check_table, fwht, upper_degrees

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
assertions=0
rows=[]
for n in range(2,13):
    size=1<<n
    p=Q(1,size)
    for kind in ('point_defect','dictator_surgery'):
        values=[1]*size if kind=='point_defect' else [1 if not x&1 else -1 for x in range(size)]
        values[0]=-1
        assertions+=check_table(values,n)
        a=fwht(values)
        d=upper_degrees(a,n)
        q=[Q(x*x,size*size) for x in a]
        influence=sum(s.bit_count()*v for s,v in enumerate(q))
        u=sum(v*(d[s]-s.bit_count()) for s,v in enumerate(q) if s and v)
        dominant=0 if kind=='point_defect' else 1
        assert a[dominant]==size-2 and all(x==-2 for s,x in enumerate(a) if s!=dominant)
        if kind=='point_defect':
            assert influence==2*n*p and u==2*n*p-4*n*p*p and u<=influence
        else:
            assert influence==1+(2*n-4)*p
            assert u==n-1-(2*n-4)*p-4*n*p*p
        assertions+=3
        rows.append({'n':n,'family':kind,'I':str(influence),'U':str(u),'U_over_I':str(u/influence)})

tensor_rows=[]
anchor_count=0
majority=fwht([1 if x.bit_count()<=1 else -1 for x in range(8)])
for n in range(2,9):
    total=n+3
    size=1<<total
    defect_values=[-1]+[1]*((1<<n)-1)
    defect=fwht(defect_values)
    values=[(1 if (x&7).bit_count()<=1 else -1)*defect_values[x>>3] for x in range(size)]
    assertions+=check_table(values,total)
    a=fwht(values)
    for s,x in enumerate(a):
        assert x==majority[s&7]*defect[s>>3]
        assertions+=1
    influence=Q(sum(s.bit_count()*v*v for s,v in enumerate(a)),size*size)
    assert influence==Q(3,2)+Q(2*n,1<<n)
    assertions+=1
    minimum=None
    direct_checks=0
    for az in range(8):
        shifted_majority=[majority[z^az] for z in range(8)]
        dz=upper_degrees(shifted_majority,3)
        rz=[z for z,v in enumerate(shifted_majority) if v]
        assert len(rz)==4 and sum(z!=0 for z in rz)>=3
        assertions+=1
        # Each majority atom has squared mass 1/4; all y-supports are present.
        all_terms=sum(Q(n+dz[z]-1,2) for z in rz)
        for ay in range(1<<n):
            anchor=az | (ay<<3)
            local=all_terms
            if 0 in rz:
                local-=Q(defect[ay]**2,(1<<n)**2)*Q(n+dz[0]-1,2)
            assert local>=Q(3*n,2)
            assertions+=1
            anchor_count+=1
            if n<=4 or anchor in [0,1,7,size-1]:
                shifted=[a[s^anchor] for s in range(size)]
                d=upper_degrees(shifted,total)
                direct=Q(sum(2*v*v*(d[s]-1) for s,v in enumerate(shifted) if s and v),size*size)
                assert direct==local
                assertions+=1
                direct_checks+=1
            minimum=local if minimum is None else min(minimum,local)
            if time.perf_counter()-started>60:
                raise RuntimeError('factorized frozen runtime exceeded')
    tensor_rows.append({'n':n,'anchors':size,'I':str(influence),'minimum_local_envelope':str(minimum),'proved_lower_bound':str(Q(3*n,2)),'independent_full_transform_checks':direct_checks})

result={'complete':True,'rows':rows,'tensor_rows':tensor_rows,'assertions':assertions,'anchor_count':anchor_count,'elapsed_seconds':time.perf_counter()-started,'arithmetic':'integer Walsh, full transform, product support factorization, exact Fraction'}
(root/'out'/'check_families_factorized.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','tensor_rows']},indent=2))
