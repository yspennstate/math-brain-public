import json,time
from fractions import Fraction as Q
from pathlib import Path
from check_carrier import lg
R=Path(__file__).resolve().parents[1]
start=time.monotonic();checks=0;cases=0;rows=0
for n in range(4):
    N=1<<n
    for code in range(1<<N):
        f=[1-2*((code>>x)&1) for x in range(N)]
        # Deliberately use direct characters, not author's Walsh helper.
        a=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
        for i in range(n):
            edge_support=sum(f[x]!=f[x^(1<<i)] for x in range(N))
            eps=Q(edge_support,N)
            energy=Q(sum(a[s]**2 for s in range(N) if s>>i&1),N*N)
            assert energy==eps;checks+=1
            mass=Q(sum(a[(1<<i)|(1<<j)]**2 for j in range(n) if j!=i),N*N)
            if eps:
                # Natural log lower enclosure = log2 lower * ln2 lower.
                from check_carrier import ln_unit
                loglower=lg(2/eps)[0]*ln_unit(Q(2))[0]
                assert mass<=2*eps*eps*loglower;checks+=1
            else:assert mass==0;checks+=1
            rows+=1
        cases+=1
e=Q(27,10);ln2=Q(69,100);sqrt2=Q(71,50)
K2=8/(e*e*ln2)+2/e+sqrt2/(e*ln2)
K12=2*K2+1/ln2
assert K2==Q(155600,50301) and K12==Q(16700,2187) and K12<8;checks+=3
# This product-law control violates the sparse derivative inequality.
# Scaling by 128^2, its row mass is 127*(127/128)^126 >16,
# whereas 2 ln256 =16 ln2 <16.
assert 127*127**126>16*128**126;checks+=1
# Source two-level real vector has I=3/2 and T12>=log2((n-1)/2).
ncontrol=65537
assert (ncontrol-1)//2==1<<15 and Q(15)/Q(3,2)>K12;checks+=2
ans={'Boolean_cases':cases,'physical_coordinate_rows':rows,'exact_assertions':checks,
 'K2_rational':str(K2),'K12_rational':str(K12),
 'product_control_n':128,'sparse_derivative_failure':'127*127^126>16*128^126; 2 ln256<16',
 'two_level_control_n':ncontrol,'T12_over_I_lower':'10','runtime_seconds':time.monotonic()-start}
assert cases==278 and ans['runtime_seconds']<60
(R/'out/LEVEL12_REVIEW.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps(ans))
