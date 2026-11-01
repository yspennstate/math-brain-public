import json,time
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parents[1];start=time.monotonic()
E=[(1<<3)|1|4,(1<<4)|1|2,(1<<5)|2|4]
f=[-1 if any(x&c==0 for c in E) else 1 for x in range(64)]
a=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(64)) for s in range(64)]
checks=0
for U in range(64):
    assert sum(a[S]*a[S^U] for S in range(64))==(4096 if not U else 0);checks+=1
assert [a[6],a[7],a[56],a[57]]==[-6,10,-2,-2];checks+=1
e=Q(sum(f[x]!=f[x^1] for x in range(64)),64)
assert e==Q(11,32);checks+=1
assert Q(a[7]**2,a[6]**2+a[7]**2)!=Q(a[57]**2,a[56]**2+a[57]**2);checks+=1
boundary=[]
for L in [4,8,16,32]:
    q=Q(1,1<<L)
    # Direct inclusion-exclusion of covering union sizes for c and ac.
    a_c=2*(-Q(1,4)-q/4+q/8+q/8+q*q/8-q*q/8)
    a_ac=2*(-Q(1,4)+q/8+q/8+q*q/8-q*q/8)
    assert a_c==-Q(1,2) and a_ac==-(1-q)/2;checks+=2
    Ipriv=L*q/2;Mlower=(1-q)**2/2
    assert Q(1,4)/((1-q)**2/4)>=1;checks+=1
    boundary.append({'L':L,'I_private_child':str(Ipriv),'M_shared_lower':str(Mlower),'M_over_I_private_lower':str(Mlower/Ipriv),
                     'parent_private_query_influence':str((1+(1-q)**2)/8),'child_reach':'1/2'})
ans={'all_signed_shifts':64,'exact_assertions':checks,'boundary':boundary,'runtime_seconds':time.monotonic()-start}
assert ans['runtime_seconds']<60
(R/'out/REPRODUCTION.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({'assertions':checks,'runtime_seconds':ans['runtime_seconds']}))
